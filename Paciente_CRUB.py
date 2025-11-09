import sqlite3

def conectar_db():
    return sqlite3.connect("Hospital.db")

class Paciente:
    def __init__(self, nombre, apellido, fecha_nacimiento, telefono, email, historia_clinica):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono
        self.email = email
        self.historia_clinica = historia_clinica

    def agregar_paciente(self):
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO Paciente (nombre, apellido, fecha_nacimiento, telefono, email, historia_clinica)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (self.nombre, self.apellido, self.fecha_nacimiento, self.telefono, self.email, self.historia_clinica))
        conexion.commit()
        conexion.close()
        print("Paciente agregado correctamente.")

    @staticmethod
    def buscar_paciente(id_paciente):
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Paciente WHERE id_paciente = ?", (id_paciente,))
        paciente = cursor.fetchone()
        conexion.close()
        if paciente:
            print("Paciente encontrado:", paciente)
        else:
            print("No se encontró al paciente.")
        return paciente

    @staticmethod
    def actualizar_paciente(id_paciente, telefono=None, email=None, historia_clinica=None):
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE Paciente 
            SET telefono = COALESCE(?, telefono), 
                email = COALESCE(?, email), 
                historia_clinica = COALESCE(?, historia_clinica)
            WHERE id_paciente = ?
        """, (telefono, email, historia_clinica, id_paciente))
        conexion.commit()
        conexion.close()
        print("Datos del paciente actualizados correctamente.")

    @staticmethod
    def eliminar_paciente(id_paciente):
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Paciente WHERE id_paciente = ?", (id_paciente,))
        conexion.commit()
        conexion.close()
        print("Paciente eliminado correctamente.")


