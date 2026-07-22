Explicación del primer ejercicio en Java:

1- Importar Scanner:
import java.util.Scanner;
Scanner es una herramienta que permite leer los datos que el usuario escribe con el teclado.

2- Crear la clase
public class DistribucionEquipos
Aquí se crea una clase llamada DistribucionEquipos.

---- El archivo debe guardarse con el mismo nombre:
DistribucionEquipos.java

3 - Método principal
public static void main(String[] args)
Este es el método principal. Java comienza a ejecutar el programa desde aquí.

4 - Crear el objeto Scanner
Crear el objeto Scanner
Creamos una variable llamada teclado, que servirá para leer lo que escriba el usuario.

5 - Declarar las variables
int totalEstudiantes;
int estudiantesPorEquipo;
int equiposCompletos;
int estudiantesRestantes;
Todas son variables de tipo int, porque van a almacenar números enteros
-totalEstudiantes: cantidad total de estudiantes.
-estudiantesPorEquipo: integrantes que tendrá cada equipo.
-equiposCompletos: cantidad de equipos que pueden formarse.
-estudiantesRestantes: estudiantes que quedan sin equipo completo.

6 - Leer los datos
System.out.print("Ingrese la cantidad total de estudiantes: ");
totalEstudiantes = teclado.nextInt();
Primero se muestra un mensaje. Después, nextInt() lee el número entero ingresado.
Lo mismo ocurre con la cantidad de estudiantes por equipo:
System.out.print("Ingrese la cantidad de estudiantes por equipo: ");
estudiantesPorEquipo = teclado.nextInt();

7 - Mostrar los valores ingresados
System.out.println("Cantidad total de estudiantes: " + totalEstudiantes);
El símbolo + permite unir texto con el valor de una variable.

Por ejemplo, si el usuario ingresó 28, se mostrará:
Cantidad total de estudiantes: 28

8 - Calcular los equipos completos
equiposCompletos = totalEstudiantes / estudiantesPorEquipo;

La / realiza una división.
Como las variables son enteras, Java solamente guarda la parte entera del resultado.
Por ejemplo: 28 / 5 = 5
Aunque matemáticamente da 5,6, Java guarda 5, porque solamente pueden formarse cinco equipos completos.

9 - Calcular los estudiantes restantes
estudiantesRestantes = totalEstudiantes % estudiantesPorEquipo;
El símbolo % obtiene el resto de una división.

Por ejemplo: 28 % 5 = 3
Esto significa que se forman cinco equipos de cinco estudiantes y quedan tres estudiantes sin integrar un equipo completo.

Finalmente como print escribimos que cerramos el scanner que como mencione al principio es la herramienta que nos permite ver lo que escribien los usauarios en la variable teclado que ahi es donde se guarda lo que ingresan los usuarios para luego hacer los distintos promedios.