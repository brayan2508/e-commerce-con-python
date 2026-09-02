## APi REST de comercio y gestion de ordenes 

API REST de alto rendimiento, escalable y robusta para la gestion de un e-commerce y procesamiento de ordenes de compra.

## Tecnologias Utilizadas 

- **Lenguaje:** Python 3.10+ 
- **Framework Web:** FastAPI
- **ORM / Esquemas:** SQLModel
- **Migraciones de Base de Datos:** Alembic
- **Servidor ASGI:** Uvicorn
- **Base de Datos (Desarrollo):** SQLite

---

## Estructura del proyecto 

``` text
ecommerce_api/
├── app/
├   ├── api/            # Endpoints y rutas agrupadas por modulo 
├   ├── core/           # Configuracion global, seguridad y variables de entorno
├   ├── db/             # Conexion a la base de datos y sesion de SQLModel
├   ├── models/         # Modelos de SQLModel (User, Products, Order, OrderItem)
├   ├── schemas/         # Esquemas DTO de pydantic para entrada y salida
├   ├── main.py         # punto de entrada de la aplicacion FastAPI 
├── .gitignore          # Archivo de exclusion del proyecto 
├── README.md           # documentacion del proyecto 
└── requirements.txt    # Lista de dependencias del proyecto 
```


## Entidades y modelos de datos.

* User: Gestion de usuarios (clientes administradores) con autenticacion. 
* Product: Catalago de productos con inventario, precio y descripcion.
* ORder: Registro general de compras y seguimiento de estados.
* OrderItem: tabla pivote para guardar el desglose de productos y el precio historico unitario al momento de la compra.

##  Guia de instalacion y ejecucion Local 

1. Clonar el repositorio 
```
git clone https://github.com/brayan2508/e-commerce-con-python.git
cd ecommerce-con-python
```
2. Crear y activar el entorno virtual

- En windows 
```
py -m venv venv 
venv\\Scripts\\activate

```
- EN Linux / macOS
```
python3 -m venv venv 
source venv/bin/activate
```

3. Instalar las dependencias
```
pip install -r requirements.txt 
```
4. Ejecutar la API
```
uvicorn app.main:app --reload
```
## Documentacion Interactiva (Swagger / OpenAPI)

Una vez iniciado el servidor accede a la interfaz interactiva para probar los endpoints sin necesidad de un frontend:
* Swagger UI: http://127.0.0.1:8000/docs

## Referencias de documentacion

FastAPI (framework)
- https://fastapi.tiangolo.com/es/tutorial/first-steps/

ALEmbic
- https://alembic-sqlalchemy-org.translate.goog/en/latest/tutorial.html?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc

Python
- https://docs.python.org/3/

SQLModel
- https://sqlmodel.tiangolo.com
