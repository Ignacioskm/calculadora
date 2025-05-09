# Calculadora hecha en Python.

* Ya que es un ejercicio en modo de aprendizaje tomare nota de los recursos utilizados

### Bibliotecas:
- Se utilizo tkinter ya que es la biblioteca que viene incorporada con python, sirve para crear interfaces graficas de usuario (GUI)

## Herramientas de la biblioteca usadas

### Ventana Principal
- .Tk() = Crea la ventana principal de la aplicación. Es el "Contenedor" de todos los widgets(botones, etiquetas, etc.)
- .title() = Cambia el titulo que aparece en la barra superior de la ventana.
- .geometry() = Define el tamaño de la ventana.
- .resizable(ancho,alto)= Controla si el usuario puede cambiar el tamaño de la ventana, si agregaramos los argumentos 0,0 = no se puede agrandar ni achicar.
-------------
### Pantalla Calculadora.
- .StringVar() = Es una variable especial que permite enlazar texto de un widget (Como label) a una variable, se puede cambiar el contenido utilizando .set().
- .label = Crea una etiqueta (texto visible)
- textvariable = Vincula el texto , asi puedes cambiar su contenido dinamicamente.
-------------
### Para los botones: 
- Button = Crea un boton que el usuario pueda presionar.
- command = indica que funcion se ejecuta cuando se hace click en el botón
- text="" =El texto que se muestra en el boton
- font(fuente,tamaño)= Cambia el tipo  el tamaño de la letra.
- bg = Cambia el color del fondo (background)
- fg = Cambia el color del texto (foreground)
- width = Tamaño del boton ancho
- height = Tamaño del boton alto
-------------
### Posicionamiento de los Widgets:
- .grid() = Posiciona un widget en un sistema de filas y columnas.
- row = En que fila estará
- column = En que columna estará
- padx = Margen horizontal
- pady = Margen vertical
- sticky="nsew" = Hace que el botón se expanda en todas las direcciones (norte,sur,este,oeste)

- root.grid_rowconfigure(i,weight=1)
- root.grid_columnconfigure(i,weight=1)

- Estas lineas hacen que todas las filas y columnas tengan el mismo peso, es decir, que se expandan proporcionalmente cuando cambias el tamaño de la ventana(si resizable lo permitiera).
-------------
### Funciones Extras:
- eval() = Evalua la cadena de texto como si fuera codigo python, por ejemplo "3+5*2" como 13
- messagebox.showerror() = Muestra una ventana emergente de error (popup).




![](https://pandao.github.io/editor.md/images/logos/editormd-logo-180x180.png)

![](https://img.shields.io/github/stars/pandao/editor.md.svg) ![](https://img.shields.io/github/forks/pandao/editor.md.svg) ![](https://img.shields.io/github/tag/pandao/editor.md.svg) ![](https://img.shields.io/github/release/pandao/editor.md.svg) ![](https://img.shields.io/github/issues/pandao/editor.md.svg) ![](https://img.shields.io/bower/v/editor.md.svg)
