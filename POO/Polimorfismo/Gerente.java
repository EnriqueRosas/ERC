public class Gerente extends Empleado {
    private double salariobase;

    public Gerente(String nombre, int diasTrabajados) {
        super(nombre, diasTrabajados);
        this.salariobase = 1200;
    }

    /*metodo del salario del empleado gerente
* obtiene los dias trabajados
* el sueldo es igual a los dias trabajados * 120
* y a eso se le agrega el salario base de gerente
*/
    @Override //ayuda a la sobreescritura de metodos
    public double calcularSueldo() {
        double sueldo = getDiasTrabajados() * 120;
        sueldo = sueldo + salariobase;
        return sueldo;
    }
}
