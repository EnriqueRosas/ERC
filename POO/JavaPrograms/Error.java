import java.util.Scanner; // libreria para poder leer datos
import java.util.InputMismatchException;

class Error{
    public static void main(String[]arg) {
    
    int prueba;
    
    Scanner sc = new Scanner(System.in); //permite la entrada de datos del teclado
    try{
        System.out.println("ingresa un numero entero");
        prueba = sc.nextInt();
        System.out.println("El numero entero es "+prueba);
    }
    catch(InputMismatchException e){
        System.out.println("no sea burro pedimos un entero xd");
    }         
    }
}


///generar una variable conntador que se encargarar de contar las veces que se inteto ingresar un numero entero y no fue entero
///validar el tipo de dato