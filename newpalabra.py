from kivy.uix.video import Video
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp
from kivy.lang import Builder 
from kivy.core.window import Window

# Configura el tamaño de la ventana
Window.size = (370, 670)

KV = """
MDFloatLayout:
    name: 'nueva'   
    MDCard:
        size_hint: .9, .8
        pos_hint: {'center_x': .5, 'center_y': .5}
        Carousel:
            id: slide
            MDFloatLayout:
                MDTextField: 
                    hint_text: "Nueva Palabra"
                    size_hint_x: .8
                    pos_hint: {'center_x': .5, 'center_y': .48}
                MDTextField:
                    hint_text: 'Tipo de palabra'
                    size_hint_x: .8
                    pos_hint: {'center_x': .5, 'center_y': .36}
                MDRaisedButton:
                    text: 'Siguiente'
                    size_hint_x: .8
                    pos_hint: {'center_x': .5, 'center_y': .2}  
                    on_release: app.next() 
                    
            MDFloatLayout:
                MDTextField: 
                    hint_text: "Nombre del video"
                    size_hint_x: .8
                    pos_hint: {'center_x': .5, 'center_y': .48}
                MDTextField:
                    hint_text: 'Sube tu video aquí'
                    size_hint_x: .8
                    pos_hint: {'center_x': .5, 'center_y': .36}
                MDRaisedButton:
                    text: 'Previo'
                    size_hint_x: .8
                    pos_hint: {'center_x': .5, 'center_y': .25}
                    on_release: app.previous()
                MDRaisedButton:
                    text: 'Guardar'
                    size_hint_x: .8
                    pos_hint: {'center_x': .5, 'center_y': .1} 
                
                    
                MDIconButton:
                    icon: "arrow-left"
                    pos_hint: {"center_y": .95}
                    user_font_size: "30sp"
                    theme_text_color: "Custom"
                    text_color: rgba(26, 24, 58, 255)
                    on_release: 
                        root.manager.transition.direction = "right"
                        app.root.current = 'home'  # Regresar a la pantalla principal
                        
    MDLabel:
        text: "Agrega una nueva palabra"
        bold: True
        pos_hint: {'center_x': .62, 'center_y': .8}  
        font_style: "H5"
    MDLabel:
        id: palabra
        text: "Palabra"
        pos_hint: {'center_x': .608,'center_y': .7}
        font_style: "H6"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color

    MDIconButton:
        id: Palabra
        icon: "numeric-1-circle"
        pos_hint: {'center_x': .18,'center_y': .65}
        user_font_size: "35sp"
        theme_text_color: "Custom"
        icon_color: app.theme_cls.primary_color
    MDProgressBar:
        id: bar
        size_hint_x: .5
        size_hint_y: .006
        pos_hint: {'center_x': .49, 'center_y': .65}
    MDLabel:
        id: video
        text: "Video"
        pos_hint: {'center_x': 1.25, 'center_y': .7}
        font_style: "H6"
        theme_text_color: "Custom"
    MDIconButton:
        id: Video
        icon: "numeric-2-circle"
        pos_hint: {'center_x': .81,'center_y': .65}
        user_font_size: "35sp"
        theme_text_color: "Custom"
"""

class palabra(MDApp):

    def build(self):
        kv = Builder.load_string(KV)
        return kv

    def next(self):
        self.root.ids.slide.load_next(mode="next")
        self.root.ids.bar.value = 100
        self.root.ids.Video.text_color = self.theme_cls.primary_color
        self.root.ids.video.text_color = self.theme_cls.primary_color
        self.root.ids.Palabra.icon = "check-decagram"
    


    def previous(self):
        self.root.ids.slide.load_previous()
        self.root.ids.Video.text_color = 0, 0, 0, 1
        self.root.ids.video.text_color = 0, 0, 0, 1
        self.root.ids.bar.value = 0.0001   
        self.root.ids.Palabra.icon = "numeric-1-circle"