public class Ejercicio05 {

    public static void main(String[] args) {

        String texto = "PROGRAMACION JAVA";

        int contadorVocales = 0;

        for (int i = 0; i < texto.length(); i++) {

            char letra = texto.charAt(i);

            if (letra == 'A' || letra == 'E' || letra == 'I' || letra == 'O' || letra == 'U') {
                contadorVocales++;
            }
        }

        System.out.println("Texto analizado: " + texto);
        System.out.println("Cantidad total de caracteres: " + texto.length());
        System.out.println("Cantidad de vocales: " + contadorVocales);
    }
}
