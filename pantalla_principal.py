from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty
from kivy.metrics import dp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

Builder.load_string("""
#:import dp kivy.metrics.dp

<HomeScreen>:
    name: 'home'
    FloatLayout:
        canvas.before:
            Color:
                rgba: 0.8, 0.6, 0.2, 0.9  # Dark purple background
            Rectangle:
                pos: self.pos
                size: self.size
            Color:
                rgba: 0.3, 0.1, 0.7, 1  # Slightly lighter purple shapes
            Ellipse:
                pos: -dp(80), self.height - dp(220)
                size: dp(500), dp(400)
            Ellipse:
                pos: self.width - dp(200), -dp(200)
                size: dp(600), dp(400)

        MDBoxLayout:
            orientation: 'vertical'
            padding: dp(20)
            spacing: dp(20)
            pos_hint: {"center_x": .5, "center_y": .5}
            size_hint: 0.9, 0.9
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 0.3  # Slightly transparent background for the box
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [dp(50)]

            MDBoxLayout:
                size_hint_y: None
                height: self.minimum_height
                padding: dp(10)

                MDBoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    spacing: dp(20)
                    MDLabel:
                        text: "Bienvenido a Signify One"
                        font_style: "H4"
                        font_name: "assets/Poppins/Poppins-Italic.ttf"
                        color: 1, 1, 1, 1
                        halign: "center"
                        size_hint_y: None
                        height: self.texture_size[1]
                        font_size: dp(24) if self.width < dp(800) else dp(32)
                    MDLabel:
                        text: "Elige una opción para comenzar"
                        font_style: "Subtitle1"
                        font_name: "assets/Poppins/Poppins-Bold.ttf"
                        color: 1, 1, 1, 1
                        halign: "center"
                        size_hint_y: None
                        height: self.texture_size[1]
                        font_size: dp(18) if self.width < dp(800) else dp(24)

            ScrollView:
                MDGridLayout:
                    id: grid_layout  # Cambiar a un id para acceder desde el Python
                    cols: root.cols 
                    adaptive_height: True
                    padding: dp(3)
                    spacing: dp(9)

                    MDCard:
                        size_hint: .45, None
                        height: dp(230)
                        orientation: 'vertical'
                        ripple_behavior: True
                        on_release: 
                            root.manager.transition.direction = "left"
                            app.root.current = 'main_screen'
                        padding: dp(10)
                        md_bg_color: 0.9, 0.1, 0.2, 1  # Rojo
                        MDBoxLayout:
                            orientation: 'vertical'
                            spacing: dp(10)
                            Image:
                                source: 'assets/images/reconocimiento.png'
                                size_hint_y: None
                                height: dp(120)
                                allow_stretch: False
                            MDLabel:
                                text: "Utilizar Voz"
                                halign: 'center'
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                font_name: "assets/Poppins/Poppins-Bold.ttf"
                                font_style: "Subtitle1"
                                font_size: dp(16) if self.width < dp(800) else dp(20)

                    MDCard:
                        size_hint: .45, None
                        height: dp(230)
                        orientation: 'vertical'
                        ripple_behavior: True
                        on_release: 
                            root.manager.transition.direction = "left"
                            app.root.current = 'junta_palabras'
                        padding: dp(10)
                        md_bg_color: 0.4, 0.5, 0.9, 1  # Azul
                        MDBoxLayout:
                            orientation: 'vertical'
                            spacing: dp(10)
                            Image:
                                source: 'assets/images/drag.png'
                                size_hint_y: None
                                height: dp(120)
                                allow_stretch: False
                            MDLabel:
                                text: "Une Palabras"
                                halign: 'center'
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                font_name: "assets/Poppins/Poppins-Bold.ttf"
                                font_style: "Subtitle1"
                                font_size: dp(16) if self.width < dp(800) else dp(20)

                    # Nueva tarjeta para "Agregar Palabras"
                    MDCard:
                        size_hint: .45, None
                        height: dp(230)
                        orientation: 'vertical'
                        ripple_behavior: True
                        on_release: 
                            root.manager.transition.direction = "left"
                            app.root.current = 'nueva'
                        padding: dp(10)
                        md_bg_color: 0.1, 0.7, 0.1, 0.9  # Light Green
                        MDBoxLayout:
                            orientation: 'vertical'
                            spacing: dp(10)
                            Image:
                                source: 'assets/images/palabra.png'
                                size_hint_y: None
                                height: dp(120)
                                allow_stretch: False
                            MDLabel:
                                text: "Agregar Palabras"
                                halign: 'center'
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                font_name: "assets/Poppins/Poppins-Bold.ttf"
                                font_style: "Subtitle1"
                                font_size: dp(16) if self.width < dp(800) else dp(20)

                    MDCard:
                        size_hint: .45, None
                        height: dp(230)
                        orientation: 'vertical'
                        ripple_behavior: True
                        on_release: 
                            root.manager.transition.direction = "left"
                            app.root.current = 'diccionario'
                        padding: dp(10)
                        md_bg_color: 0.8, 0.9, 0.2, 0.9  # Light Purple
                        MDBoxLayout:
                            orientation: 'vertical'
                            spacing: dp(10)
                            Image:
                                source: 'assets/images/diccionario.png'
                                size_hint_y: None
                                height: dp(120)
                                allow_stretch: False
                            MDLabel:
                                text: "Ver Diccionario"
                                halign: 'center'
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                font_name: "assets/Poppins/Poppins-Medium.ttf"
                                font_style: "Subtitle1"
                                font_size: dp(16) if self.width < dp(800) else dp(20)

                    MDCard:
                        size_hint: .45, None
                        height: dp(230)
                        orientation: 'vertical'
                        ripple_behavior: True
                        on_release: 
                            root.manager.transition.direction = "left"
                            app.root.current = 'configuracion'
                        padding: dp(10)
                        md_bg_color: 0.9, 0.7, 0.5, 0.9  # Light Orange
                        MDBoxLayout:
                            orientation: 'vertical'
                            spacing: dp(10)
                            Image:
                                source: 'assets/images/configuracion.png'
                                size_hint_y: None
                                height: dp(120)
                                allow_stretch: False
                            MDLabel:
                                text: "Configuración"
                                halign: 'center'
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                font_name: "assets/Poppins/Poppins-Medium.ttf"
                                font_style: "Subtitle1"
                                font_size: dp(16) if self.width < dp(800) else dp(20)

                    MDCard:
                        size_hint: .45, None
                        height: dp(230)
                        orientation: 'vertical'
                        ripple_behavior: True
                        on_release: 
                            root.manager.transition.direction = "left"
                            app.root.current = 'deteccion_señas'
                        padding: dp(10)
                        md_bg_color: 0.6, 0.3, 0.8, 1  # Morado vibrante
                        MDBoxLayout:
                            orientation: 'vertical'
                            spacing: dp(10)
                            Image:
                                source: 'assets/images/señas.png'
                                size_hint_y: None
                                height: dp(120)
                                allow_stretch: False
                            MDLabel:
                                text: "Señas a Voz"
                                halign: 'center'
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                font_name: "assets/Poppins/Poppins-Bold.ttf"
                                font_style: "Subtitle1"
                                font_size: dp(16) if self.width < dp(800) else dp(20)

        # Card transparente en la esquina superior derecha
        MDCard:
            size_hint: None, None
            size: dp(60), dp(60)  # Tamaño del card
            pos_hint: {"right": 1, "top": 1}  # Colocarlo en la esquina superior derecha
            md_bg_color: 0, 0, 0, 0  # Fondo transparente
            on_release: 
                root.manager.transition.direction = "left"
                app.root.current = 'asistente' 
 
            Image:
                source: 'assets/bot.png'  # Ruta de tu imagen
                allow_stretch: True
                size_hint: None, None
                size: dp(50), dp(60)  # Tamaño de la imagen
                pos_hint: {"center_x": 0.5, "center_y": 0.5}  # Centrar la imagen en el card
""")

class HomeScreen(MDScreen):
    cols = NumericProperty(2)  # Default number of columns
    dialog = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(size=self.update_cols)

    def update_cols(self, *args):
        if self.width > dp(800):
            self.cols = 3
        else:
            self.cols = 2

    def go_to_main_screen(self):
        self.manager.current = 'main_screen'
    
    def go_drag_and_screen(self):
        self.manager.current = 'junta_palabras'


    def show_working_modal(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Funcionalidad en Desarrollo",
                type="custom",
                content_cls=Image(source='assets/images/arreglando.png', size_hint_y=None, height=dp(300)),
                buttons=[
                    MDFlatButton(
                        text="CERRAR",
                        on_release=self.close_dialog
                    )
                ]
            )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

    def close_dialog(self, *args):
        self.dialog.dismiss()
