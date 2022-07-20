# Playground Intermedio 1

Para esta clase, copie los archivos del proyecto "ProyectoCoder" a una nueva carpeta

## Control de versiones de nuestro proyecto

Iniciamos subiendo el proyecto ProyectoCoder a GitHub

1. Desde la terminal y parados en la carpeta del proyecto, ejecutamos:

        git init

2. Conectamos nuestro proyecto en Git (local) con mi proyecto en GitHub ejecutando:

        git remote add origin url_repo_GitHub

3. Corremos

        git add .

4. Commiteamos

        git commit -m "Commit inicial Clase 19"

5. Pusheamos o subimos a GitHub

        git push origin master

De aqui en delante hay que hacer practica comun cada vez que modifiquemos algo que este correcto y funcionando

- git status
- git add
- git commit -m "comit comment"
- git push origin master
- verificar que se subio a GitHub
- git pull del repo si el proyecto deja de jalar

---

## Vistas y URLs Avanzadas

Para simplificar y mejorar la reutilizacion de codigo, veamos como usar URLs de manera mas avanzada

GENERAR UN ARCHIVO URL.PY EN NUESTRA APP

1. Crear en AppCoder urls.py

2. Le importamos el path:

        from django.urls import path

3. Importamos las vistas

        from .views import *  # usamos .views porque views esta dentro del mismo directorio donde esta mi archivo urls.py (self reference)

4. Copiamos y pegamos el urlpatterns que ya teníamos, pero sin el admin

5. Dejamos el admin, SOLO, en el url del Proyecto (tampoco necesita las vistas)

6. Lo más importante, relacionamos el urls.py de la App con el Proyecto:

        path(‘AppCoder/’, include(‘AppCoder.urls’))

    Lo que estamos haciendo es crear una path/url para cada app que yo genere en mi proyecto. Asi, desde mi proyecto principal, solo voy a llamar al path de mi App (las urls de mi app). Y lo que voy a hacer es que en cada app, yo voy a organizar y manejar mis urls en mi propio archivo de urls, el cual se va a mandar llamar desde mi proyecto principal cuando necesive mostrar una vista

    Lo que habiamos hecho la clase pasada fue importar las vistas de mi app a mi proyecto principal y generar un path para cada vista en las urls de mi proyecto. De haber seguido trabajando asi, hubiese tenido que importar todas las vistas de todas mis apps y generar un path en mi archivo principal del proyecto para cada vista, lo que haria del archivo de urls inmanejable

7. Ahora si, creamos los paths para cada vista de mi app en el urls.py de mi app

        urlpatterns = [
    
            path('curso/', curso),
            path('profesores/', profesores),
            path('estudiantes/', estudiantes),
            path('entregables/', entregables),
            path('', inicio),
            
        ]

8. El path de '' o la vacia es para definir que vista mostrar en url/AppCoder/

9. De igualmanre, habria que definir una '', inicio para mi url principal de mi proyecto (127.0.0.1:8000/), de lo contrario, nuestro navegador mostrara una pantalla de error diciendo que no hay path para esa url

## Creacion de temaplates para nuestra AppCoder

1. Dentro de la carpeta AppCoder, crear una carpeta llamada 'templates' y dentro de templates otra folder llamada AppCoder

2. Aqui crearemos un archivo html para cada una de nuestras vistas

3. A una de ellas le ponemos en el body:

        <body style="background-color:blue">
        
        </body>

4. Al resto de los html les ponemos el nombre de una vista

5. En nuestras views.py, cambiamos el self por request:

        def inicio(request):
            return HttpResponse('Vista de inicio')

        def cursos(request):
            return HttpResponse('Vista de cursos')

        def profesores(request):
            return HttpResponse('Vista de profesores')

        def estudiantes(request):
            return HttpResponse('Vista de estuduantes')

        def entregables(request):
            return HttpResponse('Vista de entregables')

6. Y en el return vamos a render el html que queremos en cada vista

        def inicio(request):
            return render (request, 'AppCoder/inicio.html')

        def cursos(request):
            return render (request, 'AppCoder/cursos.html')

        def profesores(request):
            return render (request, 'AppCoder/profesores.html')

        def estudiantes(request):
            return render (request, 'AppCoder/estuduantes.html')

        def entregables(request):
            return render (request, 'AppCoder/entregables.html')

7. Dentro de mis vista, mi return es una funcion para renderizar el html dentro de mis templates

    - Recordar tener el modulo siguiente en nustras view para poder usar la funcion render

            import django.shortcuts import render 

8. Al acceder a la url de cada vista, ya debemos de ver lo que hay en el html de cada una.

---

## BOOTSTRAP

- Es una herramienta que usaremos para bajar templates desde <https://startbootstrap.com/previews/landing-page> y usar en nuestro proyecto

- Biitstrap es un framework de Javascript y CSS.

- Elegimos la 'Free Download', el cual contiene varias carpetas que usaremos en muestra app (assets, css, js)

1. Crear una carpeta dentro de AppCoder llamada static y dentro de esta, otra llamada AppCoder

2. Guardamos ahi los archivos, recursos y demas que mi htmls y mis paginas necesiten.

3. Copiamos lo del Free Donwload dentro de static/AppCoder

4. El html de la descarga lo movemos a templates/AppCoder y lo renombramos inicio.html

5. Cargamos los archivos static escribiendo lo siguiente en nuestro ```<head>```

        {% load static %}

6. Tambien en el encabezado esta la referencia a la ubicacion de los styles:

        <link href="css/styles.css" rel="stylesheet" />

    Esta la cambiamos para indicarle donde estan ubicados los styles que descargue y guarde en static/AppCoder/css/styles.css

        <link href="{% static 'AppCoder/css/styles.css' %}" rel="stylesheet" />

7. Si teniamos el server corroendo, lo paramos y lo volvemos a correr para que jale los estilos y al cargar la pagina inicio, ya debe estar renderizada con estilos.