Instalar dependencias
pip install -r requirements.txt
Esto instalará:
Django
Django REST Framework
Simple JWT
Dependencias adicionales necesarias

Levantar el servidor
python manage.py runserver
El servidor correrá por defecto en: http://127.0.0.1:8000/

Uso de la página
Acceder al panel de administración con el usuario admin.
Desde el admin se pueden:
Agregar, editar y eliminar productos.
Gestionar categorías y otros modelos registrados.

El sitio web principal muestra los productos disponibles para los usuarios finales.


Usuario Admin
User: admin
pw: admin

Autenticación
Tipo: JWT (JSON Web Token)
Endpoints:
Autenticación con Postman
Tipo: JWT (JSON Web Token)

Endpoint	/api/token/
Método	POST
Descripción Obtener token (access + refresh)

Crear una nueva request POST → http://127.0.0.1:8000/api/token/

En Body → raw → JSON, agregar:

{
    "username": "admin",
    "password": "1234"
}


Hacer Send → recibirás:

{
    "refresh": "<token_refresh>",
    "access": "<token_access>"
}


Copiar el valor de access para usarlo en el resto de endpoints.

| Endpoint               | Método | Descripción         |
| ---------------------- | ------ | ------------------- |
| `/api/productos/`      | GET    | Listar productos    |
| `/api/productos/<id>/` | GET    | Detalle de producto |
| `/api/productos/`      | POST   | Crear producto      |
| `/api/productos/<id>/` | PUT    | Editar producto     |
| `/api/productos/<id>/` | DELETE | Eliminar producto   |


Cómo usar en Postman

Para cualquier endpoint de la API, ir a la pestaña Headers y agregar:
| Key           | Value                   |
| ------------- | ----------------------- |
| Authorization | Bearer `<access_token>` |

ejemplo:
Crear producto:

Método: POST

URL: http://127.0.0.1:8000/api/productos/

Headers:

Authorization: Bearer <access_token>

Content-Type: application/json

Body → raw JSON:

{
    "nombre": "PlayStation 5",
    "descripcion": "Consola nueva",
    "precio": 1200,
    "stock": 10
}


Listar productos:

Método: GET

URL: http://127.0.0.1:8000/api/productos/

Headers: Authorization: Bearer <access_token>

Editar producto:

Método: PUT

URL: /api/productos/<id>/

Body: JSON actualizado con los campos a modificar

Eliminar producto:

Método: DELETE

URL: /api/productos/<id>/

Header Authorization: Bearer <access_token>

Notas
Todos los endpoints de la API requieren JWT válido.
Respuestas siempre en formato JSON.

Validaciones en el serializer:
precio debe ser positivo
stock ≥ 0