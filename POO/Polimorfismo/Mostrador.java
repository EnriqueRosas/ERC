public class Mostrador extends Empleado {
    public Mostrador(String nombre, int diasTrabajados) {
        super(nombre, diasTrabajados);
    }
/*metodo del salario del empleado de mostrador
 * obtiene los dias trabajados
 * el sueldo es igual a los dias trabajados * 80
*/
    @Override
    public double calcularSueldo() {
        double sueldo = getDiasTrabajados() * 80;
        return sueldo;
    }
}
