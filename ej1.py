def agregar_producto(productos):

    nombre = input("Ingrese nombre del producto: ")

    if nombre == "":
        print("Error: el nombre no puede estar vacío")
        return

    if nombre in productos:
        print("Error: el producto ya existe")
        return

    while True:
        try:
            stock = int(input("Ingrese stock: "))

            if stock >= 0:
                break
            else:
                print("Error: el stock debe ser mayor o igual a 0")

        except:
            print("Error: debe ingresar un número entero")

    while True:
        try:
            precio = int(input("Ingrese precio: "))

            if precio > 0:
                break
            else:
                print("Error: el precio debe ser mayor que 0")

        except:
            print("Error: debe ingresar un número")

    productos[nombre] = [stock, precio]

    print("Producto agregado correctamente")


def mostrar_productos(productos):

    if len(productos) == 0:
        print("No existen productos registrados")
        return

    print("\n--- LISTADO DE PRODUCTOS ---")

    for nombre in productos:

        stock = productos[nombre][0]
        precio = productos[nombre][1]

        print("Nombre:", nombre)
        print("Stock:", stock)
        print("Precio:", precio)
        print("---------------------------")


def buscar_producto(productos):

    if len(productos) == 0:
        print("No existen productos registrados")
        return

    nombre = input("Ingrese nombre del producto a buscar: ")

    if nombre in productos:

        stock = productos[nombre][0]
        precio = productos[nombre][1]

        print("Producto encontrado")
        print("Stock:", stock)
        print("Precio:", precio)

    else:
        print("Producto no existe")


def producto_mas_caro(productos):

    if len(productos) == 0:
        print("No existen productos registrados")
        return

    mayor_nombre = ""
    mayor_precio = 0

    for nombre in productos:

        precio = productos[nombre][1]

        if precio > mayor_precio:

            mayor_precio = precio
            mayor_nombre = nombre

    print("\n--- PRODUCTO MÁS CARO ---")
    print("Nombre:", mayor_nombre)
    print("Precio:", mayor_precio)


# Programa principal

productos = {}

while True:

    print("\n===== INVENTARIO =====")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Producto más caro")
    print("5. Salir")

    try:
        opcion = int(input("Ingrese una opción: "))

    except:
        print("Error: debe ingresar un número")
        continue

    if opcion == 1:
        agregar_producto(productos)

    elif opcion == 2:
        mostrar_productos(productos)

    elif opcion == 3:
        buscar_producto(productos)

    elif opcion == 4:
        producto_mas_caro(productos)

    elif opcion == 5:
        print("Programa finalizado")
        break

    else:
        print("Error: la opción debe estar entre 1 y 5")