MAX_STOCK = 20  # stock total disponible

reservas = {}  # diccionario

def mostrar_menu():
    print("TOTEM AUTOATENCIÓN RESERVA STRIKE")
    print("1.- Reservar zapatillas")
    print("2.- Buscar zapatillas reservadas")
    print("3.- Ver stock de reservas")
    print("4.- Salir")

def reservar():
    print("-- Reservar Zapatillas --")
    nombre = input("Nombre del comprador: ").strip()

    if nombre in reservas:
        print("Error: ya existe una reserva con ese nombre.")
        return

    if obtener_total_reservas() >= MAX_STOCK:
        print("Error: no hay stock disponible.")
        return

    clave = input("Digite la palabra secreta para confirmar la reserva: ").strip()
    if clave != "EstoyEnListaDeReserva":
        print("Error: palabra clave incorrecta. Reserva no realizada.")
        return

    reservas[nombre] = 1
    print(f"Reserva realizada exitosamente para {nombre}.")

def buscar():
    print("-- Buscar Zapatillas Reservadas --")
    nombre = input("Nombre del comprador a buscar: ").strip()

    if nombre not in reservas:
        print("No se encontró ninguna reserva con ese nombre.")
        return

    pares = reservas[nombre]
    tipo = "VIP" if pares == 2 else "estándar"
    print(f"Reserva encontrada: {nombre} - {pares} par(es) ({tipo}).")

    if pares == 1:
        respuesta = input("¿Desea pagar adicional para VIP y reservar 2 pares? (s/n): ").strip().lower()
        if respuesta == 's':
            if obtener_total_reservas() + 1 <= MAX_STOCK:
                reservas[nombre] = 2
                print(f"Reserva actualizada a VIP. Ahora {nombre} tiene 2 pares reservados.")
            else:
                print("Error: no hay stock suficiente para actualizar a VIP.")
        elif respuesta == 'n':
            print("Manteniendo reserva actual.")
        else:
            print("Opción inválida. Manteniendo reserva actual.")
    else:
        print("Ya posee reserva VIP.")

def ver_stock():
    print("-- Ver Stock de Reservas --")
    total = obtener_total_reservas()
    disponible = MAX_STOCK - total
    print(f"Pares reservados: {total}")
    print(f"Pares disponibles: {disponible}")

def obtener_total_reservas():
    return sum(reservas.values())

def main():
    while True:
        print()
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == '1':
            reservar()
        elif opcion == '2':
            buscar()
        elif opcion == '3':
            ver_stock()
        elif opcion == '4':
            print("Programa terminado...")
            break
        else:
            print("Debe ingresar una opción válida!!")

if __name__ == "__main__":
    main()