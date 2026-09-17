![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791)

# 📚 BiblioOrg

> Sistema de gestión académica para un instituto bíblico desarrollado con **FastAPI** y **PostgreSQL**.

BiblioOrg es una API REST que permite administrar estudiantes, profesores, asignaturas, inscripciones, calificaciones y pagos mediante una arquitectura limpia y escalable.

---

## 🚀 Tecnologías

- Python 3.13
- FastAPI
- PostgreSQL
- SQLAlchemy
- Git & GitHub
- Pydantic

---

## ✨ Funcionalidades

- 👨‍🎓 Gestión de estudiantes
- 👨‍🏫 Administración de profesores
- 📖 Asignaturas y asignaturas activadas por período
- 📝 Inscripción de estudiantes
- 📊 Registro de calificaciones
- 💳 Control de pagos
- 🔍 Consultas SQL con relaciones entre entidades
- ✅ Validación de datos mediante esquemas

---

## 🗄️ Arquitectura

```text
app/
│
├── routers/        # Endpoints de la API
├── services/       # Lógica de negocio
├── database/       # Conexión a PostgreSQL
├── models/         # Esquemas y modelos
└── utils/          # Utilidades e inspector de BD
```

La aplicación sigue una separación por capas donde los **routers** manejan las peticiones HTTP, los **services** contienen la lógica de negocio y la base de datos se abstrae mediante SQLAlchemy.

---

## 🧩 Modelo de datos

| Entidad | Descripción |
|---------|-------------|
| Estudiantes | Información académica del alumno |
| Profesores | Docentes del instituto |
| Asignaturas | Materias disponibles |
| Asignaturas activadas | Materias abiertas por período |
| Inscripciones | Relación estudiante–materia |
| Calificaciones | Notas obtenidas |
| Pagos | Historial de pagos |

---

## ⚡ Instalación

```bash
git clone https://github.com/tuusuario/BiblioOrg.git

cd BiblioOrg

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

Configura las variables de entorno:

```env
DATABASE_URL=postgresql://usuario:password@localhost:5432/biblioorg
```

Ejecutar el servidor:

```bash
uvicorn app.main:app --reload
```

---

## 📖 Documentación de la API

Una vez iniciado el proyecto:

- Swagger UI → `http://localhost:8000/docs`
- ReDoc → `http://localhost:8000/redoc`

---

## 🎯 Objetivos del proyecto

Este proyecto fue desarrollado para fortalecer habilidades en:

- Diseño de APIs REST
- Arquitectura Backend
- Modelado de bases de datos relacionales
- SQL y PostgreSQL
- Organización de código con FastAPI
- Buenas prácticas de desarrollo

---

## 👨‍💻 Autor

**Manuel Sanchez**

Estudiante de Ingeniería de Software | Backend Developer con Python

- Python
- FastAPI
- PostgreSQL
- SQL
- Git
