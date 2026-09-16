def agregar_estudiante(lista):
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    nota = float(input("Ingrese la nota: "))

    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "nota": nota
    }

    lista.append(estudiante)


def promedio_notas(lista):
    suma = 0

    for estudiante in lista:
        suma = suma + estudiante["nota"]

    promedio = suma / len(lista)

    return promedio


def mejor_estudiante(lista):
    mejor = lista[0]

    for estudiante in lista:
        if estudiante["nota"] > mejor["nota"]:
            mejor = estudiante

    return mejor


# Programa principal
estudiantes = []

cantidad = int(input("¿Cuántos estudiantes desea registrar? "))

for i in range(cantidad):
    print("\nEstudiante", i + 1)
    agregar_estudiante(estudiantes)


# Calcular promedio
promedio = promedio_notas(estudiantes)

# Buscar mejor estudiante
mejor = mejor_estudiante(estudiantes)


# Mostrar reporte
print("\n----- REPORTE FINAL -----")
print("Total estudiantes:", len(estudiantes))
print("Promedio general:", round(promedio, 1))
print("Mejor estudiante:", mejor["nombre"], "-", mejor["nota"], "-", mejor["edad"])

#ejercicio 2

def buscar_producto(inventario, codigo):
    for producto in inventario:
     if producto[0] == codigo:
        return None

def valor_total(inventario):
    total = 0
    for producto in inventario:
        precio = producto[2]
        cantidad = producto[3]

        total = total + (precio * cantidad)

    return total

def actualizar_stock(inventario, codigo, nueva_cantidad):
    for i in range(len(inventario)):
        if inventario[i][0] == codigo:

            codigo_producto = inventario[i][0]
            nombre = inventario[i][1]
            precio = inventario[i][2]


            nueva_tupla = (codigo_producto, nombre, precio, nueva_cantidad)

            inventario[i] = nueva_tupla

            return True

    return False


# Programa principal

inventario = []

cantidad_productos = int(input("¿Cuántos productos desea registrar? "))

for i in range(cantidad_productos):
    print("\nProducto", i + 1)

    codigo = input("Ingrese el código: ")
    nombre = input("Ingrese el nombre: ")
    precio = float(input("Ingrese el precio: "))
    cantidad = int(input("Ingrese la cantidad: "))

    producto = (codigo, nombre, precio, cantidad)

    inventario.append(producto)


# Actualizar un producto
codigo_buscar = input("\nIngrese el código del producto que desea actualizar: ")
nueva_cantidad = int(input("Ingrese la nueva cantidad: "))

if actualizar_stock(inventario, codigo_buscar, nueva_cantidad):
    print("Stock actualizado correctamente.")
else:
    print("Producto no encontrado.")


# Mostrar reporte
print("\n----- INVENTARIO ACTUAL -----")
print("Código\tNombre\tPrecio\tCantidad\tValor Total")

for producto in inventario:
    codigo = producto[0]
    nombre = producto[1]
    precio = producto[2]
    cantidad = producto[3]

    valor = precio * cantidad

    print(codigo, "\t", nombre, "\t", precio, "\t", cantidad, "\t\t", valor)

print("\nValor total del inventario:", valor_total(inventario))

#ejercicio 3

ventas = {
    "enero": [1200, 1500, 800, 900],
    "febrero": [1000, 1100, 1200],
    "marzo": [1800, 1700, 1600, 2000] 
}

def total_mes(ventas, mes):
    total = 0

    for ventas in ventas[mes]:
        total = total + ventas

    return total

def promedio_general(ventas):
    suma = 0
    cantidad = 0

    for mes in ventas:
        for ventas in ventas[mes]:
            suma = suma + ventas
            cantidad = cantidad + 1

    return suma / cantidad

def mejor_mes(ventas):
    mejor = ""
    mayor_total = 0

    for mes in ventas:
        total = total_mes(ventas, mes)

        if total > mayor_total:
            mayor_total = total
            mejor = mes

    return mejor


def filtrar_ventas_altas(ventas, limite):
    ventas_altas = []

    for mes in ventas:
        for venta in ventas[mes]:
            if venta > limite:
                ventas_altas.append(venta)

    return ventas_altas


# Reporte final

print("Total por mes:")
print("Enero:", total_mes(ventas, "enero"))
print("Febrero:", total_mes(ventas, "febrero"))
print("Marzo:", total_mes(ventas, "marzo"))

print("\nPromedio general trimestral:", promedio_general(ventas))

print("Mejor mes:", mejor_mes(ventas))

limite = int(input("\nIngrese el límite de ventas: "))

print("Ventas mayores al límite:", filtrar_ventas_altas(ventas, limite))



 