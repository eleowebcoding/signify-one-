from kivy.uix.accordion import FloatLayout
import os
import cv2
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.graphics.texture import Texture
from kivy.lang import Builder
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.metrics import dp
from kivymd.uix.textfield import MDTextField  # Importar MDTextField para búsqueda
from diccionario import diccionario

# Ruta base para archivos de video
base_path = "videos/"

kv_string = '''
#:import dp kivy.metrics.dp
<JuntaPalabrasScreen>:
    name: 'junta_palabras'
    md_bg_color: 0.1, 0.1, 0.1, 1

    FloatLayout:
        canvas.before:
            Color:
                rgba: 0.4, 0.5, 0.9, 1
            Rectangle:
                pos: self.pos
                size: self.size
            Color:
                rgba: 0.6, 0.7, 0.8, 1
            Ellipse:
                pos: -dp(120), self.height - dp(200)
                size: dp(300), dp(300)
            Ellipse:
                pos: self.width - dp(120), -dp(10)
                size: dp(300), dp(300)

        MDBoxLayout:
            orientation: 'vertical'
            padding: dp(8)
            spacing: dp(5)
            pos_hint: {"center_x": .5, "center_y": .5}
            size_hint: 0.92, 0.92
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 0.2  # Fondo ligeramente transparente
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [dp(12)]

            MDBoxLayout:
                orientation: 'horizontal'
                size_hint_y: None
                height: dp(55)
                padding: dp(4)
                spacing: dp(-20)
                canvas.before:
                    Color:
                        rgba: 0.6, 0.7, 0.8, 0.7
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [dp(20)]

                MDIconButton:
                    icon: 'home'  # Ícono de flecha
                    on_release: 
                        root.manager.transition.direction = "right"
                        app.root.current = 'home'  # Regresar a la pantalla principal
                    theme_icon_color: "Custom"
                    icon_color: [1, 1, 1, 1]  # Blanco

                MDLabel:
                    text: 'Une Palabras para Formar Oraciones'
                    halign: 'center'
                    theme_text_color: 'Custom'
                    text_color: [1, 1, 1, 1]
                    font_size: '19sp'
            
            # Nueva barra de búsqueda movida hacia abajo
            MDBoxLayout:
                orientation: 'horizontal'
                size_hint_y: None
                height: dp(50)
                padding: [dp(20), dp(0), dp(20), dp(0)]
                spacing: dp(5)
                md_bg_color: 0.95, 0.95, 0.95, 1  # Fondo claro
                pos_hint: {"center_x": .5, "y": 0.45}  # Mover 10 px hacia abajo

                MDTextField:
                    id: search_field
                    hint_text: "Buscar palabra..."
                    size_hint_x: 0.85
                    mode: "rectangle"  # Cambiar a "rectangle" para no tener bordes
                    on_text_validate: root.buscar_palabra(self.text)
                    font_size: '16sp'
                    background_color: [1, 1, 1, 1]  # Fondo blanco para el campo de texto
                    foreground_color: [0, 0, 0, 1]  # Texto negro
                    line_color_focus: [1, 1, 1, 0]  # Sin línea al enfocar
                    line_color_normal: [1, 1, 1, 0]  # Sin línea normal
                    # Para eliminar el efecto al presionar
                    ripple_behavior: False  # Desactivar efecto de onda
                    # Para evitar el cambio de color en el enfoque
                    background_normal: ''  # Sin textura
                    background_active: ''  # Sin textura al activarse
                
            # ScrollView para las palabras disponibles
            ScrollView:
                size_hint_y: None
                height: dp(120)
                BoxLayout:
                    id: palabras_disponibles
                    orientation: 'horizontal'
                    spacing: dp(10)
                    size_hint_x: None
                    width: self.minimum_width

            # Contenedor para la oración y botones
            BoxLayout:
                orientation: 'horizontal'
                size_hint_y: None
                height: dp(54)
                padding: dp(9)
                spacing: dp(12)

                MDLabel:
                    id: oracion_label
                    text: 'Oración: '
                    theme_text_color: 'Custom'
                    text_color: [1, 1, 1, 1]
                    font_size: '16sp'

                MDIconButton:
                    icon: "play"
                    on_release: root.procesar_oracion()
                    theme_icon_color: "Custom"
                    icon_color: [1, 1, 1, 1]

                MDIconButton:
                    icon: "delete"
                    on_release: root.limpiar_oracion()
                    theme_icon_color: "Custom"
                    icon_color: [1, 1, 1, 1]

            BoxLayout:
                size_hint_y: 1
                Image:
                    id: video_player
                    allow_stretch: True
                    keep_ratio: True
                    size_hint_y: 1
                    size_hint_x: 1
'''

