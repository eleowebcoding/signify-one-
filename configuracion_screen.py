from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.slider import MDSlider
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.metrics import dp

KV = '''
<ConfiguracionScreen>:
    name: 'configuracion'
    md_bg_color: 0.1, 0.1, 0.1, 1

    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)

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
                text: 'Configuración'
                halign: 'center'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                font_size: '18sp'

        # Contenido principal
        ScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                adaptive_height: True
                spacing: dp(20)
                padding: dp(10)

                # Sección de Audio
                MDCard:
                    orientation: 'vertical'
                    padding: dp(20)
                    spacing: dp(15)
                    md_bg_color: 0.2, 0.2, 0.2, 1

                    MDLabel:
                        text: 'Configuración de Audio'
                        halign: 'center'
                        theme_text_color: 'Custom'
                        text_color: 1, 1, 1, 1
                        font_size: '16sp'
                        bold: True

                    MDBoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        height: dp(40)

                        MDLabel:
                            text: 'Volumen:'
                            theme_text_color: 'Custom'
                            text_color: 1, 1, 1, 1
                            size_hint_x: 0.3

                        MDSlider:
                            id: volume_slider
                            min: 0
                            max: 100
                            value: 50
                            size_hint_x: 0.7

                    MDBoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        height: dp(40)

                        MDLabel:
                            text: 'Velocidad de Reproducción:'
                            theme_text_color: 'Custom'
                            text_color: 1, 1, 1, 1
                            size_hint_x: 0.6

                        MDSlider:
                            id: speed_slider
                            min: 0.5
                            max: 2.0
                            value: 1.0
                            size_hint_x: 0.4

                # Sección de Micrófono
                MDCard:
                    orientation: 'vertical'
                    padding: dp(20)
                    spacing: dp(15)
                    md_bg_color: 0.2, 0.2, 0.2, 1

                    MDLabel:
                        text: 'Configuración de Micrófono'
                        halign: 'center'
                        theme_text_color: 'Custom'
                        text_color: 1, 1, 1, 1
                        font_size: '16sp'
                        bold: True

                    MDBoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        height: dp(40)

                        MDLabel:
                            text: 'Sensibilidad:'
                            theme_text_color: 'Custom'
                            text_color: 1, 1, 1, 1
                            size_hint_x: 0.3

                        MDSlider:
                            id: mic_sensitivity
                            min: 0.1
                            max: 1.0
                            value: 0.5
                            size_hint_x: 0.7

                    MDBoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        height: dp(40)

                        MDLabel:
                            text: 'Tiempo de Escucha (segundos):'
                            theme_text_color: 'Custom'
                            text_color: 1, 1, 1, 1
                            size_hint_x: 0.6

                        MDSlider:
                            id: listen_time
                            min: 1
                            max: 10
                            value: 5
                            size_hint_x: 0.4

                # Sección de Cámara
                MDCard:
                    orientation: 'vertical'
                    padding: dp(20)
                    spacing: dp(15)
                    md_bg_color: 0.2, 0.2, 0.2, 1

                    MDLabel:
                        text: 'Configuración de Cámara'
                        halign: 'center'
                        theme_text_color: 'Custom'
                        text_color: 1, 1, 1, 1
                        font_size: '16sp'
                        bold: True

                    MDBoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        height: dp(40)

                        MDLabel:
                            text: 'Calidad de Video:'
                            theme_text_color: 'Custom'
                            text_color: 1, 1, 1, 1
                            size_hint_x: 0.4

                        MDSlider:
                            id: video_quality
                            min: 480
                            max: 1080
                            value: 720
                            size_hint_x: 0.6

                    MDBoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        height: dp(40)

                        MDLabel:
                            text: 'Reproducción Automática:'
                            theme_text_color: 'Custom'
                            text_color: 1, 1, 1, 1
                            size_hint_x: 0.6

                        MDRaisedButton:
                            id: auto_play
                            text: 'Desactivar'
                            on_release: root.toggle_auto_play()
                            md_bg_color: 0.6, 0.2, 0.2, 1
                            size_hint_x: 0.4

                # Sección de Interfaz
                MDCard:
                    orientation: 'vertical'
                    padding: dp(20)
                    spacing: dp(15)
                    md_bg_color: 0.2, 0.2, 0.2, 1

                    MDLabel:
                        text: 'Configuración de Interfaz'
                        halign: 'center'
                        theme_text_color: 'Custom'
                        text_color: 1, 1, 1, 1
                        font_size: '16sp'
                        bold: True

                    MDBoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        height: dp(40)

                        MDLabel:
                            text: 'Tema Oscuro:'
                            theme_text_color: 'Custom'
                            text_color: 1, 1, 1, 1
                            size_hint_x: 0.6

                        MDRaisedButton:
                            id: dark_theme
                            text: 'Desactivar'
                            on_release: root.toggle_dark_theme()
                            md_bg_color: 0.2, 0.6, 0.2, 1
                            size_hint_x: 0.4

                    MDBoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        height: dp(40)

                        MDLabel:
                            text: 'Tamaño de Fuente:'
                            theme_text_color: 'Custom'
                            text_color: 1, 1, 1, 1
                            size_hint_x: 0.4

                        MDSlider:
                            id: font_size
                            min: 12
                            max: 24
                            value: 16
                            size_hint_x: 0.6

                # Botones de acción
                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: dp(10)
                    size_hint_y: None
                    height: dp(120)

                    MDRaisedButton:
                        text: 'Términos y Condiciones'
                        on_release: root.mostrar_terminos()
                        md_bg_color: 0.3, 0.3, 0.6, 1
                        size_hint_y: None
                        height: dp(50)

                    MDRaisedButton:
                        text: 'Política de Privacidad'
                        on_release: root.mostrar_privacidad()
                        md_bg_color: 0.6, 0.3, 0.3, 1
                        size_hint_y: None
                        height: dp(50)

                    MDRaisedButton:
                        text: 'Restablecer Configuración'
                        on_release: root.restablecer_configuracion()
                        md_bg_color: 0.3, 0.6, 0.3, 1
                        size_hint_y: None
                        height: dp(50)
'''

