1. Crear la clase
public class Ejercicio05 {

Acá estamos creando nuestra clase de Java y la llamamos Ejercicio05.

Si tu archivo se llama:

Ejercicio05.java

la clase debe llamarse exactamente:

Ejercicio05
2. Método principal
public static void main(String[] args) {

Este es el método principal del programa.

Java comienza a ejecutar el código desde acá.

Por ahora podés pensar:

main = lugar donde comienza mi programa.

3. Guardamos el texto
String texto = "PROGRAMACION JAVA";

Creamos una variable llamada:

texto

Su tipo es:

String

String se utiliza para almacenar cadenas de caracteres, es decir, palabras, frases o textos.

Entonces:

String texto = "PROGRAMACION JAVA";

significa:

Crear una variable llamada texto y guardar dentro de ella "PROGRAMACION JAVA".

4. Creamos el contador de vocales
int contadorVocales = 0;

Creamos una variable de tipo entero:

int

que se llama:

contadorVocales

Inicialmente vale:

0

¿Por qué?

Porque todavía no recorrimos ninguna letra, así que todavía no encontramos ninguna vocal.

Cada vez que encontremos una vocal vamos a hacer:

contadorVocales++;

Esto significa:

aumentar el contador en 1.

Por ejemplo:

0
1
2
3
4
...
5. Recorrer el texto

Esta es probablemente la parte más importante del ejercicio:

for (int i = 0; i < texto.length(); i++) {

Usamos un ciclo for porque necesitamos recorrer todos los caracteres del texto.

El for tiene tres partes:

for (int i = 0; i < texto.length(); i++)

Vamos por partes.

Primera parte
int i = 0;

Creamos una variable llamada i que comienza en 0.

Esto es porque las posiciones dentro de un String comienzan desde 0, no desde 1.

Nuestro texto sería aproximadamente:

PROGRAMACION JAVA

Y Java ve las posiciones así:

P  R  O  G  R  A  M  A  C  I  O  N     J  A  V  A
0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16

Fijate que incluso el espacio tiene una posición.

Segunda parte
i < texto.length();

texto.length() nos devuelve la cantidad de caracteres que tiene el texto.

En este caso:

texto.length()

da:

17

Porque "PROGRAMACION JAVA" tiene 17 caracteres contando el espacio.

Entonces el for seguirá funcionando mientras:

i < 17

Es decir, recorrerá las posiciones:

0
1
2
3
...
16
Tercera parte
i++

Significa:

aumentar i en 1 después de cada vuelta.

Por ejemplo:

i = 0
i = 1
i = 2
i = 3
...

De esta manera recorremos el texto una posición a la vez.

6. Obtener cada letra

Dentro del for tenemos:

char letra = texto.charAt(i);

Acá aparece algo nuevo: char.

Un char permite guardar un único carácter.

Por ejemplo:

char letra = 'A';

A diferencia del String, los caracteres se escriben con comillas simples:

'A'

Mientras que los textos se escriben con comillas dobles:

"PROGRAMACION JAVA"
¿Qué hace charAt()?

Esta parte:

texto.charAt(i)

significa:

obtener el carácter que está en la posición i.

Por ejemplo, cuando:

i = 0

Java hace:

texto.charAt(0)

y obtiene:

P

Después:

i = 1

obtiene:

R

Después:

i = 2

obtiene:

O

Y así continúa hasta recorrer todo el texto.

7. Comprobar si la letra es una vocal

Después tenemos:

if (letra == 'A' || letra == 'E' || letra == 'I' || letra == 'O' || letra == 'U') {

El if significa:

Si se cumple esta condición, ejecutar lo que está dentro de las llaves.

Queremos preguntar:

¿La letra actual es A, E, I, O o U?

Por eso tenemos:

letra == 'A'

que significa:

¿la letra es A?

Después:

||

significa O.

Entonces:

letra == 'A' || letra == 'E'

significa:

¿La letra es A o es E?

Al agregar todas:

if (letra == 'A' || letra == 'E' || letra == 'I' || letra == 'O' || letra == 'U')

estamos preguntando:

¿La letra actual es A, E, I, O o U?

8. Aumentar el contador

Si efectivamente encontramos una vocal:

contadorVocales++;

aumentamos el contador en uno.

Es exactamente lo mismo que escribir:

contadorVocales = contadorVocales + 1;

Pero normalmente se escribe de la forma más corta:

contadorVocales++;
9. ¿Qué ocurre realmente durante el recorrido?

El programa va haciendo algo parecido a esto:

P → no es vocal → contador = 0

R → no es vocal → contador = 0

O → es vocal → contador = 1

G → no es vocal → contador = 1

R → no es vocal → contador = 1

A → es vocal → contador = 2

M → no es vocal → contador = 2

A → es vocal → contador = 3

C → no es vocal → contador = 3

I → es vocal → contador = 4

O → es vocal → contador = 5

N → no es vocal → contador = 5

espacio → no es vocal → contador = 5

J → no es vocal → contador = 5

A → es vocal → contador = 6

V → no es vocal → contador = 6

A → es vocal → contador = 7

Por eso finalmente tenemos:

7 vocales
10. Mostrar el texto
System.out.println("Texto analizado: " + texto);

Esto muestra:

Texto analizado: PROGRAMACION JAVA

El símbolo:

+

en este caso sirve para unir texto con una variable.

11. Mostrar la cantidad de caracteres
System.out.println("Cantidad total de caracteres: " + texto.length());

Nuevamente usamos:

texto.length()

para conocer cuántos caracteres tiene el String.

El resultado es:

17

Importante: el espacio entre PROGRAMACION y JAVA también cuenta como carácter.

12. Mostrar la cantidad de vocales

Finalmente:

System.out.println("Cantidad de vocales: " + contadorVocales);

Como el contador terminó valiendo 7, aparecerá:

Cantidad de vocales: 7