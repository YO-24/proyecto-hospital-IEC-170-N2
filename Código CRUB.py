import sqlite3

def conectar():
    return sqlite3.connect("Hospital.db")

#Clase Direccion 
class Direccion:
    def __init__(self, region, comuna, calle, num_casa):
        self.region = region
        self.comuna = comuna
        self.calle = calle
        self.num_casa = num_casa

    def crear(self):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO Direccion (region, comuna, calle, num_casa) VALUES (?, ?, ?, ?)",
            (self.region, self.comuna, self.calle, self.num_casa)
        )
        conexion.commit()
        conexion.close()

    @staticmethod
    def listar():
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Direccion")
        direcciones = cursor.fetchall()
        conexion.close()
        return direcciones

    @staticmethod
    def actualizar(id_direccion, nueva_calle, nuevo_numero):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE Direccion SET calle = ?, num_casa = ? WHERE rowid = ?",
            (nueva_calle, nuevo_numero, id_direccion)
        )
        conexion.commit()
        conexion.close()

    @staticmethod
    def eliminar(id_direccion):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Direccion WHERE rowid = ?", (id_direccion,))
        conexion.commit()
        conexion.close()

#Clase Paciente
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
        cursor.execute("INSERT INTO Paciente (nombre, apellido, rut, fecha_nacimiento, telefono, historia_clinica) VALUES (?, ?, ?, ?, ?, ?)",
                       (self.nombre, self.apellido, self.rut, self.fecha_nacimiento, self.telefono, self.historia_clinica))
        conexion.commit()
        conexion.close()

    @staticmethod
    def listar():
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Paciente")
        pacientes = cursor.fetchall()
        conexion.close()
        return pacientes

    @staticmethod
    def actualizar(id_paciente, telefono):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("UPDATE Paciente SET telefono = ? WHERE id_paciente = ?", (telefono, id_paciente))
        conexion.commit()
        conexion.close()

    @staticmethod
    def eliminar(id_paciente):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Paciente WHERE id_paciente = ?", (id_paciente,))
        conexion.commit()
        conexion.close()

#Clase Doctor
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
        cursor.execute("INSERT INTO Doctor (nombre, apellido, especialidad, telefono, correo) VALUES (?, ?, ?, ?, ?)",
                       (self.nombre, self.apellido, self.especialidad, self.telefono, self.correo))
        conexion.commit()
        conexion.close()

    @staticmethod
    def listar():
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Doctor")
        doctores = cursor.fetchall()
        conexion.close()
        return doctores

#Clase cita
class Cita:
    def __init__(self, id_doctor, id_paciente, fecha, hora, motivo, diagnostico):
        self.id_doctor = id_doctor
        self.id_paciente = id_paciente
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.diagnostico = diagnostico

    def crear(self):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("""
        INSERT INTO Cita (id_doctor, id_paciente, fecha, hora, motivo, diagnostico)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (self.id_doctor, self.id_paciente, self.fecha, self.hora, self.motivo, self.diagnostico))
        conexion.commit()
        conexion.close()

    @staticmethod
    def listar():
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("""
        SELECT Cita.id_cita, Paciente.nombre, Doctor.nombre, Cita.fecha, Cita.hora, Cita.motivo
        FROM Cita
        JOIN Paciente ON Cita.id_paciente = Paciente.id_paciente
        JOIN Doctor ON Cita.id_doctor = Doctor.id_doctor
        """)
        citas = cursor.fetchall()
        conexion.close()
        return citas

#Clase Receta
class Receta:
    def __init__(self, descripcion, id_cita, medicamento, fecha_emision):
        self.descripcion = descripcion
        self.id_cita = id_cita
        self.medicamento = medicamento
        self.fecha_emision = fecha_emision

    def crear(self):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO Receta (descripcion, id_cita, medicamento, fecha_emision) VALUES (?, ?, ?, ?)",
                       (self.descripcion, self.id_cita, self.medicamento, self.fecha_emision))
        conexion.commit()
        conexion.close()

    @staticmethod
    def listar():
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("""
        SELECT Receta.id_receta, Cita.id_cita, Receta.medicamento, Receta.fecha_emision
        FROM Receta
        JOIN Cita ON Receta.id_cita = Cita.id_cita
        """)
        recetas = cursor.fetchall()
        conexion.close()
        return recetas

#Ejemplo de prueba de conexión 
if __name__ == "__main__":
   
    # Crear un paciente 
    p1 = Paciente("Juan", "Pérez", "12.345.678-9", "1990-03-12", "987654321", "Asma")
    p1.crear()
    print("Paciente creado correctamente.")

    # Listar pacientes
    for p in Paciente.listar():
        print(p)


    
