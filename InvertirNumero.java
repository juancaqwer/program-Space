import java.util.Scanner;

public class InvertirNumero {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.print("Introduce un número (o escribe 'salir' para terminar): ");
            if (scanner.hasNextInt()) {
                int numero = scanner.nextInt();
                MostrarNumero mostrar = new MostrarNumero(numero);
                int invertido = mostrar.invertirNumero();
                System.out.println("Número invertido: " + invertido);
            } else {
                String entrada = scanner.next();
                if (entrada.equalsIgnoreCase("salir")) {
                    System.out.println("Programa terminado.");
                    break;
                } else {
                    System.out.println("Entrada no válida. Por favor, introduce un número entero o 'salir'.");
                }
            }
        }
    }
}