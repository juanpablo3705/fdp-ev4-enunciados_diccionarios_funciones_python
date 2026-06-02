# inicializar diccionario vacío:
productos = {}

# funcion crear producto:
def agregar_producto(productos):
    nombre = input("Ingrese el nombre del producto: ")
    stock = int(input("Ingrese el stock del producto: "))
    precio = int(input("Ingrese el precio del producto: "))
    productos[nombre] = [stock,precio]

# funcion mostrar productos:
def mostrar_productos(productos):
    for nombre in productos:
        stock = productos[nombre][0]
        precio = productos[nombre][1]
        print(f"Nombre: {nombre}")
        print(f"Stock: {stock}")
        print(f"Precio: {precio}")

# funcion buscar productos:
def buscar_producto(productos):
    nombre = input("Ingrese el nombre del producto a buscar: ")
    if nombre in productos:
        print(f"Producto encontrado: {nombre}")
    else:
        print("Producto no encontrado.")

# funcion producto mas caro:
def producto_mas_caro(productos):
    mayor_precio = 0
    mayor_nombre = ""
    for nombre in productos:
        precio = productos[nombre][1]
        if precio > mayor_precio:
            mayor_precio = precio
            mayor_nombre = nombre
    print(f"Producto mas caro: {mayor_nombre}, precio: ${mayor_precio}")

# programa y menú:
while True:
    print("----- Menú -----")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Producto mas caro")
    print("5. Salir")
    opcion_menu = int(input("Ingrese una opción del menú: "))
    match opcion_menu:
        case 1:
            agregar_producto(productos)
        case 2:
            mostrar_productos(productos)
        case 3:
            buscar_producto(productos)
        case 4:
            producto_mas_caro(productos)
        case 5:
            print("Saliendo...")
            break
        case _:
            print("Ingrese una opción válida del 1 al 5.")