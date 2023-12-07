import java.util.Scanner; // libreria para poder leer datos

//definimos clase lector
public class Lector{
    //funcion principal
    public static void main(String[]arg) {
        //definimos una variable entera
        int valor;
        double valor2;
        char valor3;
        String valor4;
        valor2 = 0;

        Scanner sc = new Scanner(System.in); //permite la entrada de datos del teclado
        //pedimos al usuario que ingrese un numero entero
        System.out.println("Dame el entero a leer\n ");
        //lee un caracter y lo asigna a la variable valor
        valor = sc.nextInt();
        //imprimimos un mensaje con el valor de la variable
        System.out.println("El numero entero es "+valor);
        System.out.println("------------------------------");
        System.out.println("Dame un numero Double a leer\n ");
        valor2 = sc.nextDouble();
        System.out.println("El numero double es "+valor2);
        System.out.println("------------------------------");
        System.out.println("Dame un char a leer\n ");
        valor3 = sc.next().charAt(0);
        System.out.println("El char es "+valor3);
        System.out.println("------------------------------");
        System.out.println("Dame un String\n ");
        sc.nextLine();
        valor4 = sc.nextLine();
        System.out.println("El String es "+valor4);


        //casting = es transformar un variable de un tipo a otro tipo xd
    }//fin main
}//fin clase Lector.cha(0)