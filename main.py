from empleados import *

def main():
    empleados = []
    for i in range(10):
        print(f"\n--- Ingreso de datos para el empleado {i + 1} ---")
        empleado = ingresar_datos_empleado()
        empleados.append(empleado)

    pagos = []
    for empleado in empleados:
        meses_trabajados = int(input(f"Ingrese la cantidad de meses trabajados por {empleado['nombre']} {empleado['apellido']}: "))
        base_imponible = calcular_base_imponible(empleado['sueldo_base'], meses_trabajados, empleado['cantidad_hijos'])
        salud = calcular_salud(base_imponible)

        while True:
            try:
                empresa = int(input("Seleccione la empresa de SSO (1 o 2): "))
                sso = calcular_sso(base_imponible, empresa)
                break
            except ValueError as e:
                print(f"Error: {e}. Intente de nuevo.")

        pagos.append({'salud': salud, 'sso': sso})
        print(f"\nEmpleado: {empleado['nombre']} {empleado['apellido']}")
        print(f"Base Imponible: {base_imponible:.2f}")
        print(f"Pago en Salud: {salud:.2f}")
        print(f"Pago en SSO: {sso:.2f}")

    promedio_salud, promedio_sso = calcular_promedios(pagos)
    print(f"\nPromedio de pago en Salud: {promedio_salud:.2f}")
    print(f"Promedio de pago en SSO: {promedio_sso:.2f}")

if __name__ == "__main__":
    main()