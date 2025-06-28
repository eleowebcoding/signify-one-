from kivy.uix.screenmanager import ScreenManager, FadeTransition, Screen
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Ellipse
from kivy.clock import Clock
from kivy.metrics import dp
from mutagen.mp3 import MP3
import random
import threading
import os
import speech_recognition as sr
from gtts import gTTS
from datetime import datetime
import time
import math
from pantalla_principal import HomeScreen
from main_screen import MainScreen
from drag_and_drop_screen import JuntaPalabrasScreen
from pantalla_principal import HomeScreen
from main_screen import MainScreen
from drag_and_drop_screen import JuntaPalabrasScreen
from kivy.uix.screenmanager import CardTransition
from newpalabra_screen import NewPalabraScreen
from deteccion_señas import DeteccionSeñasScreen
from diccionario_screen import DiccionarioScreen
from configuracion_screen import ConfiguracionScreen


# Configura el tamaño de la ventana
Window.size = (370, 670)

KV = '''
<VoiceAssistantScreen>:
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 0.1, 0.1, 0.25, 1  # Fondo azul oscuro
            Rectangle:
                pos: self.pos
                size: self.size

        MDBoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(53)
            md_bg_color: 0.6, 0.2, 0.8, 0.3  # Un azul muy oscuro para un look más sofisticado
            MDIconButton:
                icon: 'home'
                md_bg_color: 0.6, 0.2, 0.8, 0.0 # Un cian brillante para un toque futurista
                on_release: 
                    app.root.current = 'home'  # Regresar a la pantalla principal
                theme_icon_color: "Custom"
                icon_color: [1,1,1,1]  # Contraste con el fondo cian

        BoxLayout:
            orientation: 'vertical'
            padding: dp(20)
            spacing: dp(20)

            canvas.before:
                Color:
                    rgba: 0.1, 0.1, 0.25, 1 # Fondo azul muy oscuro
                Rectangle:
                    pos: self.pos
                    size: self.size


            MDLabel:
                text: "¿Cómo puedo ayudarte?"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0.8, 0.2, 0.6, 0.8  # Texto cian neón
                font_style: "H6"
                size_hint_y: None
                height: dp(20)

            MDIconButton:
                icon: 'microphone'
                size_hint: None, None
                size: dp(100), dp(100)
                md_bg_color: 0.6, 0.2, 0.8, 0.3   # Botón cian neón
                on_release: root.start_listening()
                theme_icon_color: "Custom"
                icon_color: 1,1,1,1  # Contraste con el fondo cian
                pos_hint: {'center_x': 0.5}
                canvas.before:
                    Color:
                        rgba: 0.6, 0.2, 0.8, 0.3
                    Ellipse:
                        pos: self.center_x - self.width/2, self.center_y - self.height/2
                        size: self.size

        BoxLayout:
            size_hint_y: None
            height: dp(30)
            md_bg_color: 0.05, 0.05, 0.1, 1
'''

