public class Empleado {
    protected String nombre;
    protected int diasTrabajados;

    public Empleado(String nombre, int diasTrabajados) {
        this.nombre = nombre;
        this.diasTrabajados = diasTrabajados;
    }

    public String getNombre() {
        return nombre;
    }

    public int getDiasTrabajados() {
        return diasTrabajados;
    }

    public double calcularSueldo() {
        return 0; // Implementación en las clases derivadas
    }
}
