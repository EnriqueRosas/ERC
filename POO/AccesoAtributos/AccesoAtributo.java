

public class AccesoAtributo {
    
    public static void main(String[] args) {
        int a1;
        double b1;
        boolean c1;
        char e1;
        String nombre1;

        System.out.println("Viendo atributos");
        valores val = new Valores();  // Cambiado de 'valores' a 'Valores'
        valores val2 = new Valores();//accesando a los atributos
        valores val3 = new Valores();

        a1 = val.a;
        System.out.println("valor de a1: " + a1);

        val.a = 50;
        val2.b = 50.32;
        val3.c = false;
        
    }
}