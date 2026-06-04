# inicializar diccionario vacío:
diccionario_productos = {}

# 1 funcion agregar productos:
def agregar_producto(diccionario_productos):

    nombre_producto = input("Ingrese el nombre del producto: ")
    if (nombre_producto == "") or (nombre_producto in diccionario_productos):
        print("Error, el nombre no puede estar vacío ni ser el mismo de otro ya existente.")
        return

    while True:
        try:
            stock_producto = int(input("Ingrese el stock del producto: "))
            if stock_producto < 0:
                print("Error, el stock debe ser mayor o igual a cero.")
            else:
                break
        except ValueError:
            print("Error, el valor debe ser numérico, no letras.")
    
    while True:
        try:
            precio_producto = float(input("Ingrese el precio del producto: "))
            if precio_producto <= 0:
                print("Error, el precio debe ser mayor que cero.")
            else:
                break
        except ValueError:
            print("Error, el valor debe ser numérico, no letras.")

    diccionario_productos[nombre_producto] = [stock_producto, precio_producto]

# 2 funcion mostrar productos:
def mostrar_productos(diccionario_productos):

    if len(diccionario_productos) == 0:
        print("Error, no se han agregado productos, seleccione la opcion 1.")
    else:
        for nombre_producto in diccionario_productos:
            stock = diccionario_productos[nombre_producto][0]
            precio = diccionario_productos[nombre_producto][1]
            print(f"Producto: {nombre_producto}. Stock: {stock}. Precio: {precio}.")

# 3 funcion buscar productos:
def buscar_producto(diccionario_productos):

    if len(diccionario_productos) == 0:
        print("Error, no se han agregado productos, seleccione la opcion 1.")
    else:
        producto_buscar = input("Ingrese el producto a buscar: ").strip()
        if producto_buscar == "":
            print("Error, debe ingresar un producto.")
            return
        else:
            if producto_buscar in diccionario_productos:
                print(f"Producto encontrado: {producto_buscar} existe en el registro.")
            else:
                print(f"No está el producto {producto_buscar}.")

# 4 funcion producto mas caro:
def producto_mas_caro(diccionario_productos):

    if len(diccionario_productos) == 0:
        print("Error, no se han agregado productos, seleccione la opcion 1.")
    else:
        mayor_precio = 0
        mayor_nombre = ""
        for nombre_producto in diccionario_productos:
            precio = diccionario_productos[nombre_producto][1] # llamando un elemento del diccionario
            if precio > mayor_precio:
                mayor_precio = precio
                mayor_nombre = nombre_producto
        print(f"Producto mas caro: {mayor_nombre}. Precio: {mayor_precio}.")

# menú principal:
while True:

    print("----- MENU -----")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Producto mas caro")
    print("5. Salir")

    while True:
        try:
            opcion_menu = int(input("Ingrese una opción del menú: "))
            break
        except ValueError:
            print("Error. Debe elegir sólo números entre 1 y 5")

    match opcion_menu:
        case 1:
            agregar_producto(diccionario_productos)
        case 2:
            mostrar_productos(diccionario_productos)
        case 3:
            buscar_producto(diccionario_productos)
        case 4:
            producto_mas_caro(diccionario_productos)
        case 5:
            print("Saliendo...")
            break
        case _:
            print("Error. Debe elegir una opción del 1 al 5.")