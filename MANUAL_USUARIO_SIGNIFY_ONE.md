# MANUAL DE USUARIO - SIGNIFY ONE
## Aplicación de Aprendizaje de Lengua de Señas

---

## ÍNDICE
1. [Introducción](#introducción)
2. [Requisitos del Sistema](#requisitos-del-sistema)
3. [Instalación](#instalación)
4. [Pantalla Principal](#pantalla-principal)
5. [Utilizar Voz](#utilizar-voz)
6. [Une Palabras](#une-palabras)
7. [Agregar Palabras](#agregar-palabras)
8. [Ver Diccionario](#ver-diccionario)
9. [Configuración](#configuración)
10. [Asistente de Voz](#asistente-de-voz)
11. [Solución de Problemas](#solución-de-problemas)
12. [Glosario](#glosario)

---

## INTRODUCCIÓN

**Signify One** es una aplicación educativa diseñada para facilitar el aprendizaje de la lengua de señas mexicana. La aplicación combina tecnología de reconocimiento de voz, síntesis de voz y reproducción de videos para crear una experiencia de aprendizaje interactiva y accesible.

### Características Principales:
- **Reconocimiento de voz en español**
- **Síntesis de voz para retroalimentación**
- **Videos de señas organizados por categorías**
- **Interfaz intuitiva y accesible**
- **Asistente virtual integrado**

---

## REQUISITOS DEL SISTEMA

### Requisitos Mínimos:
- **Sistema Operativo**: Windows 10, macOS 10.14+, o Linux
- **Python**: Versión 3.7 o superior
- **Memoria RAM**: 4 GB mínimo
- **Almacenamiento**: 500 MB de espacio libre
- **Micrófono**: Para funciones de reconocimiento de voz
- **Altavoces/Auriculares**: Para reproducción de audio
- **Cámara web**: Para detección de señas (opcional)

### Dependencias Requeridas:
```
kivy==2.3.0
kivymd==1.1.1
mutagen==1.47.0
SpeechRecognition==3.10.0
gTTS==2.4.0
opencv-python==4.8.1.78
playsound==1.3.0
```

---

## INSTALACIÓN

### Paso 1: Preparar el Entorno
1. Asegúrate de tener Python instalado en tu sistema
2. Abre una terminal o línea de comandos
3. Navega al directorio de la aplicación

### Paso 2: Instalar Dependencias
```bash
pip install -r requirements.txt
```

### Paso 3: Ejecutar la Aplicación
```bash
python main.py
```

---

## PANTALLA PRINCIPAL

La pantalla principal es el centro de navegación de la aplicación. Aquí encontrarás todas las funcionalidades disponibles organizadas en tarjetas interactivas.

### Elementos de la Interfaz:

#### **Tarjeta "Utilizar Voz" (Roja)**
- **Función**: Reconocimiento de voz para palabras individuales
- **Acceso**: Toca la tarjeta roja con el ícono de reconocimiento
- **Uso**: Permite hablar palabras y ver su representación en señas

#### **Tarjeta "Une Palabras" (Azul)**
- **Función**: Creación de oraciones mediante drag & drop
- **Acceso**: Toca la tarjeta azul con el ícono de drag
- **Uso**: Arrastra palabras para formar oraciones completas

#### **Tarjeta "Agregar Palabras" (Verde)**
- **Función**: Añadir nuevas palabras al diccionario
- **Acceso**: Toca la tarjeta verde con el ícono de palabra
- **Uso**: Agregar vocabulario personalizado

#### **Tarjeta "Ver Diccionario" (Amarilla)**
- **Función**: Consultar el vocabulario disponible
- **Acceso**: Toca la tarjeta amarilla con el ícono de diccionario
- **Uso**: Explorar palabras organizadas por categorías

#### **Tarjeta "Configuración" (Naranja)**
- **Función**: Ajustes de la aplicación
- **Acceso**: Toca la tarjeta naranja con el ícono de configuración
- **Uso**: Personalizar la experiencia de usuario

### Navegación:
- **Botón Home**: Regresa a la pantalla principal desde cualquier sección
- **Transiciones**: Animaciones suaves entre pantallas
- **Responsive**: Se adapta a diferentes tamaños de pantalla

---

## UTILIZAR VOZ

Esta función permite reconocer palabras habladas y mostrar su representación en lengua de señas.

### Cómo Usar:

#### **1. Acceso a la Función**
- Desde la pantalla principal, toca la tarjeta **"Utilizar Voz"**
- Se abrirá la pantalla de reconocimiento de voz

#### **2. Interfaz de Reconocimiento**
- **Estado**: Muestra "¡Listo para escuchar!" cuando está preparado
- **Botón de Micrófono**: Toca para comenzar a escuchar
- **Área de Video**: Muestra la seña correspondiente a la palabra reconocida

#### **3. Proceso de Reconocimiento**
1. **Toca el botón de micrófono**
2. **Habla claramente** la palabra que deseas reconocer
3. **Espera** a que se procese el audio
4. **Observa** el video de la seña correspondiente

#### **4. Palabras Reconocibles**
La aplicación reconoce palabras organizadas en categorías:

**Sujetos (S):**
- yo, tú, él, ella, mi, me, amiga, amigo, hermana, hermano, etc.

**Objetos (O):**
- comedor, computadora, crema, escritorio, fuego, internet, etc.

**Verbos (V):**
- abandonar, abrir, admirar, aprender, ayudar, buscar, etc.

**Tiempo (T):**
- abril, agosto, ahora, ayer, hoy, mañana, tarde, noche, etc.

**Lugar (L):**
- abajo, allá, aquí, banco, biblioteca, casa, cuarto, etc.

#### **5. Mensajes del Sistema**
- **"Escuchando..."**: El sistema está procesando tu voz
- **"Texto reconocido: [palabra]"**: Confirmación del reconocimiento
- **"No se pudo entender el audio"**: Error en el reconocimiento
- **"Error en el servicio de reconocimiento"**: Problema de conexión

---

## UNE PALABRAS

Esta función permite crear oraciones completas arrastrando palabras y ver su representación en señas.

### Cómo Usar:

#### **1. Acceso a la Función**
- Desde la pantalla principal, toca la tarjeta **"Une Palabras"**
- Se abrirá la pantalla de construcción de oraciones

#### **2. Interfaz de Construcción**
- **Barra de Búsqueda**: Busca palabras específicas
- **Palabras Disponibles**: Lista horizontal de palabras seleccionables
- **Área de Oración**: Muestra las palabras seleccionadas
- **Botones de Control**: Reproducir y limpiar oración
- **Área de Video**: Reproduce las señas de la oración

#### **3. Proceso de Construcción**

**Paso 1: Buscar Palabras**
- Usa la barra de búsqueda para encontrar palabras específicas
- Escribe parte del nombre de la palabra
- La lista se filtrará automáticamente

**Paso 2: Seleccionar Palabras**
- Toca las palabras que deseas incluir en tu oración
- Las palabras seleccionadas aparecerán en el área de oración
- Puedes seleccionar múltiples palabras

**Paso 3: Formar la Oración**
- Las palabras se reordenan automáticamente según la gramática de la lengua de señas
- El orden sigue la estructura: Tiempo + Lugar + Sujeto + Objeto + Verbo

**Paso 4: Reproducir la Oración**
- Toca el botón de **reproducción** (ícono de play)
- Observa los videos de señas en secuencia
- Cada palabra se reproduce automáticamente

#### **4. Controles Disponibles**
- **Botón Play**: Reproduce la oración completa
- **Botón Delete**: Limpia la oración actual
- **Botón Home**: Regresa a la pantalla principal

#### **5. Ejemplo de Uso**
1. Busca "yo" en la barra de búsqueda
2. Selecciona "yo" de la lista
3. Busca "ayudar" y selecciónalo
4. Busca "tú" y selecciónalo
5. La oración se formará: "yo tú ayudar"
6. Toca play para ver las señas

---

## AGREGAR PALABRAS

Esta función permite añadir nuevas palabras al diccionario de la aplicación.

### Cómo Usar:

#### **1. Acceso a la Función**
- Desde la pantalla principal, toca la tarjeta **"Agregar Palabras"**
- Se abrirá la pantalla de agregar palabras

#### **2. Interfaz de Agregar Palabras**
- **Barra de Progreso**: Indica el progreso del proceso
- **Paso 1**: Información de la palabra
- **Paso 2**: Subida del video

#### **3. Proceso de Agregar Palabra**

**Paso 1: Información de la Palabra**
- **Campo "Nueva Palabra"**: Escribe la palabra que deseas agregar
- **Campo "Tipo de palabra"**: Especifica la categoría:
  - **S**: Sujeto
  - **O**: Objeto
  - **V**: Verbo
  - **T**: Tiempo
  - **L**: Lugar
- **Botón "Siguiente"**: Avanza al siguiente paso

**Paso 2: Subida del Video**
- **Campo "Nombre del video"**: Nombre del archivo de video
- **Campo "Sube tu video aquí"**: Ruta al archivo de video
- **Botón "Previo"**: Regresa al paso anterior
- **Botón "Guardar"**: Guarda la nueva palabra

#### **4. Requisitos del Video**
- **Formato**: MP4 recomendado
- **Duración**: 2-5 segundos por palabra
- **Calidad**: Resolución mínima 480p
- **Contenido**: Seña clara y bien iluminada

#### **5. Navegación**
- **Botón de Flecha**: Regresa a la pantalla principal
- **Barra de Progreso**: Muestra el avance en el proceso

---

## VER DICCIONARIO

Esta función permite explorar todas las palabras disponibles en la aplicación.

### Cómo Usar:

#### **1. Acceso a la Función**
- Desde la pantalla principal, toca la tarjeta **"Ver Diccionario"**
- Se abrirá la pantalla del diccionario

#### **2. Organización del Diccionario**
Las palabras están organizadas en 5 categorías principales:

**Sujetos (S):**
- Pronombres personales y nombres de personas
- Ejemplos: yo, tú, él, ella, amigo, hermana, padre, madre

**Objetos (O):**
- Cosas y elementos materiales
- Ejemplos: computadora, libro, mesa, lápiz, teléfono

**Verbos (V):**
- Acciones y estados
- Ejemplos: aprender, enseñar, comer, dormir, trabajar

**Tiempo (T):**
- Referencias temporales
- Ejemplos: hoy, ayer, mañana, ahora, tarde, noche

**Lugar (L):**
- Ubicaciones y espacios
- Ejemplos: casa, escuela, trabajo, parque, hospital

#### **3. Navegación del Diccionario**
- **Filtros por Categoría**: Selecciona una categoría específica
- **Búsqueda**: Busca palabras por nombre
- **Vista de Lista**: Todas las palabras organizadas alfabéticamente

#### **4. Información de Palabras**
Para cada palabra se muestra:
- **Nombre**: La palabra en español
- **Categoría**: Tipo gramatical
- **Video**: Vista previa de la seña (si está disponible)

---

## CONFIGURACIÓN

Esta sección permite personalizar la experiencia de usuario.

### Opciones Disponibles:

#### **1. Configuración de Audio**
- **Volumen**: Ajustar el volumen de reproducción
- **Velocidad de Reproducción**: Controlar la velocidad de los videos
- **Idioma de Voz**: Seleccionar el acento del español

#### **2. Configuración de Video**
- **Calidad de Video**: Ajustar la resolución de reproducción
- **Reproducción Automática**: Activar/desactivar reproducción continua
- **Tamaño de Pantalla**: Ajustar el tamaño de los videos

#### **3. Configuración de Reconocimiento de Voz**
- **Sensibilidad del Micrófono**: Ajustar la sensibilidad
- **Idioma de Reconocimiento**: Seleccionar variante del español
- **Tiempo de Escucha**: Configurar duración de escucha

#### **4. Configuración de Interfaz**
- **Tema**: Cambiar entre tema claro y oscuro
- **Tamaño de Fuente**: Ajustar el tamaño del texto
- **Animaciones**: Activar/desactivar efectos visuales

---

## ASISTENTE DE VOZ

El asistente virtual integrado proporciona ayuda y responde a comandos de voz.

### Comandos Disponibles:

#### **Saludos y Despedidas**
- **"Hola"** → El asistente responde con un saludo
- **"Adiós"** → El asistente se despide

#### **Información Personal**
- **"¿Qué eres?"** o **"¿Quién eres?"** → El asistente se presenta como "Sify"
- **"¿Qué puedes hacer?"** → Lista las funcionalidades disponibles

#### **Información Temporal**
- **"¿Qué día es hoy?"** → Proporciona la fecha actual
- **"¿Qué hora es?"** → Indica la hora actual

#### **Entretenimiento**
- **"Cuéntame un chiste"** → El asistente cuenta un chiste

#### **Ayuda**
- **"Ayuda"** → Proporciona información sobre comandos disponibles
- **"¿Cómo funciona?"** → Explica el funcionamiento de la aplicación

### Cómo Usar el Asistente:

#### **1. Acceso**
- El asistente está disponible en la pantalla principal
- Toca el botón de micrófono para activarlo

#### **2. Interacción**
- Habla claramente y cerca del micrófono
- Espera la respuesta del asistente
- El asistente responde con voz en español

#### **3. Indicadores Visuales**
- **Animación de Círculo**: Indica que el asistente está escuchando
- **Cambio de Color**: Muestra el estado de procesamiento

---

## SOLUCIÓN DE PROBLEMAS

### Problemas Comunes y Soluciones:

#### **1. Problemas de Reconocimiento de Voz**

**Síntoma**: No reconoce palabras habladas
**Soluciones**:
- Verifica que el micrófono esté conectado y funcionando
- Habla más cerca del micrófono
- Reduce el ruido ambiental
- Verifica la conexión a internet (requerida para Google Speech Recognition)

**Síntoma**: Error "No se pudo entender el audio"
**Soluciones**:
- Habla más claramente y despacio
- Verifica que estés hablando en español
- Intenta en un ambiente más silencioso

#### **2. Problemas de Reproducción de Video**

**Síntoma**: Los videos no se reproducen
**Soluciones**:
- Verifica que los archivos de video estén en la carpeta correcta
- Asegúrate de que los videos estén en formato MP4
- Reinicia la aplicación

**Síntoma**: Videos con calidad baja
**Soluciones**:
- Verifica la resolución de los archivos de video
- Ajusta la configuración de calidad en la aplicación

#### **3. Problemas de Audio**

**Síntoma**: No se escucha el audio del asistente
**Soluciones**:
- Verifica que los altavoces estén conectados y funcionando
- Ajusta el volumen del sistema
- Verifica la configuración de audio en la aplicación

#### **4. Problemas de Rendimiento**

**Síntoma**: La aplicación funciona lento
**Soluciones**:
- Cierra otras aplicaciones que consuman recursos
- Verifica que tengas suficiente memoria RAM disponible
- Reinicia la aplicación

#### **5. Problemas de Instalación**

**Síntoma**: Error al instalar dependencias
**Soluciones**:
- Verifica que tengas Python 3.7 o superior instalado
- Actualiza pip: `pip install --upgrade pip`
- Instala las dependencias una por una si es necesario

### Contacto para Soporte:
Si los problemas persisten, verifica:
1. La versión de Python instalada
2. Los permisos de micrófono y cámara
3. La conexión a internet
4. Los requisitos del sistema

---

## GLOSARIO

### Términos Técnicos:

**API (Application Programming Interface)**: Conjunto de reglas que permite que diferentes aplicaciones se comuniquen entre sí.

**gTTS (Google Text-to-Speech)**: Servicio de Google que convierte texto en voz.

**Kivy**: Framework de Python para desarrollo de aplicaciones móviles y de escritorio.

**KivyMD**: Biblioteca de componentes de Material Design para Kivy.

**MediaPipe**: Biblioteca de Google para detección de manos y gestos.

**OpenCV**: Biblioteca de visión por computadora para procesamiento de imágenes y video.

**Speech Recognition**: Reconocimiento automático de voz.

### Términos de Lengua de Señas:

**Seña**: Movimiento o gesto de las manos que representa una palabra o concepto.

**Alfabeto Manual**: Sistema de señas que representa las letras del alfabeto.

**Gramática Visual**: Estructura gramatical específica de las lenguas de señas.

**Configuración Manual**: Forma específica de las manos para realizar una seña.

**Orientación**: Dirección hacia donde apuntan las manos durante la seña.

**Movimiento**: Acción que realizan las manos para completar la seña.

**Expresión Facial**: Elemento importante que acompaña las señas para dar contexto.

---

## CONCLUSIÓN

Signify One es una herramienta poderosa para el aprendizaje de la lengua de señas mexicana. Con sus múltiples funcionalidades, interfaz intuitiva y tecnología avanzada, proporciona una experiencia de aprendizaje completa y accesible.

### Recursos Adicionales:
- **Documentación**: Consulta la documentación técnica para desarrolladores
- **Comunidad**: Únete a la comunidad de usuarios para compartir experiencias
- **Actualizaciones**: Mantén la aplicación actualizada para obtener nuevas funcionalidades

### Agradecimientos:
Gracias por elegir Signify One para tu aprendizaje de lengua de señas. Esperamos que esta herramienta te ayude a desarrollar tus habilidades de comunicación y a conectar con la comunidad sorda.

---

*Manual de Usuario v1.0 - Signify One*
*Última actualización: [27/06/25]* 