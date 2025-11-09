import sqlite3

def conectar_db():
    return sqlite3.connect("Hospital.db")


class Receta:
    def __init__(self, fecha, medicamentos, indicaciones, id_paciente, id_doctor, id_cita=None):
        self.fecha = fecha
        self.medicamentos = medicamentos
        self.indicaciones = indicaciones
        self.id_paciente = id_paciente
        self.id_doctor = id_doctor
        self.id_cita = id_cita

    def agregar_receta(self):
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO Receta (fecha, medicamentos, indicaciones, id_paciente, id_doctor, id_cita)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (self.fecha, self.medicamentos, self.indicaciones, self.id_paciente, self.id_doctor, self.id_cita))
        conexion.commit()
        conexion.close()
        print("Receta agregada correctamente.")

    @staticmethod
    def buscar_receta(id_receta):
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Receta WHERE id_receta = ?", (id_receta,))
        receta = cursor.fetchone()
        conexion.close()
        if receta:
            print("Receta encontrada:", receta)
        else:
            print("No se encontró la receta.")
        return receta

    @staticmethod
    def actualizar_receta(id_receta, medicamentos=None, indicaciones=None, fecha=None):
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE Receta
            SET medicamentos = COALESCE(?, medicamentos),
                indicaciones = COALESCE(?, indicaciones),
                fecha = COALESCE(?, fecha)
            WHERE id_receta = ?
        """, (medicamentos, indicaciones, fecha, id_receta))
        conexion.commit()
        conexion.close()
        print("Datos de la receta actualizados correctamente.")

    @staticmethod
    def eliminar_receta(id_receta):
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Receta WHERE id_receta = ?", (id_receta,))
        conexion.commit()
        conexion.close()
        print("Receta eliminada correctamente.")

