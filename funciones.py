# funciones para ejercicio1.py y ejercicio2.py (desde profesor)

'''productos = {
    "Mouse":"[10,1500]",
    "Teclado" : [5,2500],
    "Monitor" : [3,180000]
}'''
def agregar_producto(productos):
    nombre = input("Nombre del producto: ").strip().lower()

    if nombre == "":
        print("El nombre no puede ser vacío")
        return
    
    if nombre in productos:
        print("El producto ya existe!")
        return

    stock = int(input("Ingrese stock: "))
    precio = int(input("Ingrese precio $: "))

    productos[nombre] = [stock,precio]
    print("Producto agregado correctamente!")

def mostrar_productos(productos):
    if len(productos) == 0:
        print("No existen productos")
        return

    for nombre in productos:
        print(nombre,"-Stock: ",productos[nombre][0],"-Precio : $",productos[nombre][1])

def buscar_producto(productos):
    if len(productos) == 0:
        print("No existen productos")
        return
    
    nombre = input("Ingrese nombre del producto a buscar: ").strip().lower()

    if nombre in productos:
        print("Producto encontrado!")
        print(f"Stock: {productos[nombre][0]}")
        print(f"Precio $: {productos[nombre][1]}")

    else:
        print("Producto no existe o esta agotado!")

def producto_mas_caro(productos):
    if len(productos) == 0:
        print("No existen productos")
        return
    
    mayor = 0
    nombreMayor = ""
    for nombre in productos:
        precio = productos[nombre][1]

        if precio > mayor:
            mayor = precio
            nombreMayor = nombre

    print(f"Producto mas caro es: {nombreMayor}")
    print(f"Su precio es: ${mayor}")

# ----- ejercicio 2 ---- 

def agregar_alumno(alumnos):
    '''en esta funcion ingresaremos un nombre alumno con sus notas'''
    nombre = input("Ingrese nombre del alumno: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacío")
        return

    if nombre in alumnos:
        print("El alumno ya existe")
        return
    
    if nombre.isdigit():
        print("El nombre debe ser con letras! ")
        return
    
    while True:
        try:
            cantidad = int(input("Ingrese cantidad de notas: "))
            break
        except ValueError:
            print("Ingrese un numero válido y entero")

    notas = []

    for i in range(cantidad):
        print(f"Ingresando nota {i+1}/{cantidad}")
        notaParcial = validaNota()
        notas.append(notaParcial)

    alumnos[nombre] = notas    
    print("Alumno agregado correctamente!")


def validaNota():
    while True:
        try:
            nota = float(input("Ingrese nota: "))
            if nota >=1.0 and nota <= 7.0:
                return nota
            else:
                print("La nota debe estar entre 1.0 y 7.0")
        except ValueError:
            print("Debe ingresar un valor válido!")


def mostrar_alumnos(alumnos):
    if len(alumnos) == 0:
        print("No hay alumnos registrados!")
        return

    for nombre in alumnos:
        print(nombre, ":",alumnos[nombre])

def ver_promedios(alumnos):
    if len(alumnos) == 0:
        print("No hay alumnos registrados!")
        return
    
    for nombre in alumnos:
        promedio = sum(alumnos[nombre])/len(alumnos[nombre])
        print(f"{nombre}, tiene un promedio de : {round(promedio,2)}")

def mejor_alumno(alumnos):
    if len(alumnos) == 0:
        print("No hay alumnos registrados!")
        return
    
    mayor = 0
    mejorAlumno = ""
    for nombre in alumnos:
        promedio = sum(alumnos[nombre])/len(alumnos[nombre])

        if promedio > mayor:
            mayor = promedio
            mejorAlumno = nombre
    print(f"Mejor alumno: {mejorAlumno}, con promedio: {round(mayor,2)}")

def cantidad_aprobados(alumnos):
    if len(alumnos) == 0:
        print("No hay alumnos registrados!")
        return

    aprobados = 0
    for nombre in alumnos:
         promedio = sum(alumnos[nombre])/len(alumnos[nombre])

         if promedio >=4.0:
             aprobados = aprobados + 1 # aprobados +=1

    print(f"la cantidad de aprobados es: {aprobados}")
