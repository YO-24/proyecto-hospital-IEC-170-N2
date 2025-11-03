import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hospital_db"
)

cursor = conexion.cursor()

tablas = [
    
    CREATE TABLE IF NOT EXISTS Paciente (
        id_paciente INT AUTO_INCREMENT PRIMARY KEY,
        rut VARCHAR(15) UNIQUE NOT NULL,
        nombre VARCHAR(50) NOT NULL,
        apellido VARCHAR(50) NOT NULL,
        fecha_nacimiento DATE,
        direccion VARCHAR(100),
        telefono VARCHAR(15),
        historia_clinica TEXT
    )
    ,
    
    CREATE TABLE IF NOT EXISTS Doctor (
        id_doctor INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL,
        apellido VARCHAR(50) NOT NULL,
        especialidad VARCHAR(50) NOT NULL,
        telefono VARCHAR(15),
        email VARCHAR(100)
    )
    ,

    CREATE TABLE IF NOT EXISTS Cita (
        id_cita INT AUTO_INCREMENT PRIMARY KEY,
        fecha DATE NOT NULL,
        hora TIME NOT NULL,
        motivo VARCHAR(100),
        id_paciente INT NOT NULL,
        id_doctor INT NOT NULL,
        FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente)
            ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (id_doctor) REFERENCES Doctor(id_doctor)
            ON DELETE CASCADE ON UPDATE CASCADE
    )
    ,
    CREATE TABLE IF NOT EXISTS Receta (
        id_receta INT AUTO_INCREMENT PRIMARY KEY,
        id_cita INT NOT NULL,
        indicaciones TEXT,
        fecha_emision DATE DEFAULT (CURRENT_DATE),
        FOREIGN KEY (id_cita) REFERENCES Cita(id_cita)
            ON DELETE CASCADE ON UPDATE CASCADE
    )
]

for sql in tablas:
    cursor.execute(sql)

conexion.commit()
conexion.close()
print(" Tablas creadas correctamente en hospital_db.")
