//Ejercicio 3: Cálculo de la distancia entre dos puntos
import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        double x1, y1, x2, y2, distancia;

        System.out.print("Ingrese x1: ");
        x1 = teclado.nextDouble();

        System.out.print("Ingrese y1: ");
        y1 = teclado.nextDouble();

        System.out.print("Ingrese x2: ");
        x2 = teclado.nextDouble();

        System.out.print("Ingrese y2: ");
        y2 = teclado.nextDouble();

        distancia = Math.sqrt(
            Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2)
        );

        System.out.println("La distancia entre los puntos es: " + distancia);

        teclado.close();
    }
}

