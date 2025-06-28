import kivy
from kivy.lang import Builder
from kivy.graphics import Color, Ellipse, Rectangle
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
import speech_recognition as sr
from kivy.metrics import dp
import threading
from gtts import gTTS
import os
import math
from playsound import playsound  # Usamos playsound para reproducir audio

kivy.require('2.3.0')

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: dp(20)

    canvas.before:
        Color:
            rgba: 0.3, 0.1, 0.7, 0.8  # Fondo transparente
        Rectangle:    
            pos: self.pos
            size: self.size

    # Contenedor para la animación de un solo círculo
    CircleAnimation:
        id: circle_animation
        size_hint: None, None  # No usar size_hint para width y height
        height: dp(400)  # Ajustar la altura del círculo
        width: dp(400)  # Ajustar el ancho del círculo
        pos_hint: {'center_x': 0.5, 'center_y': .0}  # Centrar el círculo en X y Y
  

    # Contenedor para el texto y el botón de micrófono
    BoxLayout:
        orientation: 'vertical'
        padding: [10, 20]
        spacing: dp(10)

        MDLabel:
            text: "¿Cómo puedo ayudarte?"
            halign: "center"
            font_style: "H6"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1  # Blanco
            size_hint_y: None
            height: dp(40)

        MDIconButton:
            icon: 'microphone'
            size_hint: None, None
            size: dp(120), dp(120)
            md_bg_color: 0.8, 0.6, 0.2, 0.6  
            on_release: app.start_listening()
            theme_icon_color: "Custom"
            icon_color: 1, 1, 1, 1   # Blanco
            pos_hint: {'center_x': 0.5}  # Centrar el botón en el eje X

    # Espaciador para empujar el botón de micrófono hacia abajo
    BoxLayout:
        size_hint_y: None
        height: dp(30)  # Ajusta la altura según sea necesario
'''

class CircleAnimation(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.circle_radius = dp(150)
        self.angle = 0
        self.animating = False
        self.idle_animating = False

        with self.canvas:
            self.color = Color(0.8, 0.6, 0.2, 0.6)
            self.circles = []
            for i in range(10):
                alpha = 1 - (i * 0.1)
                color = Color(0.8, 0.6, 0.2, alpha)
                self.circles.append((color, Ellipse(size=(self.circle_radius * 2, self.circle_radius * 2), pos=self.center)))

        self.bind(pos=self.update_circle, size=self.update_circle)
        self.start_idle_animation()

    def update_circle(self, *args):
        for color, circle in self.circles:
            circle.pos = (self.center_x - self.circle_radius, self.center_y - self.circle_radius)

    def animate_circle(self, dt):
        if not self.animating:
            return
        self.angle = (self.angle + 5) % 360
        factor = 1 + 0.1 * math.sin(math.radians(self.angle))
        for i, (color, circle) in enumerate(self.circles):
            scale = factor * (1 - (i * 0.05))
            circle.size = (self.circle_radius * 2 * scale, self.circle_radius * 2 * scale)

    def start_idle_animation(self):
        if not self.idle_animating:
            self.idle_animating = True
            Clock.schedule_interval(self.idle_animation, 0.05)

    def stop_idle_animation(self):
        if self.idle_animating:
            self.idle_animating = False
            Clock.unschedule(self.idle_animation)

    def idle_animation(self, dt):
        offset = math.sin(self.angle) * dp(1.9)
        self.angle += 0.2
        for i, (color, circle) in enumerate(self.circles):
            circle.pos = (self.center_x - self.circle_radius + offset, self.center_y - self.circle_radius + offset)

    def set_speaking_animation(self):
        self.stop_idle_animation()
        self.start_animation()

    def reset_animation(self):
        self.stop_animation()
        self.start_idle_animation()

    def start_animation(self):
        if not self.animating:
            self.animating = True
            Clock.schedule_interval(self.animate_circle, 0.01)

    def stop_animation(self):
        if self.animating:
            self.animating = False
            Clock.unschedule(self.animate_circle)
            self.reset_circles()

    def reset_circles(self):
        for i, (color, circle) in enumerate(self.circles):
            circle.size = (self.circle_radius * 2, self.circle_radius * 2)

class VoiceAssistantApp(MDApp):
    def build(self):
        self.title = "Asistente de Voz"
        return Builder.load_string(KV)

    def speak(self, text):
        circle_animation = self.root.ids.circle_animation
        circle_animation.set_speaking_animation()

        threading.Thread(target=self.play_audio, args=(text,)).start()  # Pasamos solo el texto

    def play_audio(self, text):
        tts = gTTS(text=text, lang='es')
        temp_file = "temp.mp3"
        tts.save(temp_file)

        playsound(temp_file)  # Reproducir el archivo de audio

        # Eliminamos el archivo temporal una vez que se ha reproducido
        Clock.schedule_once(lambda dt: os.remove(temp_file), 5)

        # Restablecer la animación una vez que se termina el audio
        Clock.schedule_once(lambda dt: self.root.ids.circle_animation.reset_animation(), 0)

    def start_listening(self):
        threading.Thread(target=self.listen_for_command).start()

    def listen_for_command(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Escuchando...")
            audio = recognizer.listen(source)

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
            self.speak("Hasta luego, que tengas un buen día")
        elif "qué eres" in command or "quién eres" in command:
            self.speak("Soy Sify, tu asistente virtual.")
        elif "qué día es hoy" in command:
            from datetime import datetime
            today = datetime.now().strftime("%A, %d de %B del %Y")
            self.speak(f"Hoy es {today}.")
        elif "qué hora es" in command:
            from datetime import datetime
            now = datetime.now().strftime("%H:%M")
            self.speak(f"Son las {now}.")
        elif "cuéntame un chiste" in command:
            self.speak("¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.")
        else:
            self.speak("Lo siento, no entendí lo que dijiste.")

if __name__ == "__main__":
    VoiceAssistantApp().run()