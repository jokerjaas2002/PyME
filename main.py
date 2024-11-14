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