import funciones as fn

# codigo ppal

productos = {} #diccionario vacío

while True:
    print("----  MENU ----")
    print("1. Agregar Producto")
    print("2. Mostrar Productos")
    print("3. Buscar Productos")
    print("4. Producto mas caro")
    print("5. Salir")

    while True:
        try:
            op = int(input("Ingrese la opción: "))
            break
        except ValueError:
            print("Debe ingresar un opción válida (1-5), intente nuevamente")

    if op == 1 :
        fn.agregar_producto(productos)
        
    elif op == 2:
        fn.mostrar_productos(productos)
        #print(productos)
    elif op == 3 :
        fn.buscar_producto(productos)
        #print("buscar")
    elif op == 4:
        fn.producto_mas_caro(productos)
        #print("más caro")
    elif op == 5:
        print("Fin del programa")
        break
    else:
        print("Opción no válida")






