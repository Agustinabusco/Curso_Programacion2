import java.util.Random;

public class SumaNumerosImpares {

    public static void main(String[] args) {

        Random aleatorio = new Random();

        int numero;
        int sumaImpares = 0;

        do {
            numero = aleatorio.nextInt(11);

            System.out.println("Número generado: " + numero);

            if (numero % 2 == 0) {
                System.out.println("El número es par.");
            } else {
                System.out.println("El número es impar.");

                sumaImpares = sumaImpares + numero;

                System.out.println("Suma acumulada de impares: " + sumaImpares);
            }

            System.out.println("-------------------------");

        } while (sumaImpares <= 25);

        System.out.println("La suma de los números impares superó 25.");
        System.out.println("Suma total de los números impares: " + sumaImpares);
    }
}