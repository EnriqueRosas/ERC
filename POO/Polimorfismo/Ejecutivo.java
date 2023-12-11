public class Ejecutivo extends Empleado {
    private double salariobase;

    public Ejecutivo(String nombre, int diasTrabajados) {
        super(nombre, diasTrabajados);
        this.salariobase = 1800;
    }

    @Override
    public double calcularSueldo() {
        double sueldo = getDiasTrabajados() * 120;
        sueldo = sueldo + salariobase;
        return sueldo;
    }
}
