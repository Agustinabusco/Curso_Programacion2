Explicación paso a paso
1. Importar la clase Random
import java.util.Random;

Esta línea permite utilizar la clase Random, que sirve para generar números al azar.

Java tiene muchas herramientas organizadas en paquetes. La clase Random se encuentra dentro del paquete:

java.util

Por eso tenemos que importarla antes de utilizarla.

2. Declarar la clase
public class SumaNumerosImpares {

Aquí se crea la clase principal del programa.

El nombre de la clase es:

SumaNumerosImpares

Por lo tanto, el archivo debe guardarse con el mismo nombre:

SumaNumerosImpares.java

Java distingue entre mayúsculas y minúsculas, así que el nombre debe escribirse exactamente igual.

3. Método principal
public static void main(String[] args) {

Este es el método principal del programa. Java comienza a ejecutar las instrucciones que se encuentran dentro de este método.

Podemos interpretarlo así:

public: permite que Java acceda al método.
static: permite ejecutar el método sin crear un objeto de la clase.
void: indica que el método no devuelve ningún resultado.
main: es el nombre especial que identifica el comienzo del programa.
String[] args: permite recibir información desde la consola, aunque en este ejercicio no la utilizamos.
4. Crear el generador de números aleatorios
Random aleatorio = new Random();

Aquí se crea un objeto de la clase Random.

El nombre que le damos al objeto es:

aleatorio

Después utilizaremos ese objeto para generar los números.

Podría haberse llamado de otra manera, por ejemplo:

Random generador = new Random();

Pero aleatorio ayuda a comprender para qué sirve.

5. Declarar la variable numero
int numero;

Esta variable almacenará cada número generado al azar.

Es de tipo int porque guardará números enteros.

Por ejemplo, durante una repetición puede contener:

7

En la siguiente repetición puede contener:

2

La variable va cambiando su valor cada vez que se genera un nuevo número.

6. Crear la variable acumuladora
int sumaImpares = 0;

Esta variable se encarga de almacenar la suma de todos los números impares generados.

Se llama acumuladora porque va acumulando valores.

Comienza en cero porque todavía no se generó ningún número impar.

Por ejemplo, si se generan los impares 3, 7 y 5, la variable irá cambiando así:

Inicio: 0
Después de generar 3: 3
Después de generar 7: 10
Después de generar 5: 15

Es muy importante inicializarla en cero. Si no lo hacemos, Java no permitirá utilizarla correctamente.

La estructura repetitiva
7. Comienzo del do-while
do {

La estructura do-while permite repetir un conjunto de instrucciones.

Su funcionamiento general es:

do {
    instrucciones;
} while (condicion);

Primero ejecuta las instrucciones y después revisa la condición.

Esto es adecuado para el ejercicio porque necesitamos generar al menos un número antes de comprobar si la suma superó 25.

8. Generar un número entre 0 y 10
numero = aleatorio.nextInt(11);

Esta línea genera un número entero al azar.

El método:

nextInt(11)

genera números desde 0 hasta 10.

Esto sucede porque el número colocado entre paréntesis no se incluye.

Por lo tanto:

nextInt(11)

puede generar:

0, 1, 2, 3, 4, 5, 6, 7, 8, 9 o 10

Pero no puede generar 11.

Una forma de recordarlo es:

nextInt(límite)

genera números desde cero hasta uno menos que el límite.

Por ejemplo:

nextInt(5);

genera:

0, 1, 2, 3 o 4
9. Mostrar el número generado
System.out.println("Número generado: " + numero);

Esta instrucción muestra en pantalla el número generado.

El símbolo + se utiliza para unir el texto con el contenido de la variable.

Por ejemplo, si numero contiene 8, se mostrará:

Número generado: 8
Determinar si el número es par o impar
10. La condición if
if (numero % 2 == 0) {

Esta condición comprueba si el número es par.

El operador % calcula el resto de una división.

Por ejemplo:

8 % 2 = 0
7 % 2 = 1
10 % 2 = 0
5 % 2 = 1

Un número es par cuando al dividirlo entre 2 el resto es cero.

Por eso usamos:

numero % 2 == 0

Es importante diferenciar:

= asigna un valor.
== compara dos valores.

Aquí estamos comparando si el resto es igual a cero, por eso utilizamos dos signos de igualdad.

11. Mostrar que el número es par
System.out.println("El número es par.");

Esta instrucción se ejecuta solamente si la condición anterior es verdadera.

Por ejemplo, si se genera 6, Java comprueba:

6 % 2 = 0

Como el resto es cero, muestra:

El número es par.

El número 0 también se considera par, porque:

0 % 2 = 0

Los números pares no se suman a la variable acumuladora.

12. El bloque else
} else {

El bloque else se ejecuta cuando la condición del if es falsa.

Es decir, se ejecuta cuando el resto de dividir el número entre 2 no es cero.

En este ejercicio eso significa que el número es impar.

13. Mostrar que el número es impar
System.out.println("El número es impar.");

Si el número generado es impar, el programa muestra este mensaje.

Por ejemplo, si se genera 9, muestra:

El número es impar.
14. Acumular el número impar
sumaImpares = sumaImpares + numero;

Esta línea suma el número impar generado al valor que ya se encontraba almacenado en sumaImpares.

Supongamos que:

sumaImpares = 12
numero = 7

La operación será:

sumaImpares = 12 + 7

Entonces, el nuevo valor será:

sumaImpares = 19

También se puede escribir de forma abreviada:

sumaImpares += numero;

Las dos formas hacen exactamente lo mismo.

Para comenzar, la forma más extensa puede ser más sencilla de comprender:

sumaImpares = sumaImpares + numero;
15. Mostrar la suma acumulada
System.out.println("Suma acumulada de impares: " + sumaImpares);

Cada vez que se genera un número impar, el programa muestra cuánto se lleva acumulado.

Por ejemplo:

Número generado: 7
El número es impar.
Suma acumulada de impares: 19

Esta línea está dentro del bloque else, por lo que solamente se muestra cuando el número es impar.

Si el número es par, la suma no cambia.

16. Separador visual
System.out.println("-------------------------");

Esta línea no modifica el funcionamiento del programa.

Solamente imprime una línea para separar cada número generado y hacer que la salida sea más fácil de leer.

Condición para continuar
17. El while del ciclo
} while (sumaImpares <= 25);

Esta es la condición que controla la repetición.

El programa continuará generando números mientras:

sumaImpares sea menor o igual que 25

El operador <= significa:

menor o igual

Por ejemplo:

Si la suma es 18, continúa.
Si la suma es 25, continúa.
Si la suma es 26, se detiene.
Si la suma es 31, se detiene.

Esto respeta la consigna, porque el programa debe detenerse inmediatamente después de que la suma supere 25.

Es importante colocar:

sumaImpares <= 25

y no:

sumaImpares < 25

La consigna dice que el proceso continúa mientras la suma sea menor o igual que 25. Por eso, si la suma llega exactamente a 25, todavía debe generar otro número.

Finalización del programa
18. Mostrar que la suma superó 25
System.out.println("La suma de los números impares superó 25.");

Cuando el ciclo termina, sabemos que la suma es mayor que 25.

Por eso se muestra este mensaje.

19. Mostrar la suma final
System.out.println("Suma total de los números impares: " + sumaImpares);

Esta línea muestra el resultado final acumulado.

La suma no tiene por qué ser exactamente 26. Puede superar 25 con diferentes valores.

Por ejemplo, podría terminar en:

27

o:

31

o:

35

Eso depende de los números aleatorios generados.