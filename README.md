# _*Kovix Automation Challenge*_
 
En este repositorio, dejo subido el challenge técnico de Kovix, una descripción de la instalación y cómo correr los test por consola.

## _*Instalación de Python, Git y Chrome*_:
- Se deberá instalar python: para ello, ingresaremos en el link "https://www.python.org/" y descargaremos la versión más
actual (para este proyecto, se utilizó python 3.10). Al momento de instalar se deberá tildar la opción "Add Python.exe to PATH"
- Se deberá instalar git. Para ello ingresaremos en "https://git-scm.com/" y descargaremos la última versión compatible 
con nuestro procesador. (esto en caso de usar Windows, en ubuntu ya viene instalado por defecto)
- Se utilizará como navegador chrome, para descargarlo deberemos ingresar en "https://www.google.com/intl/es-419/chrome/" 
y hacer click en "Descargar Chrome".

## _*Clonación del proyecto*_:
Una vez instalado Git, deberemos clonar el proyecto en el lugar que nosotros deseemos, para lo cual, deberemos abrir una consola en el lugar que queramos y ejecutar el siguiente comando:
- ```git clone https://github.com/nicolaspablocordoba/Kovix_challenge.git```
- https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository (instructivo de ayuda)

## _*Librerías necesarias*_:
Para poder ejecutar el proyecto, se deberán instalar las siguientes librerías necesarias para correr el proyecto. 
Para ello abriremos una consola y nos posicionaremos sobre la carpeta raiz del proyecto (```\Kovix_challenge```) e introduciremos el siguiente comando:
- ```pip install -r requirements.txt```. Si la instalación de python se hizo correctamente, se instalaran todas las librerías necesarias.

## _*Ejecutar los test por consola*_:
- Antes de ejecutar los test desde la consola, 
deberemos hacer una modificación en el archivo [JSON_DATA_FILE.json](Data%2FJSON_DATA_FILE.json), 
modificando el valor "ABSOLUTE_PATH" por el path absoluto hasta la raiz del proyecto (se obtiene ingresando a la carpeta y copiando la ruta de la carpeta) 
(Ejemplo: Si la carpeta se descarga dentro del escritorio de windows se deberá modificar el path por 
```C:\\Escritorio\\Kovix_challenge``` IMPORTANTE: en caso de ser windows, debe utilizarse la doble barra invertida)


- Para poder correr los test por consola, ingresaremos por la consola hasta la carpeta ```\Test``` y luego correremos el 
comando ```python3 -m unittest Suite_criterios_de_aceptacion.py``` para ubuntu y en caso de que estemos utilizando Windows 
el comando será 
```py -m unittest Suite_criterios_de_aceptacion.py```

## _*Consideraciones personales y explicaciones del código*_:
- Para realizar este challenge, decicí utilizar la herramienta Selenium Webdriver con Python, ya que, está considerada una
herramienta muy robusta para automatizar, tiene una gran comunidad detrás en caso de necesitar resolver algún problema y también permite 
agregar código propio para resolver alguna situación particular en caso de ser necesario. 


- Empleé el patron de diseño POM (Page Object Model), que encapsula el comportamiento
de cada uno de los elementos de la pantalla para poder usarlos luego en los test.


- En cada uno de los test se encuentra comentado al principio de cada test, un resumen de los pasos que recorrerá el test 
y luego, en cada paso, se encontrará comentado que paso es el que se está realizando.


- En todo el proyecto se utilizan esperas implicitas (dentro de los test) y explicitas (dentro de los page objects).
Se puede observar en el test_sign_up, en la línea 55 un ```time.sleep(0.5)```, en general, el uso de sleeps se considera una mala 
práctica, pero decidí utilizarlo en este caso debido a que la página detecta la automatización y me envía a una pantalla de error.


- Para el test "test_create_account" implementé el archivo [Functions_create_data_random.py](src%2FFunctions%2FFunctions_create_data_random.py)
que tiene las funciones para poder crear un email, usuario y contraseña aleatorio.


- Al momento de finalizar la suite, se genera un reporte HTML que registra en que momento se corrió la suite, cuanto tiempo
tardó en correrse, cuantos test estaban incluidos en la suite, que test pasaron correctamente, que test fallaron el assert, 
que test tuvieron un error (antes de poder ejecutar el assert) y que test fueron skipeados. En caso de encontrarse con un error o un fallo,
se mostrará que tipo de error fué y el código en el que apareció ese error o fallo.


- Se agregaron las pruebas adicionales "test_empty_search" y "test_search_movie_with_year_filter" dentro de los test de Landing page,
en la pantalla de Sign In se agregaron las pruebas adicionales "test_login_empty_fields" y "test_login_with_incorrect_credentials", 
y por último se agregó la prueba adicional "test_create_account" en la pantalla de Sign up.


- En el archivo de "Test_landing_page" se podrá observar tres pruebas adicionales extra a las mencionadas en el punto anterior, estas son
"test_landing_page_fail_report", "test_landing_page_error_report" y "test_landing_page_skip_report", las cuales fueron puestas para poder ver
los resultados de un fail, un error y un skip dentro del reporte generado por la suite.


- Para los reportes HTML, utilizo la librería HtmlTestRunner, la cual se encuentra dentro del proyecto y no en las 
librerías incluidas en el requirements.txt, debido a un error dentro de la misma que imposibilita utilizarlo con versiones actuales de python, por lo cual,
pasé la librería al proyecto, corregí el error de incompatibilidad y luego la llamo en las suites como un archivo común del proyecto.


- Si se desea correr los test en modo "headless" se deberá ingresar en cada test y modificar ```options.add_argument("--start-maximized")``` por ```options.add_argument("--headless")```


- Por último, a modo de consejo, les recomiendo utilizar algún editor de código tipo Pycharm para poder poner breakpoints en los pasos del test
y ver detalladamente el paso a paso de estos, ya que, debido a que la pantalla carga muy rápido, los test corren en un promedio de 3 segundos cada uno
y casi no es posible ver que es lo que está pasando en ese momento.



Cualquier duda o consulta, quedo a su disposición. ¡Saludos!