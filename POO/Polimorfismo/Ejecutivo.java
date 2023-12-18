public class Ejecutivo extends Empleado {
    private double salariobase;

    public Ejecutivo(String nombre, int diasTrabajados) {
        super(nombre, diasTrabajados);
        this.salariobase = 1800;
    }
/*metodo del salario del empleado ejecutivo
 * obtiene los dias trabajados
 * el sueldo es igual a los dias trabajados * 180
 * y a eso se le suma el salario base
*/
    @Override
    public double calcularSueldo() {
        double sueldo = getDiasTrabajados() * 180;
        sueldo = sueldo + salariobase;
        return sueldo;
    }
}
