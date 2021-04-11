# Django-tutorial ✔
## Bloc de Django para aprendices
El propósito de este repositorio es aprender Django para desarrollo web 😎 realizando pequeños proyectos y explorando el potencial que nos ofrece Django como Framework. 
Así mismo, con este bloc personal pretendo refrescar mi memoria y comenzar a reforzar mis métodos de auto-aprendizaje. 

## Django y Python 👀🐍
Django es una herramienta **Open Source** gratuita (recordemos que no todo el Open Source es gratis). Con Django podremos desarrollar de manera rápida y sencilla páginas web tanto complejas como sencillas. Al igual que otros Frameworks de desarrollo, Django **requiere conocimientos de programación en el lenguaje Python** (de no tenerlos, sería recomendable volver después de adquirir algo de conocimiento importante).

Recordando que Django es un Framework para Python, no debería sorprendernos que necesitamos tener **Python instalado**.
Instalar Python es relativamente sencillo y se da una (breve) explicación a continuación.

**❗NOTA❗:** Por ahora solo se contempla la explicación para SO Windows. Quizá después me aventure a realizar la explicación en un entorno Linux.

#### Instalación de Python 🐍

#### Instalación de Django 🐱‍👤

## Abriendo un proyecto en Django 🐱‍💻

Para la creación de un proyecto web con Django, haremos uso de la terminal (cmd para los panas) o símbolo del sistema. Para este punto es importante ya haber realizado tanto la instalación de Python como la de Django, de lo contrario no funcionará lo explicado a continuación. Una vez instalado, seguimos los pasos:

1. Abre una terminal (CMD) en Windows
2. Con la terminal (o explorador de archivos, si lo prefieres) crea un directorio donde será el repositorio para el proyecto a crearse. 
3. Creado el directorio, nos movemos a él desde la terminal de Windows. 
4. Para crear nuestro primer proyecto, ya posicionados en el directorio creado, utilizamos la sintaxis:

   > django-admin startproject \[Nombre de tu proyecto]

Donde en Nombre de tu proyecto, debes poner el nombre de tu eleccion, ejemplo:

   > django-admin startproject Proyecto1

Pulsamos enter y en el explorador de archivos podremos observar que se ha creado la carpeta con archivos **.py** dentro.    
Al posicionarlos con la terminal dentro del directorio que acabamos de crear, tendremos acceso a una variedad de comandos reconocidmos por un archivo **manage.py** para poder verlos todos, podemos hacer uso de la sintaxis:
    
   > manage.py help
    
De igual forma puedes obtener más conocimiento sobre estos comandos en la documentación de la página de [Django][1].
[1]: <https://docs.djangoproject.com/en/3.2/ref/django-admin/> "django-admin and manage.py"
    
5. Para aplicar los cambios realizados y poder comenzar a trabajar en nuestro proyecto, es necesario hacer uso de el comando **migrations**. De forma general, las migraciones nos permiten *propagar* nuestros cambios (agregados, eliminaciones, etc) dentro de nuestra base de datos. Para realizar nuestra primera migración (y con ello levantar nuestro proyecto), utilizamos la sintaxis:

   > python manage.py migrate

Aparecerá una secuencia de información que terminará con una validación **OK**, de momento no haremos mucho caso a esta información. Realizado esto solo nos queda correr un servidor local en nuestra máquina local.

6. Por defecto Django incluye un servidor *ligero* (no recomendado para proyectos avanzados) y éste corre en el puerto 8000 con la IP **127.0.0.1 por default** (puede cambiarse si así se desea, para efectos prácticos, nosotros no lo cambiaremos).
  Así, para lanzar nuestro servidor, utilizaremos la sintaxis
  
   > python manage.py runserver

Lo que nos permitirá visualizar la página default incluída en el proyecto de Django al introducir en el navegador web de nuestra preferencia la dirección IP que nos proporciona en la terminal, bajo el mensaje:
    
   > Starting development server at http://127.0.0.1:8000/

Con esto finaliza el levantamiento de nuestro proyecto, posteriormente podremos trabajar en el proyecto utilizando el editor de código de nuestra preferencia. Para *tirar* el seridor basta con la secuencia de comandos  **CRTL + BREAK**
