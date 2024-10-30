# usar datetime para gestionar las fechas

from datetime import datetime  

# Definir habitaciones y características mediante una lista:
habitaciones = [
    [301, "sencilla", 30000, "disponible", None, (datetime(2024, 10, 1), datetime(2024, 10, 30))],
    [302, "sencilla", 30000, "disponible", None, (datetime(2024, 12, 4), datetime(2024, 12, 30))],
    [401, "doble", 80000, "disponible", None, (datetime(2024, 10, 20), datetime(2024, 11, 25))],
    [402, "doble", 80000, "disponible", None, (datetime(2024, 11, 1), datetime(2024, 11, 30))],
    [501, "suite", 250000, "disponible", None, (datetime(2024, 10, 15), datetime(2024, 12, 15))],
]

# Crear listas de almacenado para el historial y las reservas
reservas = []
historial = []

# Impresión del menú
def mostrar_menu():
    print("\nMenú Principal  Hotel la resaca:")
    print(
        """
1. Gestión de Habitaciones
2. Reservas
3. Registro de Entrada (Check-in)
4. Registro de Salida (Check-out)
5. Reportes de Ocupación y Historial
6. Salir
        """
    )

# Funciones de gestión de habitaciones
def gestion_habitaciones():
    while True:
        print("\nGestión de Habitaciones:")
        print(
            """
1. Mostrar habitaciones
2. Modificar habitación
3. Eliminar habitación
4. Regresar
            """
        )
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            for habitacion in habitaciones:
                fechas = habitacion[5]
                print(
                    f"Habitación {habitacion[0]}: {habitacion[1]}, Precio: {habitacion[2]}, Estado: {habitacion[3]}, "
                    f"Fechas disponibles: {fechas[0].date()} a {fechas[1].date()}"
                )