Builder.load_string(kv_string)  # Cargar la cadena kv


class JuntaPalabrasScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.palabras_seleccionadas = []
        self.palabras_en_espera = []
        self.cap = None
        Clock.schedule_once(self.init_ui, 0)

    def init_ui(self, dt):
        self.cargar_palabras_disponibles(diccionario.keys())

    def cargar_palabras_disponibles(self, palabras):
        """Carga las tarjetas de palabras disponibles en el contenedor."""
        self.ids.palabras_disponibles.clear_widgets()
        for palabra in palabras:
            card = MDCard(
                orientation='vertical',
                size_hint=(None, None),
                size=(dp(100), dp(50)),
                md_bg_color=(0, 0, 0, 0),  # Fondo transparente
                ripple_behavior=True,  # Efecto de onda al hacer clic
                elevation=0  # Sin sombra
            )
            label = MDLabel(
                text=palabra,
                halign='center',
                theme_text_color='Custom',
                text_color=[1, 1, 1, 1]  # Color del texto blanco
            )
            card.add_widget(label)
            card.bind(on_release=lambda x=card: self.add_palabra(x.children[0].text))
            self.ids.palabras_disponibles.add_widget(card)

    def buscar_palabra(self, palabra_buscada):
        """Busca una palabra en el diccionario y actualiza la lista de palabras disponibles."""
        palabras_filtradas = [palabra for palabra in diccionario if palabra_buscada.lower() in palabra.lower()]
        self.cargar_palabras_disponibles(palabras_filtradas)

    def add_palabra(self, palabra):
        print(f"Añadiendo palabra: {palabra}")
        if palabra in diccionario:
            self.palabras_seleccionadas.append(palabra)
            self.update_oracion_label()

    def update_oracion_label(self):
        oracion = " ".join(self.palabras_seleccionadas)
        self.ids.oracion_label.text = f'Oración: {oracion}'

    def procesar_oracion(self):
        oracion = " ".join(self.palabras_seleccionadas)
        if oracion:
            print(f"Procesando oración: {oracion}")
            oracion_reordenada = self.reordenar_oracion(oracion)
            self.ids.oracion_label.text = f'Oración: {oracion_reordenada}'
            self.palabras_en_espera = oracion_reordenada.split()  # Almacena las palabras a reproducir
            self.iniciar_reproduccion()  # Inicia la reproducción inmediatamente

    def iniciar_reproduccion(self):
        if self.palabras_en_espera:
            palabra = self.palabras_en_espera.pop(0)
            self.mostrar_video(palabra)

    def mostrar_video(self, palabra):
        video_path = self.obtener_ruta_video(palabra)
        print(f"Mostrando video para: {palabra}, ruta: {video_path}")
        if not video_path or not os.path.exists(video_path):
            print(f"Video no encontrado para: {palabra}")
            return

        if self.cap is not None:
            self.cap.release()

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
                # Si no hay más palabras, quita el video
                self.ids.video_player.texture = None  # Limpiar el área del video

    def play_next_video(self, dt):
        if self.palabras_en_espera:
            palabra = self.palabras_en_espera.pop(0)
            self.mostrar_video(palabra)

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
        
        # Reordenar según la gramática: T, L, S, O, V
        oracion_reordenada = categorias['T'] + categorias['L'] + categorias['S'] + categorias['O'] + categorias['V']
        
        return " ".join(oracion_reordenada)

    def limpiar_oracion(self):
        print("Limpiando oración.")
        self.palabras_seleccionadas.clear()
        self.ids.oracion_label.text = 'Oración: '  # Restablecer la etiqueta
        self.palabras_en_espera.clear()  # Limpiar las palabras en espera
        self.ids.video_player.texture = None  # Limpiar el área del video
