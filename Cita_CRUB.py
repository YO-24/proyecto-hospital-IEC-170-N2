import sqlite3

def conectar_db():
    return sqlite3.connect("Hospital.db")


class Cita:
    def __init__(self, fecha, hora, motivo, id_paciente, id_doctor):
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.id_paciente = id_paciente
        self.id_doctor = id_doctor

    def agregar_cita(self):
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO Cita (fecha, hora, motivo, id_paciente, id_doctor)
            VALUES (?, ?, ?, ?, ?)
        """, (self.fecha, self.hora, self.motivo, self.id_paciente, self.id_doctor))
        conexion.commit()
        conexion.close()
        print("Cita agregada correctamente.")

    @staticmethod
    def buscar_cita(id_cita):
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Cita WHERE id_cita = ?", (id_cita,))
        cita = cursor.fetchone()
        conexion.close()
        if cita:
            print("Cita encontrada:", cita)
        else:
            print("No se encontró la cita.")
        return cita

    @staticmethod
    def actualizar_cita(id_cita, fecha=None, hora=None, motivo=None):
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE Cita
            SET fecha = COALESCE(?, fecha),
                hora = COALESCE(?, hora),
                motivo = COALESCE(?, motivo)
            WHERE id_cita = ?
        """, (fecha, hora, motivo, id_cita))
        conexion.commit()
        conexion.close()
        print("Datos de la cita actualizados correctamente.")

    @staticmethod
    def eliminar_cita(id_cita):
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Cita WHERE id_cita = ?", (id_cita,))
        conexion.commit()
        conexion.close()
        print("Cita eliminada correctamente.")

    @staticmethod
    def buscar_citas_por_paciente(id_paciente):
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Cita WHERE id_paciente = ?", (id_paciente,))
        citas = cursor.fetchall()
        conexion.close()
        if citas:
            print(f"Citas del paciente {id_paciente}:")
            for cita in citas:
                print(cita)
        else:
            print("No se encontraron citas para este paciente.")
        return citas



