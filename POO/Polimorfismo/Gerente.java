public class Gerente extends Empleado {
    private double salariobase;

    public Gerente(String nombre, int diasTrabajados) {
        super(nombre, diasTrabajados);
        this.salariobase = 1200;
    }

    @Override
    public double calcularSueldo() {
        double sueldo = getDiasTrabajados() * 120;
        sueldo = sueldo + salariobase;
        return sueldo;
    }
}
