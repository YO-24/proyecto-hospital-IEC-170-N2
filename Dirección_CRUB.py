import sqlite3

def conectar_db():
    return sqlite3.connect("Hospital.db")


class Direccion:
    def __init__(self, calle, numero, ciudad, region, codigo_postal, id_paciente=None, id_doctor=None):
        self.calle = calle
        self.numero = numero
        self.ciudad = ciudad
        self.region = region
        self.codigo_postal = codigo_postal
        self.id_paciente = id_paciente
        self.id_doctor = id_doctor

    def agregar_direccion(self):
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO Direccion (calle, numero, ciudad, region, codigo_postal, id_paciente, id_doctor)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (self.calle, self.numero, self.ciudad, self.region, self.codigo_postal, self.id_paciente, self.id_doctor))
        conexion.commit()
        conexion.close()
        print("Dirección agregada correctamente.")

    @staticmethod
    def buscar_direccion(id_direccion):
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Direccion WHERE id_direccion = ?", (id_direccion,))
        direccion = cursor.fetchone()
        conexion.close()
        if direccion:
            print("Dirección encontrada:", direccion)
        else:
            print("No se encontró la dirección.")
        return direccion

    @staticmethod
    def actualizar_direccion(id_direccion, calle=None, numero=None, ciudad=None, region=None, codigo_postal=None):
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE Direccion
            SET calle = COALESCE(?, calle),
                numero = COALESCE(?, numero),
                ciudad = COALESCE(?, ciudad),
                region = COALESCE(?, region),
                codigo_postal = COALESCE(?, codigo_postal)
            WHERE id_direccion = ?
        """, (calle, numero, ciudad, region, codigo_postal, id_direccion))
        conexion.commit()
        conexion.close()
        print("Datos de la dirección actualizados correctamente.")

    @staticmethod
    def eliminar_direccion(id_direccion):
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Direccion WHERE id_direccion = ?", (id_direccion,))
        conexion.commit()
        conexion.close()
        print("Dirección eliminada correctamente.")
        
