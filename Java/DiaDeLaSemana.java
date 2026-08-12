import java.util.Random;  

public class DiaDeLaSemana {  
    public static void main(String[] args) {  
        Random aleatorio = new Random();  
        int dia;  
        String nombreDia;  

        do {  
            dia = aleatorio.nextInt(7) + 1; // Genera un número entre 1 y 7  

            switch (dia) {  
                case 1:  
                    nombreDia = "Lunes";  
                    break;  
                case 2:  
                    nombreDia = "Martes";  
                    break;  
                case 3:  
                    nombreDia = "Miércoles";  
                    break;  
                case 4:  
                    nombreDia = "Jueves";  
                    break;  
                case 5:  
                    nombreDia = "Viernes";  
                    break;  
                case 6:  
                    nombreDia = "Sábado";  
                    break;  
                case 7:  
                    nombreDia = "Domingo";  
                    break;  
                default:  
                    nombreDia = "Día inválido"; // Esto no debería ocurrir debido al rango de generación de números
            }  

            System.out.println("Número generado: " + dia + " - Día de la semana: " + nombreDia);  

        } while (dia != 7); // Continúa hasta que se genere el número correspondiente al domingo (7)  

        System.out.println("Se ha generado el día domingo. Fin del programa.");  
    }  
}
