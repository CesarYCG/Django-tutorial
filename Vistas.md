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

