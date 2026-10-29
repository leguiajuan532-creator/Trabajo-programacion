java
import java.util.Scanner;

public class menu {

    static Scanner entrada = new Scanner(System.in);

    public static void main(String[] args) {

        int opcion;

        do {
            System.out.println("\n===== MENU PRINCIPAL =====");
            System.out.println("1. Calcular factorial");
            System.out.println("2. Calcular IMC");
            System.out.println("3. Hacer una pausa de 5 segundos");
            System.out.println("4. Salir");
            System.out.print("Seleccione una opcion: ");

            opcion = entrada.nextInt();

            switch (opcion) {

                case 1:
                    System.out.print("Ingrese un numero entero: ");
                    int numero = entrada.nextInt();

                    if (numero < 0) {
                        System.out.println("No se puede calcular el factorial de un numero negativo.");
                    } else {
                        System.out.println("El factorial es: " + factorial(numero));
                    }
                    break;

                case 2:
                    System.out.print("Ingrese su peso en Kg: ");
                    double peso = entrada.nextDouble();

                    System.out.print("Ingrese su estatura en centimetros: ");
                    double estatura = entrada.nextDouble();

                    if (peso <= 0 || estatura <= 0) {
                        System.out.println("El peso y la estatura deben ser mayores que cero.");
                    } else {
                        double imc = calcularIMC(peso, estatura);

                        System.out.printf("Su IMC es: %.2f%n", imc);

                        if (imc <= 18) {
                            System.out.println("IMC con valor bajo");
                        } else {
                            System.out.println("Mantenga su peso controlado");
                        }
                    }
                    break;

                case 3:
                    hacerPausa();
                    break;

                case 4:
                    System.out.println("Programa finalizado.");
                    break;

                default:
                    System.out.println("Opcion no valida.");
            }

        } while (opcion != 4);

        entrada.close();
    }

    public static long factorial(int numero) {
        long resultado = 1;

        for (int i = 1; i <= numero; i++) {
            resultado = resultado * i;
        }

        return resultado;
    }

    public static double calcularIMC(double peso, double estatura) {
        double estaturaMetros = estatura / 100;

        return peso / (estaturaMetros * estaturaMetros);
    }

    public static void hacerPausa() {
        System.out.println("Haga una pausa de 5 segundos...");

        try {
            Thread.sleep(5000);
        } catch (InterruptedException e) {
            System.out.println("La pausa fue interrumpida.");
            Thread.currentThread().interrupt();
            return;
        }

        System.out.println("La pausa ha terminado.");
    }
}
