import java.util.Scanner;
import java.util.InputMismatchException;

//este programa muestra como manejar errores pidiendo al usuario que ingrese un numero entero, de lo contrario este mostrara un mensaje de error
//el programa no se cerrara hasta que se ingrese un numero entero
//el programa contara las veces que el usuario intente ingresar un numero entero hasta que lo logre
public class Errorr {
    public static void main(String[] args) {
        //definimos un entero
        int numero = 0;
        int contador = 0;
        //definimos un boleano 
        boolean entradaValida = false;
        //
        Scanner sc = new Scanner(System.in);
        
        while (!entradaValida) {
            try {
                
                System.out.print("Ingresa Un Número Entero: ");
                numero = sc.nextInt();
                entradaValida = true; // Si llegamos aquí, la entrada es válida, salimos del bucle
            } catch (InputMismatchException e) {
                // Si se lanza InputMismatchException, significa que la entrada no es un número entero
                contador++;
                System.out.println("No Sea Tonto... Debes Ingresar Un Número Entero, esta es la ocacion numero "+contador+" Que se equivoca");
                sc.nextLine(); // Limpiamos el buffer del Scanner para evitar bucles infinitos
            }
        }//Aqui el programa sale del ciclo while e imprime el numero entero ingresado
        System.out.println("Bien Hecho, El Número Entero Que Se Ingreso Es: " + numero);
    }
}
