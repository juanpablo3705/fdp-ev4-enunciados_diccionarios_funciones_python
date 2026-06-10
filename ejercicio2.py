import funciones as fn
#----- sistema ppal------

alumnos = {} # dicc vacío - inicializacion del dicc - creo el dicc

while True:
    print("-- MENU ALUMNOS---")
    print("1. Agregar Alumnos")
    print("2. Mostrar Alumnos")
    print("3. Ver Promedio")
    print("4. Mejor Alumno")
    print("5. Cantidad de aprobados")
    print("6. Salir")

    while True:
        try:
            op = int(input("Inrese su opción: "))
            break
        except ValueError:
            print("Por favor ingrese un valor válido, intente nuevamente")
    
    if op == 1:
        fn.agregar_alumno(alumnos)
        # dato = input("Ingrese dato: ")
        # print(dato.isdigit())
        # if dato.isdigit():
        #     print("debe ser letras")
        # else:
        #     print("Correcto! ") //para hacerlo con todas las lineas use ctr + }
    elif op == 2:
        fn.mostrar_alumnos(alumnos)
    elif op == 3:
        fn.ver_promedios(alumnos)
    elif op == 4:
        fn.mejor_alumno(alumnos)
    elif op == 5:
        fn.cantidad_aprobados(alumnos)
    elif op == 6:
        print("Saliendo...")
        break
    else:
        print("Opción no válida!")
    
    

