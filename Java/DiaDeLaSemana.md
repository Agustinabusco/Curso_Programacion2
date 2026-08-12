1. Importar Random
import java.util.Random;

Esta línea le dice a Java:

"Voy a utilizar una herramienta llamada Random."

Random sirve para generar números aleatorios.

Por ejemplo, gracias a Random, podemos hacer que el programa genere:

3, después 6, después 1, después 7, etc.

Sin esta línea, Java no reconocería qué es Random.

2. Crear la clase
public class DiaDeLaSemana {

En Java, prácticamente todo nuestro programa tiene que estar dentro de una clase.

En este caso la clase se llama:

DiaDeLaSemana

Si guardás este código en un archivo, normalmente el archivo debería llamarse:

DiaDeLaSemana.java

Fijate también que aparece una llave:

{

Esa llave indica:

"A partir de acá empieza el contenido de la clase."

La llave que aparece al final de todo:

}

es la que la cierra.

3. El método main
public static void main(String[] args) {

Esta línea seguramente te va a aparecer muchísimo en Java.

Por ahora podés pensarla así:

main es el lugar donde comienza a ejecutarse el programa.

Cuando apretás Ejecutar, Java busca el método:

main

y empieza a leer las instrucciones desde ahí.

No hace falta que todavía memorices exactamente qué significa public static void String[] args.

Lo realmente importante ahora es saber que:

public static void main(String[] args)

marca el inicio del programa principal.

4. Crear el generador de números aleatorios
Random aleatorio = new Random();

Acá pasan varias cosas.

Tenemos:

Random

que es el tipo de objeto que vamos a utilizar.

Después:

aleatorio

es el nombre que nosotros decidimos darle.

Podría haberse llamado:

Random numeroRandom = new Random();

o:

Random generador = new Random();

Pero se eligió aleatorio porque es fácil de entender.

Entonces:

Random aleatorio = new Random();

significa aproximadamente:

"Creá un objeto que pueda generar números aleatorios y llamalo aleatorio."

Después vamos a utilizar ese nombre:

aleatorio

para pedirle números.

5. Declarar la variable dia
int dia;

Acá creamos una variable llamada:

dia

y decimos que es de tipo:

int

int significa número entero.

Por ejemplo:

1
2
3
4
5
6
7

son valores que puede guardar un int.

Entonces:

int dia;

significa:

"Quiero una variable llamada dia que va a guardar números enteros."

Todavía no le estamos poniendo ningún valor.

No pusimos:

int dia = 5;

Solamente declaramos que la variable existe.

6. Declarar nombreDia
String nombreDia;

Acá hacemos algo parecido, pero ahora necesitamos guardar texto.

Por ejemplo:

"Lunes"
"Martes"
"Miércoles"

Para guardar texto en Java usamos:

String

Entonces:

String nombreDia;

significa:

"Quiero una variable llamada nombreDia que va a guardar texto."

Tenemos entonces dos variables:

int dia;
String nombreDia;

Una guarda un número:

5

y la otra guarda el nombre correspondiente:

"Viernes"
7. Comienza el do

Ahora aparece:

do {

Esto comienza una estructura repetitiva llamada:

do-while

Un do-while sirve para repetir instrucciones.

Su estructura general es:

do {

    instrucciones;

} while (condicion);

La idea es:

"Hacé esto y después comprobá si hay que volver a hacerlo."

Una característica muy importante del do-while es que siempre se ejecuta por lo menos una vez.

En nuestro programa queremos:

Generar días una y otra vez hasta que aparezca domingo.

Por eso tiene mucho sentido utilizar una repetición.

8. Generar el número aleatorio

Esta es una de las líneas más importantes:

dia = aleatorio.nextInt(7) + 1;

Vamos a separarla.

Primero:

aleatorio.nextInt(7)

genera un número aleatorio entre:

0 y 6

Es decir, puede salir:

0
1
2
3
4
5
6

¿Por qué no llega hasta 7?

Porque:

nextInt(7)

genera desde 0 hasta uno menos que 7.

Entonces:

0 → 6

Pero nosotros necesitamos días del:

1 → 7

Por eso hacemos:

+ 1

Entonces:

aleatorio.nextInt(7) + 1

queda así:

0 + 1 = 1
1 + 1 = 2
2 + 1 = 3
3 + 1 = 4
4 + 1 = 5
5 + 1 = 6
6 + 1 = 7

Por lo tanto genera:

1, 2, 3, 4, 5, 6 o 7

Y finalmente ese número se guarda en:

dia

Por ejemplo, si salió un 4:

dia = 4;
9. El switch

Ahora tenemos:

switch (dia) {

El switch sirve para preguntar:

"¿Qué valor tiene dia?"

Y según el valor, realiza una acción diferente.

En este programa tenemos siete posibilidades.

1 → Lunes
2 → Martes
3 → Miércoles
4 → Jueves
5 → Viernes
6 → Sábado
7 → Domingo
10. Primer case
case 1:
    nombreDia = "Lunes";
    break;

Esto significa:

"Si dia vale 1, guardá "Lunes" en nombreDia."

Es decir, si antes salió:

dia = 1;

entonces:

nombreDia = "Lunes";

Ahora tenemos:

dia = 1
nombreDia = "Lunes"
11. ¿Para qué sirve break?

Después aparece:

break;

break significa aproximadamente:

"Terminá acá este case y salí del switch."

Es muy importante.

Por ejemplo:

case 1:
    nombreDia = "Lunes";
    break;

Si salió 1, Java encuentra Lunes y gracias al break deja de revisar los demás casos.

12. Los demás case

Lo mismo ocurre con todos los otros.

case 2:
    nombreDia = "Martes";
    break;

Si:

dia = 2

entonces:

nombreDia = "Martes"
case 3:
    nombreDia = "Miércoles";
    break;

Si:

dia = 3

entonces:

nombreDia = "Miércoles"
case 4:
    nombreDia = "Jueves";
    break;

Si:

dia = 4

entonces:

nombreDia = "Jueves"
case 5:
    nombreDia = "Viernes";
    break;

Si:

dia = 5

entonces:

nombreDia = "Viernes"
case 6:
    nombreDia = "Sábado";
    break;

Si:

dia = 6

entonces:

nombreDia = "Sábado"

Y finalmente:

case 7:
    nombreDia = "Domingo";
    break;

Si:

dia = 7

entonces:

nombreDia = "Domingo"

Y este caso es especialmente importante porque cuando salga 7, después terminará la repetición.

13. ¿Qué es default?

Tenemos:

default:
    nombreDia = "Día inválido";

default significa:

"Si no se cumplió ninguno de los casos anteriores, hacé esto."

Por ejemplo, imaginemos que:

dia = 15;

No existe:

case 15:

Entonces Java llegaría al:

default

y pondría:

nombreDia = "Día inválido";

Pero en este programa es prácticamente imposible que suceda porque nosotros generamos únicamente números entre 1 y 7.

Por eso el comentario dice:

// Esto no debería ocurrir debido al rango de generación de números
14. Mostrar el resultado

Después aparece:

System.out.println("Número generado: " + dia + " - Día de la semana: " + nombreDia);

System.out.println sirve para mostrar información en la consola.

Tenemos:

"Numero generado: "

después:

+ dia

después:

" - Día de la semana: "

y finalmente:

+ nombreDia

Los signos:

+

acá sirven para unir texto y variables.

Por ejemplo, imaginemos que salió:

dia = 3
nombreDia = "Miércoles"

La consola mostraría:

Número generado: 3 - Día de la semana: Miércoles
15. La condición del while

Llegamos a una parte fundamental:

} while (dia != 7);

Recordá que estamos dentro de un:

do {

Por eso ahora aparece:

while

La condición es:

dia != 7

El operador:

!=

significa:

distinto de

Entonces:

dia != 7

significa:

"Mientras dia sea distinto de 7."

Por lo tanto:

} while (dia != 7);

significa:

"Volvé a repetir todo mientras no haya salido el número 7."

Por ejemplo

Supongamos que la primera vez sale:

3

Entonces:

3 != 7

es verdadero.

Por lo tanto vuelve a repetirse.

Después sale:

5

Se pregunta:

5 != 7

Verdadero.

Se repite otra vez.

Después sale:

2

Se pregunta:

2 != 7

Verdadero.

Se repite.

Finalmente sale:

7

Ahora se pregunta:

7 != 7

Eso es falso.

Entonces el ciclo termina.

16. Mensaje final

Cuando finalmente salió 7, el programa sale del do-while y continúa con:

System.out.println("Se ha generado el día domingo. Fin del programa.");

Entonces muestra:

Se ha generado el día domingo. Fin del programa.

Y después el programa termina.