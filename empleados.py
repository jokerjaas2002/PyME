# empleados.py

def ingresar_datos_empleado():
    while True:
        try:
            nombre = input("Ingrese el nombre del empleado: ")
            apellido = input("Ingrese el apellido del empleado: ")
            sueldo_base = float(input("Ingrese el sueldo base del empleado: "))
            fecha_ingreso = input("Ingrese la fecha de ingreso (DD/MM/AAAA): ")
            cantidad_hijos = int(input("Ingrese la cantidad de hijos: "))
            if cantidad_hijos < 0:
                raise ValueError("La cantidad de hijos no puede ser negativa.")
            return {
                'nombre': nombre,
                'apellido': apellido,
                'sueldo_base': sueldo_base,
                'fecha_ingreso': fecha_ingreso,
                'cantidad_hijos': cantidad_hijos
            }
        except ValueError as e:
            print(f"Error en la entrada de datos: {e}. Intente de nuevo.")

def calcular_base_imponible(sueldo_base, meses_trabajados, cantidad_hijos):
    bonificacion = 0.01 * sueldo_base * meses_trabajados
    asignacion_familiar = 0.05 * sueldo_base * cantidad_hijos
    base_imponible = sueldo_base + bonificacion + asignacion_familiar
    return base_imponible

def calcular_salud(base_imponible):
    return 0.07 * base_imponible

def calcular_sso(base_imponible, empresa):
    if empresa == 1:
        return 0.12 * base_imponible
    elif empresa == 2:
        return 0.114 * base_imponible
    else:
        raise ValueError("Empresa de SSO inválida.")

def calcular_promedios(pagos):
    if len(pagos) == 0:
        return 0, 0
    promedio_salud = sum(pago['salud'] for pago in pagos) / len(pagos)
    promedio_sso = sum(pago['sso'] for pago in pagos) / len(pagos)
    return promedio_salud, promedio_sso