import cv2
import mediapipe as mp
import numpy as np
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.metrics import dp
from gtts import gTTS
import os
import threading
from playsound import playsound

# Configuración de MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

KV = '''
<DeteccionSeñasScreen>:
    name: 'deteccion_señas'
    md_bg_color: 0.1, 0.1, 0.1, 1

    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(10)
        spacing: dp(10)

        # Header con botón de regreso
        MDBoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(50)
            md_bg_color: 0.2, 0.2, 0.2, 1
            padding: dp(10)

            MDIconButton:
                icon: 'arrow-left'
                on_release: 
                    root.stop_camera()
                    app.root.current = 'home'
                theme_icon_color: "Custom"
                icon_color: 1, 1, 1, 1

            MDLabel:
                text: 'Detección de Señas'
                halign: 'center'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                font_size: '18sp'

        # Área de video
        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: 0.7
            padding: dp(10)
            md_bg_color: 0.05, 0.05, 0.05, 1

            CameraWidget:
                id: camera_widget
                size_hint: 1, 1

        # Panel de controles
        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: 0.3
            padding: dp(10)
            spacing: dp(10)
            md_bg_color: 0.15, 0.15, 0.15, 1

            # Estado de la cámara
            MDLabel:
                id: status_label
                text: 'Cámara: Desconectada'
                halign: 'center'
                theme_text_color: 'Custom'
                text_color: 0.8, 0.8, 0.8, 1
                size_hint_y: None
                height: dp(30)

            # Resultado de detección
            MDLabel:
                id: result_label
                text: 'Seña detectada: Ninguna'
                halign: 'center'
                theme_text_color: 'Custom'
                text_color: 0.9, 0.9, 0.9, 1
                font_size: '16sp'
                size_hint_y: None
                height: dp(30)

            # Botones de control
            MDBoxLayout:
                orientation: 'horizontal'
                size_hint_y: None
                height: dp(50)
                spacing: dp(20)
                padding: dp(10)

                MDRaisedButton:
                    id: camera_button
                    text: 'Iniciar Cámara'
                    on_release: root.toggle_camera()
                    md_bg_color: 0.2, 0.6, 0.2, 1
                    size_hint_x: 0.5

                MDRaisedButton:
                    text: 'Reproducir Audio'
                    on_release: root.speak_detected()
                    md_bg_color: 0.6, 0.2, 0.6, 1
                    size_hint_x: 0.5
'''

Builder.load_string(KV)