class CircleAnimation(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.circle_radius = dp(125)
        self.angle = 0
        self.animating = False
        self.idle_animating = False

        with self.canvas.before:
            # Anillo exterior púrpura translúcido
            self.outer_color = Color(0.6, 0.2, 0.8, 0.3)
            self.outer_ring = Ellipse(
                size=(self.circle_radius * 2 + dp(60), self.circle_radius * 2 + dp(60)),
                pos=(self.center_x - self.circle_radius - dp(30), self.center_y - self.circle_radius - dp(30))
            )
            # Anillo interior azul brillante
            self.inner_color = Color(0.2, 0.6, 0.8, 1)
            self.inner_ring = Ellipse(
                size=(self.circle_radius * 2, self.circle_radius * 2),
                pos=(self.center_x - self.circle_radius, self.center_y - self.circle_radius)
            )

        with self.canvas:
            # Círculo central
            self.color = Color(0.8, 0.2, 0.6, 0.8)
            self.circle = Ellipse(size=(self.circle_radius * 2, self.circle_radius * 2), pos=self.center)

        self.bind(pos=self.update_circle, size=self.update_circle)
        self.start_idle_animation()

    def update_circle(self, *args):
        self.circle.pos = (self.center_x - self.circle_radius, self.center_y - self.circle_radius)
        self.outer_ring.pos = (self.center_x - self.circle_radius - dp(30), self.center_y - self.circle_radius - dp(30))
        self.inner_ring.pos = (self.center_x - self.circle_radius, self.center_y - self.circle_radius)

    def animate_circle(self, dt):
        if not self.animating:
            return
        self.angle = (self.angle + 4) % 360  # Cambio en la dirección de rotación
        scale = 1 + 0.15 * math.sin(math.radians(self.angle))  # Efecto de pulso

        # Dinamismo de los anillos
        outer_scale = 1 + 0.1 * math.cos(math.radians(self.angle * 2))
        inner_scale = 1 + 0.08 * math.sin(math.radians(self.angle * 2))

        # Rotación de anillos
        self.outer_ring.size = (self.circle_radius * 2 * outer_scale + dp(60), self.circle_radius * 2 * outer_scale + dp(60))
        self.inner_ring.size = (self.circle_radius * 2 * inner_scale, self.circle_radius * 2 * inner_scale)

        # Color dinámico
        self.outer_color.rgba = (0.6 + 0.2 * math.sin(math.radians(self.angle)), 0.2, 0.8, 0.3)
        self.inner_color.rgba = (0.2, 0.6 + 0.2 * math.cos(math.radians(self.angle)), 0.8, 1)

        # Actualización de posición
        self.update_circle()

    def start_idle_animation(self):
        if not self.idle_animating:
            self.idle_animating = True
            Clock.schedule_interval(self.idle_animation, 0.05)

    def stop_idle_animation(self):
        if self.idle_animating:
            self.idle_animating = False
            Clock.unschedule(self.idle_animation)

    def idle_animation(self, dt):
        offset = math.sin(self.angle) * dp(2)
        self.angle += 0.15  # Movimiento suave en modo idle
        self.circle.pos = (self.center_x - self.circle_radius + offset, self.center_y - self.circle_radius + offset)
        self.outer_ring.pos = (self.center_x - self.circle_radius - dp(30) + offset, self.center_y - self.circle_radius - dp(30) + offset)
        self.inner_ring.pos = (self.center_x - self.circle_radius + offset, self.center_y - self.circle_radius + offset)

    def set_speaking_animation(self):
        self.stop_idle_animation()
        self.start_animation()

    def reset_animation(self):
        self.stop_animation()
        self.start_idle_animation()

    def start_animation(self):
        if not self.animating:
            self.animating = True
            Clock.schedule_interval(self.animate_circle, 0.02)

    def stop_animation(self):
        if self.animating:
            self.animating = False
            Clock.unschedule(self.animate_circle)
            self.reset_circle()

    def reset_circle(self):
        self.circle.size = (self.circle_radius * 2, self.circle_radius * 2)
        self.outer_ring.size = (self.circle_radius * 2 + dp(60), self.circle_radius * 2 + dp(60))
        self.inner_ring.size = (self.circle_radius * 2, self.circle_radius * 2)
        self.update_circle()

class VoiceAssistantScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.circle_animation = CircleAnimation()  # Inicializa la animación del círculo
        self.add_widget(self.circle_animation)  # Agrega la animación al Screen
        self.listening_thread = None  # Inicializa la variable del hilo de escucha

        # Lista de saludos
        self.greetings = [

            "¡Hola! Soy Sify, tu asistente virtual.",
            "Hola, ¿cómo te sientes hoy?",
            "¡Saludos! soy tú asistente Sify. ¿En qué puedo ayudarte?",
            "Hola, soy Sify, tú asistente. ¿Qué necesitas?",
        ]


    
    def on_enter(self, *args):
        # Seleccionar un saludo aleatorio y hablarlo
        greeting = random.choice(self.greetings)
        self.speak(greeting)

    def start_listening(self):
        if self.listening_thread is None or not self.listening_thread.is_alive():
            self.listening_thread = threading.Thread(target=self.listen_for_command)
            self.listening_thread.start()  # Inicia el reconocimiento de voz en un hilo

    def listen_for_command(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Escuchando...")
            audio = recognizer.listen(source)  # Escucha hasta que se detecta un comando

            try:
                command = recognizer.recognize_google(audio, language="es-LA")
                print("Comando recibido:", command.lower())
                self.process_command(command.lower())
            except sr.UnknownValueError:
                print("No entendí el audio.")
            except sr.RequestError:
                print("Error al conectarse al servicio de reconocimiento de voz.")

    def process_command(self, command):
        if "hola" in command:
            self.speak("Hola, ¿cómo estás?")
        elif "adiós" in command:
            self.speak("Hasta luego, que tengas un buen día.")
        elif "qué eres" in command or "quién eres" in command:
            self.speak("Soy Sify, tu asistente virtual, fui desarrollado por Signify One, estoy aquí para ayudarte.")
        elif "qué día es hoy" in command:
            today = datetime.now().strftime("%A, %d de %B del %Y")
            self.speak(f"Hoy es {today}.")
        elif "qué hora es" in command:
            now = datetime.now().strftime("%H:%M")
            self.speak(f"Son las {now}.")
        elif "cuéntame un chiste" in command:
            self.speak("¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.")

        # Respuestas relacionadas con la aplicación Signify One
        elif "cómo inicio sesión" in command:
            self.speak("Para iniciar sesión, haz clic en el botón de inicio en la pantalla principal e ingresa tu usuario y contraseña.")
        elif "cómo puedo recuperar mi contraseña" in command:
            self.speak("Puedes recuperar tu contraseña haciendo clic en '¿Olvidaste tu contraseña?' y siguiendo las instrucciones en pantalla.")
        elif "cómo crear una cuenta" in command:
            self.speak("Para crear una cuenta nueva, selecciona 'Registrarse' en la pantalla de inicio e ingresa la información requerida.")
        elif "cómo accedo a mis configuraciones" in command:
            self.speak("Puedes acceder a tus configuraciones desde el menú principal seleccionando 'Configuraciones'.")
        elif "cómo contacto soporte" in command:
            self.speak("Para contactar soporte, dirígete a la sección de 'Ayuda' en la aplicación o envía un correo a soporte@signifyone.com.")
        elif "cómo ver mi perfil" in command:
            self.speak("Para ver tu perfil, haz clic en tu avatar en la esquina superior derecha de la pantalla.")
        elif "cómo cambio el idioma" in command:
            self.speak("Puedes cambiar el idioma en la sección de 'Configuraciones' bajo 'Preferencias de idioma'.")
        elif "dónde están mis notificaciones" in command:
            self.speak("Puedes ver tus notificaciones en el ícono de la campana en la esquina superior derecha de la pantalla.")
        elif "qué es signify one" in command:
            self.speak("Es una app multiplataforma desarrollada en python, con el objetivo de interpetrar la voz a lengua de señas mexicana.")
        elif "cómo actualizo la app" in command:
            self.speak("Para actualizar la aplicación, visita la tienda de aplicaciones correspondiente y busca actualizaciones disponibles para Signify One.")
        elif "tú interpretas señas" in command:
            self.speak("No exactamente, aunque el equipo se Signify One si agregara esa función en mi.")
        else:
            self.speak("Lo siento, mis respuestas son limitadas. Por favor, pregunta sobre la aplicación de Signify One.")

    def speak(self, text):
        # Calcular la duración del audio antes de reproducirlo
        tts = gTTS(text=text, lang='es')
        tts.save("temp.mp3")

        # Iniciar la animación antes de reproducir el audio
        self.circle_animation.set_speaking_animation()

        # Reproducir el audio en un hilo separado
        threading.Thread(target=self.play_audio, args=("temp.mp3",)).start()

    def play_audio(self, file_path):
        # Reproducir el audio
        os.system(f"afplay {file_path}")  # Cambia "afplay" a "start" o "mpg123" según el sistema operativo

        # Detener la animación después de que el audio termine
        Clock.schedule_once(lambda dt: self.circle_animation.reset_animation(), 0)


class MainApp(MDApp):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())

        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(MainScreen(name='main_screen'))
        sm.add_widget(JuntaPalabrasScreen(name='junta_palabras'))
        sm.add_widget(VoiceAssistantScreen(name='asistente'))
        sm.add_widget(NewPalabraScreen(name='nueva'))
        sm.add_widget(DeteccionSeñasScreen(name='deteccion_señas'))
        sm.add_widget(DiccionarioScreen(name='diccionario'))
        sm.add_widget(ConfiguracionScreen(name='configuracion'))

        return sm

if __name__ == '__main__':
    Builder.load_string(KV)
    MainApp().run()