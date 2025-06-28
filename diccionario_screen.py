from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivymd.uix.textfield import MDTextField
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from diccionario import diccionario

KV = '''
<DiccionarioScreen>:
    name: 'diccionario'
    md_bg_color: 0.1, 0.1, 0.1, 1

    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(10)
        spacing: dp(10)

        # Header
        MDBoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(50)
            md_bg_color: 0.2, 0.2, 0.2, 1
            padding: dp(10)

            MDIconButton:
                icon: 'arrow-left'
                on_release: app.root.current = 'home'
                theme_icon_color: "Custom"
                icon_color: 1, 1, 1, 1

            MDLabel:
                text: 'Diccionario de Señas'
                halign: 'center'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                font_size: '18sp'

        # Barra de búsqueda
        MDTextField:
            id: search_field
            hint_text: "Buscar palabra..."
            mode: "rectangle"
            on_text_validate: root.buscar_palabra(self.text)
            font_size: '16sp'
            background_color: 1, 1, 1, 1
            foreground_color: 0, 0, 0, 1
            line_color_focus: 1, 1, 1, 0
            line_color_normal: 1, 1, 1, 0
            size_hint_y: None
            height: dp(50)

        # Filtros de categoría
        MDBoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(40)
            spacing: dp(5)

            MDRaisedButton:
                text: 'Todas'
                on_release: root.filtrar_categoria('Todas')
                md_bg_color: 0.3, 0.3, 0.3, 1
                size_hint_x: 0.2

            MDRaisedButton:
                text: 'Sujetos'
                on_release: root.filtrar_categoria('S')
                md_bg_color: 0.2, 0.6, 0.2, 1
                size_hint_x: 0.2

            MDRaisedButton:
                text: 'Objetos'
                on_release: root.filtrar_categoria('O')
                md_bg_color: 0.6, 0.2, 0.2, 1
                size_hint_x: 0.2

            MDRaisedButton:
                text: 'Verbos'
                on_release: root.filtrar_categoria('V')
                md_bg_color: 0.2, 0.2, 0.6, 1
                size_hint_x: 0.2

            MDRaisedButton:
                text: 'Tiempo'
                on_release: root.filtrar_categoria('T')
                md_bg_color: 0.6, 0.6, 0.2, 1
                size_hint_x: 0.2

        # Lista de palabras
        ScrollView:
            MDGridLayout:
                id: words_grid
                cols: 2
                adaptive_height: True
                spacing: dp(10)
                padding: dp(10)
'''

Builder.load_string(KV)

class DiccionarioScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_filter = 'Todas'
        self.all_words = list(diccionario.keys())
        self.filtered_words = self.all_words.copy()

    def on_enter(self):
        self.cargar_palabras()

    def buscar_palabra(self, texto):
        if texto:
            self.filtered_words = [palabra for palabra in self.all_words 
                                 if texto.lower() in palabra.lower()]
        else:
            self.filtered_words = self.all_words
        self.cargar_palabras()

    def filtrar_categoria(self, categoria):
        self.current_filter = categoria
        if categoria == 'Todas':
            self.filtered_words = self.all_words
        else:
            self.filtered_words = [palabra for palabra in self.all_words 
                                 if diccionario.get(palabra) == categoria]
        self.cargar_palabras()

    def cargar_palabras(self):
        grid = self.ids.words_grid
        grid.clear_widgets()

        for palabra in self.filtered_words:
            categoria = diccionario.get(palabra, '')
            color_categoria = self.get_color_categoria(categoria)
            
            card = MDCard(
                orientation='vertical',
                size_hint=(None, None),
                size=(dp(150), dp(100)),
                md_bg_color=color_categoria,
                ripple_behavior=True,
                elevation=2
            )

            # Nombre de la palabra
            label_palabra = MDLabel(
                text=palabra,
                halign='center',
                theme_text_color='Custom',
                text_color=[1, 1, 1, 1],
                font_size='14sp',
                size_hint_y=0.7
            )

            # Categoría
            label_categoria = MDLabel(
                text=self.get_nombre_categoria(categoria),
                halign='center',
                theme_text_color='Custom',
                text_color=[0.9, 0.9, 0.9, 1],
                font_size='12sp',
                size_hint_y=0.3
            )

            card.add_widget(label_palabra)
            card.add_widget(label_categoria)
            grid.add_widget(card)

    def get_color_categoria(self, categoria):
        colores = {
            'S': [0.2, 0.6, 0.2, 1],  # Verde para sujetos
            'O': [0.6, 0.2, 0.2, 1],  # Rojo para objetos
            'V': [0.2, 0.2, 0.6, 1],  # Azul para verbos
            'T': [0.6, 0.6, 0.2, 1],  # Amarillo para tiempo
            'L': [0.6, 0.2, 0.6, 1],  # Morado para lugar
        }
        return colores.get(categoria, [0.3, 0.3, 0.3, 1])

    def get_nombre_categoria(self, categoria):
        nombres = {
            'S': 'Sujeto',
            'O': 'Objeto',
            'V': 'Verbo',
            'T': 'Tiempo',
            'L': 'Lugar',
        }
        return nombres.get(categoria, 'Desconocida') 