#Evaluar con try y exept para evitar errores por digitar letras envez de numeros
        elif opcion == "2":
            try:
                num = int(input("Ingrese el número de habitación a modificar: "))
                for habitacion in habitaciones:
                    if habitacion[0] == num:
                        habitacion[2] = float(input("Ingrese nuevo precio: "))
                        habitacion[1] = input("Ingrese nuevo tipo (sencilla/doble/suite): ")
                        print("Habitación modificada.")
                        break
                else:
                    print("Habitación no encontrada.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

        elif opcion == "3":
            try:
                num = int(input("Ingrese el número de habitación a eliminar: "))
                for habitacion in habitaciones:
                    if habitacion[0] == num and habitacion[3] == "disponible":
                        habitaciones.remove(habitacion)
                        print("Habitación eliminada.")
                        break
                else:
                    print("Habitación no encontrada o no está disponible.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

        elif opcion == "4":
            break


# Funciones de la opción 2 reservas
def realizar_reserva():
    print("Antes de reservar porfavor ver el apartado de gestion_habitaciones para ver habitaciones disponibles.")
    nombre_cliente = input("Ingrese el nombre del cliente: ")

    print("\nTipos de habitación:")
    print("1. Sencilla")
    print("2. Doble")
    print("3. Suite")

    try:
        tipo_opcion = int(input("Seleccione tipo de habitación (1-3): "))
        tipo_habitacion = ["sencilla", "doble", "suite"][tipo_opcion - 1]
    except (ValueError, IndexError):
        print("Opción no válida. Intente nuevamente.")
        return

    # Pedir fechas de inicio y fin
    fecha_inicio_str = input("Ingrese la fecha de inicio (AÑO-MES-DIA): ")#Digitar en orden estricto usando guiones
    fecha_fin_str = input("Ingrese la fecha de fin (AÑO-MES-DIA): ")#Digitar en orden estricto usando guiones

    try:
        fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d")
        fecha_fin = datetime.strptime(fecha_fin_str, "%Y-%m-%d")
    except ValueError:
        print("Formato de fecha inválido. Intente nuevamente.")
        return

    if fecha_fin <= fecha_inicio:
        print("La fecha de fin debe ser posterior a la fecha de inicio.")
        return

    # Comprobar disponibilidad en el rango de fechas
    habitaciones_disponibles = [
        h for h in habitaciones 
        if h[1] == tipo_habitacion 
        and h[3] == "disponible" 
        and h[5][0] <= fecha_inicio <= h[5][1]  # La fecha de inicio debe estar dentro del rango de la habitación
        and h[5][0] <= fecha_fin <= h[5][1]  # La fecha de fin debe estar dentro del rango de la habitación
    ]

    if not habitaciones_disponibles:
        print("No hay habitaciones disponibles del tipo solicitado en las fechas seleccionadas.")
        return

    print("\nHabitaciones disponibles:")
    for habitacion in habitaciones_disponibles:
        print(f"Habitación {habitacion[0]} - Precio: {habitacion[2]} por noche")

    try:
        N_Habitacion = int(input("Seleccione el número de habitación para reservar: "))
        for habitacion in habitaciones:
            if habitacion[0] == N_Habitacion and habitacion[3] == "disponible":
                habitacion[3] = "ocupada"
                habitacion[4] = (nombre_cliente, (fecha_inicio, fecha_fin))
                dias = (fecha_fin - fecha_inicio).days
                reservas.append((nombre_cliente, habitacion[0], dias))
                print(f"Reserva exitosa en la habitación {habitacion[0]} para {dias} días.")
                return

        print("Número de habitación no válido o ya está ocupada.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Cancelar reservas
def cancelar_reserva():
    nombre_cliente = input("Ingrese el nombre del cliente para cancelar la reserva: ")
    for reserva in reservas:
        if reserva[0] == nombre_cliente:
            for habitacion in habitaciones:
                if habitacion[0] == reserva[1]:
                    habitacion[3] = "disponible"
                    habitacion[4] = None
                    reservas.remove(reserva)
                    print(f"Reserva de {nombre_cliente} cancelada. Habitación {habitacion[0]} ahora disponible.")
                    return
    print("No se encontró ninguna reserva activa para este cliente.")

def mostrar_reservas_activas():
    if not reservas:
        print("No hay reservas activas.")
    else:
        print("\nReservas activas:")
        for reserva in reservas:
            print(f"Cliente: {reserva[0]}, Habitación: {reserva[1]}, Días: {reserva[2]}")

# Función para gestionar las reservas
def gestion_reservas():
    while True:
        print("\nGestión de Reservas:")
        print(
            """
1. Realizar Reserva
2. Cancelar Reserva
3. Mostrar Reservas Activas
4. Regresar
            """
        )
        sub_opcion = input("Seleccione una opción: ")

        if sub_opcion == "1":
            realizar_reserva()
        elif sub_opcion == "2":
            cancelar_reserva()
        elif sub_opcion == "3":
            mostrar_reservas_activas()
        elif sub_opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Apartado de registros
def registrar_entrada():
    nombre_cliente = input("Ingrese el nombre del cliente para check-in: ")
    habitaciones_cliente = [h for h in habitaciones if h[4] and h[4][0] == nombre_cliente]

    if not habitaciones_cliente:
        print("No hay reservas para este cliente.")
        return

    print("\nReservas encontradas:")
    for habitacion in habitaciones_cliente:
        print(f"Habitación {habitacion[0]}")

    try:
        N_Habitacion = int(input("Seleccione el número de habitación para check-in: "))
        for habitacion in habitaciones_cliente:
            if habitacion[0] == N_Habitacion:
                print(f"Check-in registrado para {habitacion[4][0]} en habitación {N_Habitacion}.")
                return
        print("Número de habitación no válido.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

def registrar_salida():
    nombre_cliente = input("Ingrese el nombre del cliente para check-out: ")
    habitaciones_cliente = [h for h in habitaciones if h[4] and h[4][0] == nombre_cliente]

    if not habitaciones_cliente:
        print("No hay reservas para este cliente.")
        return

    print("\nReservas encontradas:")
    for habitacion in habitaciones_cliente:
        print(f"Habitación {habitacion[0]}")

    try:
        N_Habitacion = int(input("Seleccione el número de habitación para check-out: "))
        for habitacion in habitaciones_cliente:
            if habitacion[0] == N_Habitacion:
                cliente, (fecha_inicio, fecha_fin) = habitacion[4]
                dias = (fecha_fin - fecha_inicio).days
                costo = dias * habitacion[2]
                historial.append((cliente, habitacion[0], dias, costo))

                # Cancelar la reserva
                habitacion[3] = "disponible"
                habitacion[4] = None
                reservas[:] = [reserva for reserva in reservas if reserva[1] != habitacion[0]]

                print(f"Check-out registrado. Total a pagar: {costo}.")
                return
        print("Número de habitación no válido.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Reportes del hotel
def reportes():
    print("\nReportes de Ocupación y Historial:")
    print("Habitaciones ocupadas:")
    for habitacion in habitaciones:
        if habitacion[3] == "ocupada":
            print(f"Habitación {habitacion[0]} está ocupada por {habitacion[4][0]}.")

    print("\nHistorial de Estadías:")
    for registro in historial:
        print(f"Cliente: {registro[0]}, Habitación: {registro[1]}, Días: {registro[2]}, Total: {registro[3]}")

    tasa_ocupacion = (
        sum(1 for h in habitaciones if h[3] == "ocupada") / len(habitaciones) * 100
    )
    print(f"\nTasa de ocupación: {tasa_ocupacion:.2f}%")

# Función principal
def gestionar_opciones():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestion_habitaciones()
        elif opcion == "2":
            gestion_reservas()
        elif opcion == "3":
            registrar_entrada()
        elif opcion == "4":
            registrar_salida()
        elif opcion == "5":
            reportes()
        elif opcion == "6":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    gestionar_opciones()