// Importamos la clase Random para poder generar números aleatorios
import java.util.Random;

// Creamos una clase pública llamada SumaHastaAleatorio
// El archivo debe llamarse SumaHastaAleatorio.java
public class SumaHastaAleatorio {

    // Método principal: desde aquí comienza la ejecución del programa
    public static void main(String[] args) {

        // Creamos un objeto de tipo Random llamado aleatorio
        // Este objeto nos permitirá generar números al azar
        Random aleatorio = new Random();

        // Declaramos una variable entera llamada m
        // nextInt(20) genera un número desde 0 hasta 19
        // Sumamos 1 para que el resultado esté entre 1 y 20
        int m = aleatorio.nextInt(20) + 1;

        // Declaramos la variable suma y la inicializamos en 0
        // Esta variable irá acumulando los números desde 1 hasta m
        int suma = 0;

        // Mostramos en pantalla el número aleatorio generado
        System.out.println("El número generado es: " + m);

        // Creamos una variable llamada numero que comienza en 1
        // El ciclo continúa mientras numero sea menor o igual que m
        // Después de cada repetición, numero aumenta en 1
        for (int numero = 1; numero <= m; numero++) {

            // Sumamos el valor actual de numero al valor acumulado
            // de la variable suma
            suma = suma + numero;
        }

        // Cuando el ciclo termina, mostramos el valor final de suma
        System.out.println("La suma de los números desde 1 hasta "
                + m + " es: " + suma);
    }
}