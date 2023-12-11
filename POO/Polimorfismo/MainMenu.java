import java.util.Scanner;

public class MainMenu {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Bucle principal
        while (true) {
            // Paso 1: Pedir los días trabajados
            System.out.println("Ingrese los días trabajados (entre 1 y 31, ingrese 0 para salir):");
            int diasTrabajados = scanner.nextInt();

            // Verificar si el usuario desea salir
            if (diasTrabajados == 0) {
                System.out.println("Saliendo del programa. ¡Hasta luego!");
                break;
            }

            if (diasTrabajados < 1 || diasTrabajados > 31) {
                System.out.println("Error: Los días trabajados deben estar entre 1 y 31.");
                continue;  // Volver al inicio del bucle
            }

            // Paso 2: Seleccionar el tipo de empleado
            System.out.println("Seleccione el tipo de empleado:");
            System.out.println("1. Gerente");
            System.out.println("2. Mostrador");
            System.out.println("3. Ejecutivo");

            int tipoEmpleado = scanner.nextInt();

            Empleado empleado = null;

            // Paso 3: Crear el objeto Empleado según el tipo seleccionado
            switch (tipoEmpleado) {
                case 1:
                    empleado = new Gerente("Juan", diasTrabajados);
                    break;
                case 2:
                    empleado = new Mostrador("Maria", diasTrabajados);
                    break;
                case 3:
                    empleado = new Ejecutivo("Carlos", diasTrabajados);
                    break;
                default:
                    System.out.println("Tipo de empleado no válido");
                    continue;  // Volver al inicio del bucle
            }

            // Mostrar resultados
            System.out.println("Salario de " + empleado.getNombre() + ": $" + empleado.calcularSueldo());
        }

        scanner.close();
    }
}
