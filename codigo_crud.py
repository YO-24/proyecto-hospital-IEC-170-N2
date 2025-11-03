import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hospital_db"
    )

# ------------------ PACIENTE ------------------
class Paciente:
    def __init__(self, nombre, apellido, rut, fecha_nacimiento, telefono, historia_clinica):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono
        self.historia_clinica = historia_clinica

    def crear(self):
        conexion = conectar()
        cursor = conexion.cursor()
        try:
            cursor.execute("""
                INSERT INTO Paciente (nombre, apellido, rut, fecha_nacimiento, telefono, historia_clinica)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (self.nombre, self.apellido, self.rut, self.fecha_nacimiento, self.telefono, self.historia_clinica))
            conexion.commit()
            print(" Paciente creado correctamente.")
        except mysql.connector.IntegrityError:
            print(" Ya existe un paciente con ese RUT.")
        finally:
            conexion.close()


# ------------------ DOCTOR ------------------
class Doctor:
    def __init__(self, nombre, apellido, especialidad, telefono, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.telefono = telefono
        self.correo = correo

    def crear(self):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO Doctor (nombre, apellido, especialidad, telefono, email)
            VALUES (%s, %s, %s, %s, %s)
        """, (self.nombre, self.apellido, self.especialidad, self.telefono, self.correo))
        conexion.commit()
        conexion.close()
        print(" Doctor agregado correctamente.")


# ------------------ CITA ------------------
class Cita:
    def __init__(self, id_doctor, id_paciente, fecha, hora, motivo):
        self.id_doctor = id_doctor
        self.id_paciente = id_paciente
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo

    def crear(self):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO Cita (id_doctor, id_paciente, fecha, hora, motivo)
            VALUES (%s, %s, %s, %s, %s)
        """, (self.id_doctor, self.id_paciente, self.fecha, self.hora, self.motivo))
        conexion.commit()
        conexion.close()
        print(" Cita registrada correctamente.")


# ------------------ RECETA ------------------
class Receta:
    def __init__(self, indicaciones, id_cita, fecha_emision):
        self.indicaciones = indicaciones
        self.id_cita = id_cita
        self.fecha_emision = fecha_emision

    def crear(self):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO Receta (id_cita, indicaciones, fecha_emision)
            VALUES (%s, %s, %s)
        """, (self.id_cita, self.indicaciones, self.fecha_emision))
        conexion.commit()
        conexion.close()
        print(" Receta creada correctamente.")


# ------------------ EJEMPLOS DE PRUEBA ------------------
if __name__ == "__main__":
    # Crear un paciente
    p1 = Paciente("Roberto", "Lopez", "18.256.610-k", "1999-03-14", "987623321", "cáncer de piel")
    p1.crear()

    # Crear un doctor
    d1 = Doctor("María", "Sánchez", "Dermatóloga", "912345678", "maria.sanchez@hospital.cl")
    d1.crear()

    # Crear una cita (id_paciente=1, id_doctor=1 deben existir)
    c1 = Cita(1, 1, "2025-11-04", "10:30:00", "Control de piel")
    c1.crear()

    # Crear una receta asociada a la cita
    r1 = Receta("Aplicar crema 2 veces al día", 1, "2025-11-04")
    r1.crear()
