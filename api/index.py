import os
from fastapi import FastAPI
import mysql.connector

app = FastAPI()

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "instancia-mysql.ctjm6xph3sme.us-east-1.rds.amazonaws.com"),
        user=os.getenv("DB_USER", "admin"),
        password=os.getenv("DB_PASSWORD", "tu_contraseña"),
        database=os.getenv("DB_NAME", "directorio_contactos"),
        port=3306
    )

@app.get("/")
def root():
    return {"mensaje": "API corriendo en Vercel"}

@app.get("/contactos")
def get_contactos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM contactos;")
    contactos = cursor.fetchall()
    cursor.close()
    conn.close()
    return contactos