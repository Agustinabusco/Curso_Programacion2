import java.util.Scanner;

public class DistribucionEquipos {

    public static void main(String[] args) {

        // Creamos el Scanner para leer datos ingresados por el usuario
        Scanner teclado = new Scanner(System.in);

        // Declaramos las variables enteras
        int totalEstudiantes;
        int estudiantesPorEquipo;
        int equiposCompletos;
        int estudiantesRestantes;

        // Solicitamos la cantidad total de estudiantes
        System.out.print("Ingrese la cantidad total de estudiantes: ");
        totalEstudiantes = teclado.nextInt();

        // Solicitamos la cantidad de estudiantes por equipo
        System.out.print("Ingrese la cantidad de estudiantes por equipo: ");
        estudiantesPorEquipo = teclado.nextInt();

        // Mostramos los valores ingresados
        System.out.println("\nDatos ingresados:");
        System.out.println("Cantidad total de estudiantes: " + totalEstudiantes);
        System.out.println("Cantidad de estudiantes por equipo: " + estudiantesPorEquipo);

        // Calculamos los equipos completos
        equiposCompletos = totalEstudiantes / estudiantesPorEquipo;

        // Calculamos los estudiantes que quedan sin equipo completo
        estudiantesRestantes = totalEstudiantes % estudiantesPorEquipo;

        // Mostramos los resultados
        System.out.println("\nResultados:");
        System.out.println("Se pueden formar " + equiposCompletos + " equipos completos.");
        System.out.println("Quedan " + estudiantesRestantes
                + " estudiantes sin integrar un equipo completo.");

        // Cerramos el Scanner
        teclado.close();
    }
}