# Visión por computadora

## Introducción

Este proyecto se enfoca en el desarrollo de una interfaz gráfica que simplifique la búsqueda y aplicación de filtros en imágenes en escala de grises con formato TIFF, en particular, se aplicará el filtro "mediana". Aprovechando los principios de la visión por computadora y la implementación de técnicas de IA aprendidas, la interfaz permitirá a los usuarios seleccionar imágenes y ajustar los parámetros de los filtros de manera interactiva.

La funcionalidad principal radica en la aplicación de filtros previamente estudiados en el contexto de la visión por computadora. Estos filtros, diseñados para mejorar la calidad de las imágenes y resaltar características específicas, serán integrados de manera modular en la interfaz. Lo importante de este proyecto es la oportunidad de ajustar los parámetros de los filtros directamente desde la interfaz gráfica, permitiendo a los usuarios personalizar el proceso de filtrado según sus necesidades.

### Visión por computadora

La **visión por computadora**, también conocida como visión artificial, es parte del campo de la inteligencia artificial, se enfoca en instruir a las computadoras para la obtención de información relevante a partir de imágenes digitales, videos y otras formas de datos visuales. Este estudio tiene como objetivo equipar a las máquinas con la facultad de interpretar y comprender su entorno visual, facultándolas así para la toma de decisiones y la formulación de recomendaciones basadas en la información visual adquirida.

En la esencia de los sistemas de visión computacional se encuentra la implementación de software de inteligencia artificial, respaldado por algoritmos matemáticos. Estos algoritmos desempeñan una función esencial al descifrar las imágenes, identificando y reconociendo patrones, formas y figuras en el proceso. La habilidad para reconocer estas características visuales permite a las computadoras generar respuestas específicas, como la comparación de elementos, la toma de decisiones o la ejecución de acciones físicas, como la manipulación de objetos.

En conclusión, la visión computacional no se limita únicamente al procesamiento pasivo de imágenes, en realidad, posibilita que las máquinas comprendan y actúen con base en la información visual adquirida. Este campo tiene aplicaciones diversas, que abarcan desde el reconocimiento de objetos y rostros hasta la automatización industrial, la realidad aumentada y otros campos, propiciando progresos notables en la confluencia entre la inteligencia artificial y la percepción visual.

### Interfaz gráfica
Una **interfaz gráfica** o interfaz para el usuario es un componente visual que posibilita la interacción entre un usuarios y un programa de manera más intuitiva. Este elemento visual emplea elementos como ventanas, iconos, botones y menús para facilitar la comunicación, permitiendo a los usuarios realizar acciones de manera más comprensible sin depender exclusivamente de comandos de texto.

La finalidad principal de una interfaz gráfica es simplificar la experiencia de usuario, haciendo que las operaciones sean más accesibles, especialmente para aquellos usuarios que no poseen conocimientos técnicos avanzados. Algunas de las características típicas de una interfaz gráfica incluyen el uso de ventanas para organizar información, iconos que representan visualmente aplicaciones o funciones, botones para activar acciones específicas, menús desplegables que ofrecen opciones organizadas y campos de entrada para ingresar datos de manera interactiva.

Las interfaces gráficas se aplican en una variedad de dispositivos, desde computadoras personales hasta dispositivos móviles y electrodomésticos inteligentes. La evolución constante de estos desarrollos ha tenido un impacto significativo en la experiencia del usuario, contribuyendo a la integración generalizada de la informática en la vida diaria.


## Materiales

1. **Python:**
Python es un lenguaje de programación de alto nivel, interpretado y generalista. Es conocido por su sintaxis clara y legible, lo que lo hace accesible tanto para principiantes como para desarrolladores experimentados. Python es utilizado en diversos campos, como desarrollo web, análisis de datos, inteligencia artificial, automatización, entre otros. Su comunidad activa y su amplio conjunto de bibliotecas hacen de Python una opción popular para una variedad de aplicaciones.

2. **OpenCV:**
El Open Source Computer Vision Library (OpenCV) es una biblioteca de visión por computadora y procesamiento de imágenes. Proporciona una amplia gama de funciones y algoritmos que facilitan el trabajo con imágenes y videos. OpenCV se utiliza en aplicaciones que abarcan desde reconocimiento de objetos y seguimiento de movimiento hasta procesamiento de imágenes médicas y realidad aumentada. Es una herramienta esencial en el campo de la visión por computadora e IA.

1. **PyQt6:**
PyQt6 es un conjunto de enlaces (bindings) de Python para Qt, un marco de desarrollo de aplicaciones multiplataforma. Qt ofrece herramientas para el desarrollo de interfaces gráficas de usuario (GUI) y es utilizado para crear aplicaciones que se ejecutan en diversos sistemas operativos. PyQt6 facilita la integración de la funcionalidad de Qt en aplicaciones Python, permitiendo a los desarrolladores crear interfaces gráficas interactivas y atractivas.

