//Ejercicio 1: Suma de dos números
import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        int numero1, numero2, suma;

        System.out.print("Ingrese el primer numero: ");
        numero1 = teclado.nextInt();

        System.out.print("Ingrese el segundo numero: ");
        numero2 = teclado.nextInt();

        suma = numero1 + numero2;

        System.out.println("La suma es: " + suma);

        teclado.close();
    }
}

