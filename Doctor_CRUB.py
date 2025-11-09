import sqlite3

def conectar_db():
    return sqlite3.connect("Hospital.db")

class Doctor:
    def __init__(self, nombre, apellido, especialidad, telefono, email):
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.telefono = telefono
        self.email = email 

    def agregar_doctor(self):
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO Doctor (nombre, apellido, especialidad, telefono, email)
            VALUES (?, ?, ?, ?, ?)
        """, (self.nombre, self.apellido, self.especialidad, self.telefono, self.email))
        conexion.commit()
        conexion.close()
        print("Doctor agregado correctamente.") 

    @staticmethod
    def buscar_doctor(id_doctor):
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Doctor WHERE id_doctor = ?", (id_doctor,))
        doctor = cursor.fetchone()
        conexion.close()
        if doctor:
            print("Doctor encontrado:", doctor)
        else:
            print("No se encontró al doctor.")
        return doctor

    @staticmethod
    def actualizar_doctor(id_doctor, telefono=None, email=None, especialidad=None):
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE Doctor
            SET telefono = COALESCE(?, telefono),
                email = COALESCE(?, email),
                especialidad = COALESCE(?, especialidad)
            WHERE id_doctor = ?
        """, (telefono, email, especialidad, id_doctor))
        conexion.commit()
        conexion.close()
        print("Datos del doctor actualizados correctamente.")

    @staticmethod
    def eliminar_doctor(id_doctor):
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Doctor WHERE id_doctor = ?", (id_doctor,))
        conexion.commit()
        conexion.close()
        print("Doctor eliminado correctamente.")


