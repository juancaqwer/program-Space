public class MostrarNumero {
    private int numero;

    public MostrarNumero(int numero) {
        this.numero = numero;
    }

    public int invertirNumero() {
        int invertido = 0;
        int n = Math.abs(numero);
        while (n != 0) {
            invertido = invertido * 10 + n % 10;
            n /= 10;
        }
        return numero < 0 ? -invertido : invertido;
    }
}