class CameraWidget(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.capture = None
        self.hands = mp_hands.Hands(
            model_complexity=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5,
            max_num_hands=2
        )
        self.detected_sign = None
        self.is_camera_on = False

    def start_camera(self):
        self.capture = cv2.VideoCapture(0)
        if self.capture.isOpened():
            self.is_camera_on = True
            Clock.schedule_interval(self.update, 1.0 / 30.0)
            return True
        return False

    def stop_camera(self):
        self.is_camera_on = False
        if self.capture:
            self.capture.release()
        self.capture = None
        Clock.unschedule(self.update)

    def update(self, dt):
        if not self.is_camera_on or not self.capture:
            return

        ret, frame = self.capture.read()
        if ret:
            # Procesar frame para detección de manos
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(frame_rgb)

            # Dibujar landmarks de las manos
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        frame,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style()
                    )

                # Detectar seña
                self.detected_sign = self.detect_sign(results.multi_hand_landmarks[0])
                # Actualizar la pantalla
                self.parent.parent.parent.update_detection(self.detected_sign)
            else:
                self.detected_sign = None
                self.parent.parent.parent.update_detection(None)

            # Convertir frame para Kivy
            buf = cv2.flip(frame, 0)
            buf = buf.tobytes()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.texture = texture

    def detect_sign(self, hand_landmarks):
        """Detectar seña basada en la posición de los landmarks"""
        landmarks = []
        for lm in hand_landmarks.landmark:
            landmarks.append([lm.x, lm.y, lm.z])

        # Convertir a numpy array
        landmarks = np.array(landmarks)

        # Detectar gestos básicos
        if self.is_hello_sign(landmarks):
            return "Hola"
        elif self.is_thanks_sign(landmarks):
            return "Gracias"
        elif self.is_yes_sign(landmarks):
            return "Sí"
        elif self.is_no_sign(landmarks):
            return "No"
        elif self.is_good_sign(landmarks):
            return "Bien"
        elif self.is_bad_sign(landmarks):
            return "Mal"
        
        return None

    def is_hello_sign(self, landmarks):
        """Detectar seña de saludo"""
        # Pulgar extendido, otros dedos cerrados
        thumb_tip = landmarks[4]
        thumb_ip = landmarks[3]
        index_tip = landmarks[8]
        index_pip = landmarks[6]
        
        # Verificar si el pulgar está extendido y otros dedos cerrados
        if (thumb_tip[1] < thumb_ip[1] and  # Pulgar extendido
            index_tip[1] > index_pip[1]):    # Índice cerrado
            return True
        return False

    def is_thanks_sign(self, landmarks):
        """Detectar seña de gracias"""
        # Mano plana hacia arriba
        wrist = landmarks[0]
        middle_tip = landmarks[12]
        middle_pip = landmarks[10]
        
        # Verificar si la mano está plana
        if abs(middle_tip[1] - middle_pip[1]) < 0.05:
            return True
        return False

    def is_yes_sign(self, landmarks):
        """Detectar seña de sí (pulgar arriba)"""
        thumb_tip = landmarks[4]
        thumb_ip = landmarks[3]
        
        if thumb_tip[1] < thumb_ip[1]:  # Pulgar hacia arriba
            return True
        return False

    def is_no_sign(self, landmarks):
        """Detectar seña de no (pulgar abajo)"""
        thumb_tip = landmarks[4]
        thumb_ip = landmarks[3]
        
        if thumb_tip[1] > thumb_ip[1]:  # Pulgar hacia abajo
            return True
        return False

    def is_good_sign(self, landmarks):
        """Detectar seña de bien (pulgar arriba)"""
        return self.is_yes_sign(landmarks)

    def is_bad_sign(self, landmarks):
        """Detectar seña de mal (pulgar abajo)"""
        return self.is_no_sign(landmarks)

class DeteccionSeñasScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_sign = None

    def toggle_camera(self):
        camera_widget = self.ids.camera_widget
        status_label = self.ids.status_label
        camera_button = self.ids.camera_button

        if not camera_widget.is_camera_on:
            if camera_widget.start_camera():
                status_label.text = 'Cámara: Conectada'
                camera_button.text = 'Detener Cámara'
                camera_button.md_bg_color = 0.8, 0.2, 0.2, 1
            else:
                status_label.text = 'Error: No se pudo conectar la cámara'
        else:
            camera_widget.stop_camera()
            status_label.text = 'Cámara: Desconectada'
            camera_button.text = 'Iniciar Cámara'
            camera_button.md_bg_color = 0.2, 0.6, 0.2, 1
            self.ids.result_label.text = 'Seña detectada: Ninguna'

    def stop_camera(self):
        self.ids.camera_widget.stop_camera()

    def speak_detected(self):
        if self.current_sign:
            threading.Thread(target=self.speak_text, args=(self.current_sign,)).start()

    def speak_text(self, text):
        try:
            tts = gTTS(text=text, lang='es')
            tts.save("temp.mp3")
            playsound("temp.mp3")
            os.remove("temp.mp3")
        except Exception as e:
            print(f"Error al reproducir audio: {e}")

    def update_detection(self, sign):
        self.current_sign = sign
        if sign:
            self.ids.result_label.text = f'Seña detectada: {sign}'
        else:
            self.ids.result_label.text = 'Seña detectada: Ninguna' 