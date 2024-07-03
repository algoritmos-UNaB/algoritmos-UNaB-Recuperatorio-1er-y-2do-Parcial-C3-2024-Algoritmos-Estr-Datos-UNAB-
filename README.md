# RECUPERATORIO 1ER Y 2do PARCIAL - Algoritmos y Estructuras de datos - MIERCOLES 3 de Julio  - 2024

## Modalidad:

- El parcial estará habilitado para su resolución desde: Miercoles 03/07 @ 18:00hs, hasta: Jueves 27/06 @ 01:45hs. (pueden elegir cuando comenzar el intento)

- Tienen 1 (uno) sólo  intento para resolver la actividad; el tiempo máximo es 4 (cuatro) horas.

- **El tiempo será contabilizado desde el momento que aceptan realizar la actividad en Github Classroom, y cualquier "commit" realizado luego de 4 horas no será aceptado como parte del intento de resolución!!**

- Los resultados sólo será visibles luego de que la actividad cierre.   

<u>NOTA:</u> TODOS LOS EJERCICIOS DEBEN SER REALIZADOS EN UN SOLO ARCHIVO.PY, (EJERCICIO1.PY )O SEA LOS MÉTODOS QUE SE VAN AGREGANDO , DEBEN ESTAR EN SUS CORRESPONDIENTES CLASES EN EL ARCHIVO EJERCICIO1.PY
LOS ARCHIVOS RESTANTES QUEDAN POR SI NECESITAN BORRADORES, PERO SOLO MIRAMOS EL PRIMER ARCHIVO, EN EL CUAL TIENE QUE HABER DECLARADAS LAS CLASES SOLICITADAS SOLO UNA VEZ, POR ENDE ANTE NUEVOS PEDIDOS DE FUNCIONALIDAD SE DEBEN AGREGAR LOS MÉTODOS A LA CLAS ORIGINAL Y RELALIZAR LOS CAMBIOS NECESARIOS PARA QUE FUNCIONE LO ENTERIOR Y LO NUEVO


# Ejercicios:
# Ejercicios
Ejercicio 1)
1.1)
Crear una clase Alumno, está contendrá los datos básicos de un Alumno de la facultad  : nombre, Nro de Alumno,  carrera,  email y fecha de ingreso a la facultad, además de los métodos necesarios para cambiar estos datos. Además el usuario tendrá un método especial para "recibir mensajes" e imprimirlos.
1.2)
- Modelar la clase Materias que contendrá los campos identificador (tipo entero positivo), nombre, descripción, carrera en que se cursa (solo un string)). En el constructor se deben establecer todos estos datos. Crear los métodos necesarios para modificar estos valores. 
1.3)
Ahora Modificar al atributo de clase que hace referencia a "Carrera en que se cursa"
para que ese dato almacenado sea en vez de un único string como se definió en el punto 1.1, una  lista  sea una lista tipo combinación, del año/carrera donde se curse la materia 
1.4)
Agregar a la Clase Materias un método mostrar_info_materia()  que imprima toda la información relacionada con la materia, incluida los años y materias donde se cursa
 1.5)
Explicar brevemente cuál sería el cambio necesario  en la implementación, para poder utilizarla, si la clase Alumno estuviera dentro de un módulo llamado Alumos_Unab.

Ejercicio 2)
2.1 ) Agregar a la clase Alumno atributos y métodos para  Asignar  materias (el método debe llamarse asignar_materias) que permita instanciar y  asignar materias  a una lista de materias a cursar dentro de la clase Alumno. 

2.2 ) Agregar a la clase Alumno un método cursa_materia que reciba el identificador de la materia  y devuelva True o False de acuerdo a si la materia  está o no en la lista del Alumno. Para tal búsqueda, utilizar el método de búsqueda binaria.

2.3 - Agregar a la clase Alumno  un método eliminar materia que reciba el identificador de la materia y elimine las instancias de la materias asignadas en la lista del Alumno.

2.4 )
Agregar a la clase Alumno, una lista de materias aprobados que sólo contenga el identificador (int) de materias aprobadas, en una simple lista
Implementar en la clase Alumno, un método llamado aprobo_materia,  el cual realiza una búsqueda binaria  en la lista antes mencionada. El método devolverá un string  "Materia Aprobada  Por el Alumno" si el identificador recibido por ese método como parámetro está en la lista de materias aprobadas. En caso de no encontrarlo, levantará una excepción con el comando RAISE, indicando "Materia NO Aprobada  Por el Alumno"

Ejercicio 3)
3.1) Modelar la Clase Profesores
Esta clase representará un Profesor, con sus propias variables de instancia : nombre, dni , edad. Solo sus atributos y constructor, sin métodos adicionales 
 
3.2 ) Agregar a la clase Alumno, una lista enlazada que contenga el listado de profesores que el alumno tuvo. 
Para ello crear dos métodos :
 agregar_profesor_unab
 obtener_profesores_unab
instanciar objetos de tipo Profesor y almacenar al menos tres instancia en la lista enlazada. 

3.3) Crear un iterador para la lista enlazada de Alumnos.profesores e imprimir iterando  la edad promedio de los profesores 






Ejercicio 4)
Importar los módulos pickle,  y  Path de pathlib, para crear dos métodos en Alumnos,  guardar_materias() y leer_materias() para almacenar las materias aprobadas que están en alumnos.materias_aprobadas y luego levantar esa info,  e imprimirla sencillo
La serialización se realizará en un supuesto archivo llamado
materias.dat, al cual se accede concatenando el path home  + Documents/archivos/materias.dat para acceder a la ubicación del archivo 
