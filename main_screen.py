from kivy.uix.accordion import FloatLayout
import os
import cv2
import speech_recognition as sr
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.graphics.texture import Texture
from kivy.lang import Builder
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivy.metrics import dp
from diccionario import diccionario

# Ruta base para archivos de video
base_path = "videos/"

kv_string = '''
#:import dp kivy.metrics.dp
<MainScreen>:
    name: 'main_screen'
    md_bg_color: 0.1, 0.1, 0.1, 1  # Fondo oscuro

    FloatLayout:
        canvas.before:
            Color:
                rgba: 0.1, 0.1, 0.1, 1  # Fondo oscuro
            Rectangle:
                pos: self.pos
                size: self.size

            Color:
                rgba: 0.9, 0.1, 0.2, 1
            Ellipse:
                pos: -dp(100), self.height - dp(130)
                size: dp(300), dp(300)
            Ellipse:
                pos: self.width - dp(150), -dp(100)
                size: dp(300), dp(300)

        MDBoxLayout:
            orientation: 'vertical'
            padding: dp(8)
            spacing: dp(8)
            pos_hint: {"center_x": .5, "center_y": .5}
            size_hint: 0.9, 0.9
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 0.7  # Fondo ligeramente transparente
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [dp(12)]

            MDBoxLayout:
                orientation: 'horizontal'
                size_hint_y: None
                height: dp(53)
                padding: dp(3)
                spacing: dp(-50)
                canvas.before:
                    Color:
                        rgba: 0.2, 0.2, 0.2, 1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [dp(12)]

                MDIconButton:
                    icon: 'home'  # Ícono de flecha
                    on_release: 
                        root.manager.transition.direction = "right"
                        app.root.current = 'home'  # Regresar a la pantalla principal
                    theme_icon_color: "Custom"
                    icon_color: [1, 1, 1, 1]  # Blanco

                MDLabel:
                    text: 'Reconocimiento de Voz'
                    halign: 'center'
                    theme_text_color: 'Custom'
                    text_color: [1, 1, 1, 1]
                    font_size: '18sp'

            MDLabel:
                id: status_label
                text: '¡Listo para escuchar!'
                halign: 'center'
                theme_text_color: 'Custom'
                text_color: [1, 1, 1, 1]  # Texto blanco
                font_size: '24sp'
                size_hint_y: None
                height: dp(50)

            MDLabel:
                id: reconocido_label
                text: ''
                halign: 'center'
                theme_text_color: 'Custom'
                text_color: [0.9, 0.9, 0.9, 1]  # Texto gris claro
                font_size: '18sp'
                size_hint_y: None
                height: dp(30)

            BoxLayout:
                size_hint_y: 1  # Asegurarse de que ocupe todo el espacio restante
                Image:
                    id: video_player
                    allow_stretch: True
                    keep_ratio: True  # Mantener la proporción
                    size_hint_y: 1  # Asegurarse de que ocupe toda la altura
                    size_hint_x: 1  # Asegurarse de que ocupe toda la anchura

            MDIconButton:
                icon: 'microphone'
                pos_hint: {'center_x': 0.5}
                size_hint: None, None
                size: dp(120), dp(120)
                md_bg_color: [0.2, 0.2, 0.2, 1]  # Transparente
                on_release: root.start_recognition()
                theme_icon_color: "Custom"
                icon_color: [1, 1, 1, 1]  # Color azul claro

            MDLabel:
                text: 'Presiona el micrófono y habla'
                halign: 'center'
                theme_text_color: 'Custom'
                text_color: [0.7, 0.7, 0.7, 1]  # Gris claro
                size_hint_y: None
                height: dp(30)
'''

Builder.load_string(kv_string)

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.palabras_en_espera = []
        self.cap = None

    def start_recognition(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.ids.status_label.text = "Escuchando..."
            audio = recognizer.listen(source)
            try:
                texto = recognizer.recognize_google(audio, language='es-ES')
                self.ids.status_label.text = f"Texto reconocido: {texto}"
                self.procesar_oracion(texto)
            except sr.UnknownValueError:
                self.ids.status_label.text = "No se pudo entender el audio"
            except sr.RequestError as e:
                self.ids.status_label.text = f"Error en el servicio de reconocimiento: {e}"

    def obtener_ruta_video(self, palabra):
        categoria = diccionario.get(palabra)
        if categoria == "S":
            return f"{base_path}sujeto/{palabra}.mp4"
        elif categoria == "O":
            return f"{base_path}objeto/{palabra}.mp4"
        elif categoria == "V":
            return f"{base_path}verbo/{palabra}.mp4"
        elif categoria == "T":
            return f"{base_path}tiempo/{palabra}.mp4"
        elif categoria == "L":
            return f"{base_path}lugar/{palabra}.mp4"
        else:
            return None

    def reordenar_oracion(self, oracion):
        palabras = oracion.lower().split()
        categorias = {'T': [], 'L': [], 'S': [], 'O': [], 'V': []}
        
        for palabra in palabras:
            if palabra in diccionario:
                categorias[diccionario[palabra]].append(palabra)
        
        oracion_reordenada = categorias['T'] + categorias['L'] + categorias['S'] + categorias['O'] + categorias['V']
        
        return " ".join(oracion_reordenada)

    def mostrar_video(self, palabra):
        video_path = self.obtener_ruta_video(palabra)
        if not video_path:
            self.ids.status_label.text = f"No se encontró video para: {palabra}"
            return
        
        if not os.path.exists(video_path):
            self.ids.status_label.text = f"Archivo de video no encontrado: {video_path}"
            return

        self.cap = cv2.VideoCapture(video_path)
        self.frame_rate = self.cap.get(cv2.CAP_PROP_FPS) or 35
        Clock.schedule_interval(self.update_frame, 1.0 / self.frame_rate)

    def update_frame(self, dt):
        if self.cap is None:
            return False

        ret, frame = self.cap.read()
        if ret:
            buffer = cv2.flip(frame, 0).tobytes()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
            self.ids.video_player.texture = texture
        else:
            self.cap.release()
            self.cap = None
            if self.palabras_en_espera:
                Clock.schedule_once(self.play_next_video, 1.0 / self.frame_rate)
            else:
                self.ids.video_player.texture = None
                return False

    def play_next_video(self, dt):
        if self.palabras_en_espera:
            palabra = self.palabras_en_espera.pop(0)
            self.mostrar_video(palabra)

    def procesar_oracion(self, oracion):
        self.ids.status_label.text = f"Texto reconocido: {oracion}"
        oracion_reordenada = self.reordenar_oracion(oracion)
        self.palabras_en_espera = oracion_reordenada.split()
        if self.palabras_en_espera:
            palabra = self.palabras_en_espera.pop(0)
            self.mostrar_video(palabra)
