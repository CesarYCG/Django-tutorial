# Vistas 👀
Sabemos de anticipo que cualquier sitio web se puede componer de una o más vistas. Las vistas son (valga la redundancia)
sub-páginas de nuestro proyecto y son accesibles por medio de lo que denominamos **Request** y **Responses**. 

Por ahora entenderemos un **Request** como una petición hecha por el **usuario** hacia nuestro sitio, una solicitud para
obtener una vista de nuestro sitio. Por ejemplo, si nuestro sitio es una página de restaurant y tenemos un botón que nos
conduce a una página del "menú", el usuario nos hará un request de dicha página menú.

Por consiguiente, el **Response** es la respuesta que daremos a la petición del usuario, en este caso será devolviendo
el contenido y formato de la página a la que intenta accesar. 

Para esta introducción, haremos la creación de una primera página que muestre el clásico mensaje "Hola Mundo".

### Creando páginas - Response y Request 🐱‍🐉

Entendamos un **Request** como una petición que hará el usuario para ver una determinada página de nuestro sitio.
Entendamos un **Response** como la vista que nosotros le daremos al usuario, según la Request que éste haga.

De esta manera, podemos sintetizar diciendo, para cada Request, podremos retornar una Response. 🤓

### Creando nuestra primera vista (página) 👁

Para realizar esto crearemos dentro de nuestro directorio (al nivel donde se encuentra el archivo **__init__.py** un archivo
denominado **views.py**

Para poder trabajar con las request y las responses. En el archivo views.py importaremos el módulo Response (con el cual también
podremos hacer uso de las request). Esto se realiza con la sintaxis:

> from django.http import HttpResponse

Y ahora procederemos a realiar nuestra primera vista, por ejemplo, crearemos la vista saludo, el código se dará de la forma:

    from django.http import HttpResponse
  
    def saludo(request): #Aqui se crea la primera vista
        return HttpResponse("Hola mundo, primera vista hecha con Django :D") #Esto es lo que retornaremos por esta peticion
 
Nótese que la creación de la vista se declara como si fuera una función cuyo **parámetro** es el response. La instrucción
**return HttpResponse** será lo que retornará dicha función al ser invocada. Con esto tenemos la creación de nuestra primer
página, pero falta referenciarla (conectarla) para que pueda ser accesible por medio de un URL.

Para realizar esta conexión, se realiza en el archivo **urls.py** de modo que nos colocaremos ahí.

### Agregando la vista a urls.py

Para agregar estas vistas en urls.py, se hace a forma de listas. Para agregar una vista recién creada, tenemos que importarlas.
Para importar nuestra vista de saludo, la importaremos con.

    from Proyecto1.views import saludo #Aqui se está importando la vista saludo
  
Posteriormetne debemos agregarla en forma de lista en *urlpatterns*, que es una variable que lista las vistas. 

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('saludo/', saludo),
    ]

Una vez agregada, con el servidor levantado podemos acceder desde la dirección proporcionada por el servidor y el nombre dado
a la vista, en este caso, le dimos el nombre "saludo", de forma que podremos accesar con:

> http://127.0.0.1:8000/saludo/

Al accesar, veremos algo como: 

![Primera Página con Django](/img/capturaPrimeraVista.PNG)


