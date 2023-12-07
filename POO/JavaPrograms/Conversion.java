//para ejecutar el programa debemos pasar los argumentos
//este programa recibe como argumentos 3 tipos de datos: un entero, un double y un  
// asi se ejecuta : java Conversion 10 20.23 z 
//este comentario es para hacer un comit mas xd
class Conversion{
    
    public static void main(String[]arg) {
    
    int tcoche;
    double temperatura;
    char nivel;

    for(int i=0; i<arg.length; i++){
        System.out.println("\n "+arg[i]);
    }
    
    tcoche=Integer.parseInt(arg[0]);
    temperatura=Double.parseDouble(arg[1]);
    nivel=arg[2].charAt(0);
    }
}