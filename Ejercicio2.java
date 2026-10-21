//Ejercicio 2: Conversión de kilómetros a metros y centímetros
import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        double kilometros, metros, centimetros;

        System.out.print("Ingrese la distancia en kilometros: ");
        kilometros = teclado.nextDouble();

        metros = kilometros * 1000;
        centimetros = kilometros * 100000;

        System.out.println("Distancia en metros: " + metros);
        System.out.println("Distancia en centimetros: " + centimetros);

        teclado.close();
    }
}
