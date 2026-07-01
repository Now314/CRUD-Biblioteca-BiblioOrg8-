from sqlalchemy import text
from app.database.session import SessionLocal


def get_version():

    db = SessionLocal()
    try:
        version = db.execute(text("SELECT version()"))
        return {"database_version": version.scalar()}
    finally:
        db.close()

def get_time():
    db = SessionLocal()
    try:
        time = db.execute(text("SELECT now()"))
        return {"time": time.scalar()}
    finally:
        db.close()

def get_principal():
    db = SessionLocal()
    try:
        table = db.execute(text("SELECT * from principal LIMIT 5"))
        counted_rows = db.execute(text("SELECT COUNT(*) FROM principal;"))
        return table.mappings().all(), counted_rows.scalar()
    finally:
        db.close()