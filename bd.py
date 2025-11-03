import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = conexion.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS hospital_db")
conexion.commit()
print(" Base de datos 'hospital_db' creada correctamente.")
conexion.close()
