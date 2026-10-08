![Python](https://img.shields.io/badge/Python-3.14%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791)

# BiblioOrg

BiblioOrg es una aplicación de escritorio para consultar el catálogo de una biblioteca y registrar préstamos. El escritorio, construido con PySide6, consume una API FastAPI que consulta y modifica una base de datos PostgreSQL mediante SQLAlchemy.

## Funcionalidades

- Consultar y buscar libros del catálogo.
- Ver los préstamos registrados.
- Registrar préstamos.
- Descontar una unidad del stock al prestar un libro. El préstamo se rechaza si el libro no existe o no tiene stock; el descuento y el alta se realizan en una misma transacción.
- Editar los datos de una persona y las fechas de un préstamo.
- Eliminar un préstamo y reponer una unidad al stock dentro de una misma transacción.
- Consultar el estado de la API y de su conexión con la base de datos.

La lista de lecturas todavía está incompleta.

## Estructura

```text
api/
  app/
    database/   Configuración de PostgreSQL, sesiones e inspección del esquema
    routers/    Endpoints HTTP de FastAPI
    services/   Consultas y operaciones de base de datos
  pyproject.toml
  .env.example
desktop/
  controllers/ Controladores de ventanas y utilidades compartidas
  manager/     Navegación e historial de ventanas
  services/    Cliente HTTP y operaciones CRUD
  ui/          Interfaces Qt y archivos fuente .ui
  main.py      Punto de entrada del escritorio
```

Los routers reciben las solicitudes HTTP y llaman a los servicios. Las reglas de negocio y el acceso a los datos están en `api/app/services/`; la configuración de sesiones se encuentra en `api/app/database/session.py`.

## Requisitos

- Python 3.14 o superior.
- [uv](https://docs.astral.sh/uv/) para instalar y ejecutar las dependencias de cada aplicación.
- PostgreSQL con las tablas `principal` y `prestamos` y las columnas utilizadas por el proyecto.
- Para usar el escritorio sin cambios de configuración, acceso a la API publicada en `https://biblioorg.onrender.com`.

## Configurar y ejecutar la API

En `api/`, crea `.env` usando `.env.example` como referencia y configura la URL PostgreSQL. No compartas ni subas credenciales.

```dotenv
DATABASE_URL=postgresql://usuario:contraseña@host:5432/base_de_datos
```

Desde la carpeta `api/`, instala dependencias e inicia el servidor:

```powershell
uv sync
uv run uvicorn app.main:app --reload
```

La API queda disponible en `http://127.0.0.1:8000`. La documentación interactiva está en `http://127.0.0.1:8000/docs`; la ruta `/get_table/health` comprueba la conexión con la base de datos.

## Ejecutar el escritorio

Desde la carpeta `desktop/`:

```powershell
uv sync
uv run python main.py
```

El cliente HTTP está configurado en `desktop/services/api_client.py`. Por defecto apunta a `https://biblioorg.onrender.com`; para desarrollo local, cambia `API_URL` a `http://127.0.0.1:8000`.

## Endpoints

| Método | Ruta | Función |
|---|---|---|
| `GET` | `/` | Mensaje de estado de la API |
| `GET` | `/get_table/health` | Comprueba la conexión con PostgreSQL |
| `GET` | `/get_table/principal` | Devuelve el catálogo |
| `GET` | `/get_table/prestamos` | Devuelve los préstamos |
| `POST` | `/post_table/prestamos` | Descuenta stock y registra un préstamo |
| `PUT` | `/put_table/prestamos?register_id=<id>` | Actualiza un préstamo |
| `DELETE` | `/delete_table/prestamos/<id>` | Elimina un préstamo y repone el stock |

El alta de préstamo espera un JSON con los campos del registro, incluido `codigo`, que identifica el libro en `principal`. El esquema real de PostgreSQL debe incluir la columna `stock` en esa tabla. Si el libro no existe o no tiene stock, el endpoint responde `409 Conflict` y no crea el préstamo. La eliminación repone el stock; la edición desde el escritorio no permite cambiar el libro asociado.

## Notas de desarrollo

- La API carga `DATABASE_URL` desde `api/.env`.
- `api/.env` está excluido del control de versiones; utiliza `.env.example` como guía.
- La API valida nombres de tablas y columnas inspeccionando el esquema de PostgreSQL.
- Este repositorio no contiene instrucciones de migración de la base de datos: las tablas deben existir antes de iniciar la aplicación.

## Autor

Manuel Sanchez — estudiante de Ingeniería de Software.
