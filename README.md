# djangorest-challange

La app esta deployada en http://nicog.pythonanywhere.com/ Para poder actuar con esa api se necesitan credenciales. Se las mando por mail para que puedan usarlas.
En caso de clonar la app y se quiere usar el web version tambien deberan usar las mismas credenciales.
En caso de querer probar los endpoints con postman se puede correr en el archivo jwt.py, buscar en el archivo que crea de creds.json el valor de 'access' y con eso se pasa como berer token de postman y ya van a estar autorizados.
los endpoints desarrollados son

/api/productos/                  method['GET'] -> Trae todos los productos.

/api/productos/                  method['POST'] -> Crea un producto.

/api/productos/{pk}/             method['GET'] -> Trae el producto de la key pk.

/api/productos/{pk}/delete       method['DELETE'] -> Elimina el producto de la pk.

/api/productos/{pk}/update       method['PUT'] ->  Updetea el producto con la key {pk} (Se deben ingresar todos los campos.

/api/productos/{pk}/update_stock method['PATCH'] ->  Updetea el stock del producto con la key {pk} (Se deben ingresar {"stock": el numero que quiera}.


/api/orders/                      method ['GET'] -> Trae todas las ordenes.

/api/orders/{pk}/                 method ['GET'] -> Trae la orden de key pk.

/api/orders/                      method ['POST'] -> crea una orden, se puede ingresar o no detalles de ordenes para ingresarlos es { 'orderDetails':[{'cuantity': int,'product':'productPK'}]} (tienen que existir el productoy y debe ser suficiente el stock


/api/orders/{pk}/update/          method ['PUT'] -> Updetea la orden, se debe completar con todos los campos.

/api/orders/{pk}/delete/          method ['DELETE'] -> elimina la orden de key pk.

/api/orderDetail/                 method ['GET'] Trae todas las orderDetail.

/api/orderDetail/                 method ['POST'] -> Crea una ordenDetail.

/api/orderDetail/{pk}             method ['GET'] -> Trae la orden detail de key pk.

/api/orderDetail/{pk}             method ['DELETE'] -> deletea la orderDetail de key pk.

/api/orderDetail/{pk}             method ['PUT'] -> Updetea la ordenDetail, se debe completar con todos los campos.


Hay test cases para probar todos estos endpoints y mas. Todo esta validado por token JWT como se pidio. Se utiliza el ModelViewSet para los endpoints y todo esta 
serializado usando el ModelSerializer.

