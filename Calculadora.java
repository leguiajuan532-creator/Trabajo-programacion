//Calculadora
public class Calculadora {

    // Metodo para sumar dos numeros
    public void suma(float num1, float num2) {
        float resultado = num1 + num2;
        System.out.printf("La suma es: %.1f%n", resultado);
    }

    // Metodo para multiplicar dos numeros
    public void producto(float num1, float num2) {
        float resultado = num1 * num2;
        System.out.printf("El producto es: %.1f%n", resultado);
    }

    // Metodo principal
    public static void main(String[] args) {
        Calculadora calculadora = new Calculadora();

        calculadora.suma(5.0f, 3.0f);
        calculadora.producto(5.0f, 3.0f);
    }
}