1. **Formato TIFF:**
El formato TIFF es un estándar de archivo para almacenar imágenes, especialmente utilizado en el ámbito de la edición de imágenes y la industria de la impresión. Lo notable del formato TIFF es su capacidad para preservar la calidad de la imagen sin pérdida de datos, ya que soporta imágenes de alta resolución y utiliza compresión sin pérdida. Además, el formato TIFF permite la inclusión de metadatos y múltiples capas, lo que lo hace adecuado para diversas aplicaciones, como la manipulación de imágenes médicas y la preservación de archivos de imágenes de alta calidad.

1. **PEP8:**
El Python Enhancement Proposal 8 (PEP 8) es un conjunto de directrices y convenciones de estilo de código para el lenguaje de programación Python, el cual proporciona recomendaciones sobre cómo estructurar y formatear el código Python de manera consistente, con el objetivo de mejorar la legibilidad y la comprensión del código fuente. Las "normas" del PEP 8 abarcan diversos aspectos del código, incluyendo la indentación, el uso de espacios en blanco, la longitud de las líneas, la importación de módulos, y la nomenclatura de variables y funciones.

## Métodos

### Filtros digitales

Los filtros digitales son herramientas utilizadas en el procesamiento de imágenes para alterar o mejorar sus características o componentes. Estos filtros pueden aplicarse a datos digitales para suavizar, resaltar, eliminar ruido u otras modificaciones específicas.

#### Filtro del la mediana (median filter)

El filtro de la mediana es un tipo de filtro digital no lineal que se utiliza comúnmente en el procesamiento de imágenes. Su función principal es reducir el ruido y preservar los bordes en una imagen. A diferencia de otros filtros, como los filtros de media aritmética, el filtro de la mediana no promedia los valores de los píxeles en una ventana, sino que selecciona el valor central de la distribución ordenada de los valores de píxeles en esa ventana.

El proceso del filtro de la mediana implica ordenar los valores de píxeles en una ventana deslizante y seleccionar el valor central como el nuevo valor del píxel en el centro de la ventana. Esto tiene el efecto de eliminar los valores extremos y preservar los bordes, lo que lo hace efectivo para suavizar imágenes sin sacrificar la nitidez de los detalles.

##### Implementación matemática

La explicación matemática más detallada involucra el ordenamiento de conjuntos de datos y la selección de medianas:

1. Supongamos que tenemos una ventana deslizante de tamaño (n \times n\), y recopilamos \(n \times n\) valores de píxeles en esta ventana.
1. Ordenamos estos valores de manera ascendente o descendente.
1. El valor central de esta distribución ordenada se convierte en el nuevo valor del píxel central en la imagen.

Esta operación se repite para cada posición de la ventana deslizante a lo largo de la imagen. La principal ventaja de utilizar la mediana en lugar de otros métodos de filtrado es su capacidad para preservar los detalles y bordes en la imagen, ya que selecciona el valor central sin verse afectado por valores extremos o ruido puntual.

### Mockup (bosquejo)
![Copia de Fractales y dónde encontarlos (1)](https://github.com/monseher00/Vision-por-computadora/assets/92997919/cff93fe7-3035-4c59-8a3e-96b9ac908e72)


## Código

### Visualización del programa

1. Visualización de la ventana:
   ![Captura de pantalla 2023-11-13 121532](https://github.com/monseher00/Vision-por-computadora/assets/92997919/c11a36b8-557f-439f-816c-55d1356f2650)

2. Cargar imagen:
   ![Captura de pantalla 2023-11-13 121605](https://github.com/monseher00/Vision-por-computadora/assets/92997919/b15c2d9b-cdfd-4280-aecb-e29760586a3b)

3. Imagen original (sin filtro):
   ![Captura de pantalla 2023-11-13 121630](https://github.com/monseher00/Vision-por-computadora/assets/92997919/0b29885f-88a0-4569-820f-619f1602452f)

4. Deslizador para aplicar el filtro:
![Captura de pantalla 2023-11-13 121923](https://github.com/monseher00/Vision-por-computadora/assets/92997919/f2a1f634-be00-4e8e-8923-81d8085f843f)


## Conclusión

En conclusión, este proyecto fusiona conceptos clave de visión por computadora, interfaces gráficas y procesamiento de imágenes en una herramienta integral. La implementación de una interfaz gráfica para la búsqueda y aplicación de filtros en imágenes en escala de grises (formato TIFF) representa un paso significativo hacia la accesibilidad y la personalización en el ámbito del procesamiento visual.