Builder.load_string(KV)

class ConfiguracionScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.terminos_dialog = None
        self.privacidad_dialog = None
        self.auto_play_active = False
        self.dark_theme_active = True

    def mostrar_terminos(self):
        if not self.terminos_dialog:
            self.terminos_dialog = MDDialog(
                title="Términos y Condiciones",
                text="""TÉRMINOS Y CONDICIONES DE USO

1. ACEPTACIÓN DE TÉRMINOS
Al usar Signify One, aceptas estos términos y condiciones de uso.

2. DESCRIPCIÓN DEL SERVICIO
Signify One es una aplicación educativa para el aprendizaje de lengua de señas mexicana.

3. USO ACEPTABLE
- Usar la aplicación solo para fines educativos
- Respetar los derechos de autor
- No usar la aplicación para fines comerciales sin autorización

4. PRIVACIDAD
- La aplicación no recopila datos personales
- El reconocimiento de voz se procesa localmente
- No se almacenan conversaciones de voz

5. LIMITACIONES
- La aplicación requiere conexión a internet para algunas funciones
- El reconocimiento de voz puede no ser 100% preciso
- Se requiere micrófono y cámara para funcionalidades completas

6. RESPONSABILIDAD
- El usuario es responsable del uso correcto de la aplicación
- Los desarrolladores no se responsabilizan por mal uso

7. MODIFICACIONES
Estos términos pueden modificarse sin previo aviso.

8. CONTACTO
Para dudas sobre estos términos, contacta al equipo de desarrollo.

Fecha de última actualización: 27/06/2025""",
                buttons=[
                    MDRaisedButton(
                        text="CERRAR",
                        on_release=lambda x: self.terminos_dialog.dismiss()
                    )
                ]
            )
        self.terminos_dialog.open()

    def mostrar_privacidad(self):
        if not self.privacidad_dialog:
            self.privacidad_dialog = MDDialog(
                title="Política de Privacidad",
                text="""POLÍTICA DE PRIVACIDAD

1. INFORMACIÓN QUE RECOPILAMOS
Signify One no recopila información personal identificable.

2. USO DE LA INFORMACIÓN
- Los datos de voz se procesan temporalmente para reconocimiento
- No se almacenan conversaciones de voz
- No se comparten datos con terceros

3. PERMISOS DE LA APLICACIÓN
- Micrófono: Para reconocimiento de voz
- Cámara: Para detección de señas
- Almacenamiento: Para archivos temporales

4. SEGURIDAD
- Los datos se procesan localmente cuando es posible
- Conexiones seguras para servicios en línea
- No se almacenan contraseñas

5. COOKIES Y TECNOLOGÍAS SIMILARES
- No utilizamos cookies de seguimiento
- Solo cookies técnicas necesarias para el funcionamiento

6. DERECHOS DEL USUARIO
- Acceso a información personal (si la hubiera)
- Rectificación de datos incorrectos
- Eliminación de datos personales
- Portabilidad de datos

7. CAMBIOS EN LA POLÍTICA
Esta política puede actualizarse. Se notificarán cambios importantes.

8. CONTACTO
Para preguntas sobre privacidad: [email de contacto]

Fecha de última actualización: 27/06/2025""",
                buttons=[
                    MDRaisedButton(
                        text="CERRAR",
                        on_release=lambda x: self.privacidad_dialog.dismiss()
                    )
                ]
            )
        self.privacidad_dialog.open()

    def restablecer_configuracion(self):
        # Restablecer todos los valores a los predeterminados
        self.ids.volume_slider.value = 50
        self.ids.speed_slider.value = 1.0
        self.ids.mic_sensitivity.value = 0.5
        self.ids.listen_time.value = 5
        self.ids.video_quality.value = 720
        self.auto_play_active = False
        self.dark_theme_active = True
        self.ids.font_size.value = 16
        
        # Actualizar botones
        self.ids.auto_play.text = 'Activar'
        self.ids.auto_play.md_bg_color = (0.6, 0.2, 0.2, 1)
        self.ids.dark_theme.text = 'Desactivar'
        self.ids.dark_theme.md_bg_color = (0.2, 0.6, 0.2, 1)

    def toggle_auto_play(self):
        self.auto_play_active = not self.auto_play_active
        self.ids.auto_play.text = 'Activar' if not self.auto_play_active else 'Desactivar'
        self.ids.auto_play.md_bg_color = (0.2, 0.6, 0.2, 1) if self.auto_play_active else (0.6, 0.2, 0.2, 1)

    def toggle_dark_theme(self):
        self.dark_theme_active = not self.dark_theme_active
        self.ids.dark_theme.text = 'Activar' if not self.dark_theme_active else 'Desactivar'
        self.ids.dark_theme.md_bg_color = (0.2, 0.6, 0.2, 1) if self.dark_theme_active else (0.6, 0.2, 0.2, 1) 