public class Mostrador extends Empleado {
    public Mostrador(String nombre, int diasTrabajados) {
        super(nombre, diasTrabajados);
    }

    @Override
    public double calcularSueldo() {
        double sueldo = getDiasTrabajados() * 80;
        return sueldo;
    }
}
