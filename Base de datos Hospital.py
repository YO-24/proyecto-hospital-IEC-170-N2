import sqlite3

conexion = sqlite3.connect("Hospital.db")
cursor = conexion.cursor()

print("Conectado a la base de datos 'Hospital.db'")


cursor.execute("""
CREATE TABLE IF NOT EXISTS Direccion (
    region TEXT,
    comuna TEXT,
    calle TEXT,
    num_casa TEXT
);
""")

#Paciente
cursor.execute("""
CREATE TABLE IF NOT EXISTS Paciente (
    id_paciente INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    apellido TEXT,
    rut TEXT,
    fecha_nacimiento DATE,
    telefono TEXT,
    historia_clinica TEXT
);
""")

#Doctor
cursor.execute("""
CREATE TABLE IF NOT EXISTS Doctor (
    id_doctor INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    apellido TEXT,
    especialidad TEXT,
    telefono TEXT,
    correo TEXT
);
""")

#Cita
cursor.execute("""
CREATE TABLE IF NOT EXISTS Cita (
    id_cita INTEGER PRIMARY KEY AUTOINCREMENT,
    id_doctor INTEGER,
    id_paciente INTEGER,
    fecha DATE,
    hora TEXT,
    motivo TEXT,
    buscar_historial TEXT,
    diagnostico TEXT,
    historial_medico TEXT,
    FOREIGN KEY (id_doctor) REFERENCES Doctor(id_doctor),
    FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente)
);
""")

#Receta
cursor.execute("""
CREATE TABLE IF NOT EXISTS Receta (
    id_receta INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT,
    id_cita INTEGER,
    medicamento TEXT,
    fecha_emision DATE,
    FOREIGN KEY (id_cita) REFERENCES Cita(id_cita)
);
""")


conexion.commit()
print("Tablas creadas correctamente.")

conexion.close()
print("Conexión finalizada.")
