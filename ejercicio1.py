#Ejercicio 1.1
class Alumno:
    def __init__(self, nombre, nro_alumno, carrera, email, fecha_ingreso):
        self.nombre = nombre
        self.nro_alumno = nro_alumno
        self.carrera = carrera
        self.email = email
        self.fecha_ingreso = fecha_ingreso
        self.mensajes = []

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def cambiar_nro_alumno(self, nuevo_nro_alumno):
        self.nro_alumno = nuevo_nro_alumno

    def cambiar_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera

    def cambiar_email(self, nuevo_email):
        self.email = nuevo_email

    def cambiar_fecha_ingreso(self, nueva_fecha_ingreso):
        self.fecha_ingreso = nueva_fecha_ingreso

    def recibir_mensaje(self, mensaje):
        self.mensajes.append(mensaje)
        print(mensaje)

#Ejercicio 1.2
class Materias:
    def __init__(self, identificador, nombre, descripcion, carrera):
        self.identificador = identificador
        self.nombre = nombre
        self.descripcion = descripcion
        self.carrera = carrera

    def cambiar_identificador(self, nuevo_identificador):
        self.identificador = nuevo_identificador

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def cambiar_descripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion

    def cambiar_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera
#Ejercicio 1.3
class Materias:
    def __init__(self, identificador, nombre, descripcion, carrera_anio):
        self.identificador = identificador
        self.nombre = nombre
        self.descripcion = descripcion
        self.carrera_anio = carrera_anio

    def cambiar_identificador(self, nuevo_identificador):
        self.identificador = nuevo_identificador

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def cambiar_descripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion

    def cambiar_carrera_anio(self, nueva_carrera_anio):
        self.carrera_anio = nueva_carrera_anio
#Ejercicio 1.4
class Materias:
    def __init__(self, identificador, nombre, descripcion, carrera_anio):
        self.identificador = identificador
        self.nombre = nombre
        self.descripcion = descripcion
        self.carrera_anio = carrera_anio

    def cambiar_identificador(self, nuevo_identificador):
        self.identificador = nuevo_identificador

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def cambiar_descripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion

    def cambiar_carrera_anio(self, nueva_carrera_anio):
        self.carrera_anio = nueva_carrera_anio

    def mostrar_info_materia(self):
        print(f"ID: {self.identificador}")
        print(f"Nombre: {self.nombre}")
        print(f"Descripción: {self.descripcion}")
        print(f"Carrera y año: {self.carrera_anio}")
#Ejercicio 1.5
#para utilizar la clase Alumno dentro de un módulo llamado Alumnos_Unab, se debería importar la clase desde el módulo en los archivos donde se desee utilizar. Por ejemplo:
# from Alumnos_Unab import Alumno
