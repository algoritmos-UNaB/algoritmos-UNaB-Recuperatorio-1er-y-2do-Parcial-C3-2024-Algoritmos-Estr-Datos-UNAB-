# 2do-Parcial-C6-2024-Algoritmos-Estr-Datos-UNAB

## Modalidad

Tienen 1 (uno) sólo intento para resolver la actividad; el tiempo máximo es 4 (cuatro) horas.

El tiempo será contabilizado desde el momento que aceptan realizar la actividad en Github Classroom, y cualquier "commit" realizado luego de 4 horas no será aceptado como parte del intento de resolución!!

# Ejercicios

## Ejercicio 1

1.1 - Crear una clase Comprador, que contenga los datos básicos de una persona: nombre, dirección, teléfono, fecha de nacimiento y un campo *puntaje* que dependerá de las compras que realice. En el constructor, se deben inicializar todos los campos, y por defecto, el valor de puntaje será 0 (cero). Implementar los métodos para sumar o restar puntos del puntaje del comprador.

1.2 - Crear una clase Articulos que contenga los campos identificador (tipo entero positivo), nombre, descripcion, marca, precio (float) y puntos. En el constructor se deben establecer todos estos datos. Crear los métodos necesarios para modificar estos valores. IMPORTANTE: los puntos no pueden ser negativos.

## Ejercicio 2

2.1 - Agregar a la clase Comprador un método *comprar_artículo* que permita adquirir Articulos y agregarlos a una lista (privada) de artículos comprados. Al comprarlos, los puntos del artículo se suman a los puntos del Comprador. 

2.2 - Agregar a la clase Comprador un método *encontrar_articulo* que reciba el identificador del artículo y devuelva True o False de acuerdo a si el artículo está o no en la lista del comprador. Utilizar el método de **búsqueda lineal**.

2.3 - Agregar a la clase Comprador un método *eliminar artículo* que reciba el identificador del artículo y elimine **TODAS** las instancias del artículo en la lista del comprador. En cada ocasión, deben eliminarse los puntos correspondientes al artículo del puntaje del Comprador.

## Ejercicio 3

3.1 - Crear seis instancias de compradores, y agregarles (mediante el método *comprar artículos*) diferentes cantidades de artículos. Nota: crear las instancias necesarias de artículos diferentes.

3.2 - Crear una lista con estos compradores.

3.3 - Utilizar el método de **ordenamiento burbuja** para ordenarlos de forma **DESCENDENTE** (de mayor valor a menor valor) de acuerdo al puntaje de cada uno.

3.3 - Crear una lista enlazada de todos los artículos creados en el punto 3.1, y escribir una función que pueda procesar esta lista y determinar (devolviendo un valor booleano) si existen dos artículos con la misma cantidad de puntos.

## Ejercicio 4

4.1 - Agregar a la clase Comprador un método *lista_a_string* que devuelva una lista de strings con los atributos de los artículos comprados [identificador, nombre, marca, precio, puntos] separados por puntos y comas (ej: ['1; "computadora"; "dell"; 100.00; 30', '5; "mouse"; "logitech"; 200.00; 15'])

4.2 - Escribir una función que reciba la lista de compradores creada en el punto 3.2 y genere archivos de texto con extensión .csv cuyo nombre sea el nombre del comprador y que contengan la lista de artículos correspondiente, un artículo en cada línea.
