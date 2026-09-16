#1
while True:
  # Solicitamos los tres lados
  lado1 = float(input("Ingrese la longitud del primer lado: "))
  lado2 = float(input("Ingrese la longitud del segundo lado: "))
  lado3 = float(input("Ingrese la longitud del tercer lado: "))

 
  if lado1 > 0 and lado2 > 0 and lado3 > 0:
    break  # Salimos del ciclo si la validación es correcta
  else:
    print("Error: Todos los lados deben ser mayores a cero. Intente de nuevo.\n")

if (
    (lado1 + lado2 > lado3)
    and (lado1 + lado3 > lado2)
    and (lado2 + lado3 > lado1)
):
  print("\n¡Los valores ingresados SÍ forman un triángulo!")

  if lado1 == lado2 and lado2 == lado3:
    print("Clasificación: Triángulo **Equilátero** (todos sus lados iguales).")
  elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Clasificación: Triángulo **Isósceles** (dos lados iguales).")
  else:
    print("Clasificación: Triángulo **Escaleno** (todos sus lados diferentes).")
else:
  print(
      "\nLos valores ingresados NO cumplen con la condición de existencia"
      " (la suma de dos lados debe ser mayor al tercero)."
  )
  
#2
while True:
  cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
  if cantidad_estudiantes > 0:
    break
  print("Error: La cantidad de estudiantes debe ser mayor a cero.")

contador_aprobados = 0
contador_reprobados = 0
suma_promedios_grupo = 0
promedio_mas_alto = -1.0
promedio_mas_bajo = 6.0

for i in range(1, cantidad_estudiantes + 1):
  print(f"\nEstudiante {i}")
  suma_calificaciones = 0

  for j in range(1, 4):
    while True:
      calificacion = float(input(f"Ingrese la calificación {j} (0.0 a 5.0): "))
      if 0.0 <= calificacion <= 5.0:
        break
      print("Error: La calificación debe estar entre 0.0 y 5.0.")
    suma_calificaciones += calificacion

  promedio_estudiante = suma_calificaciones / 3
  suma_promedios_grupo += promedio_estudiante

  if promedio_estudiante <= 2.9:
    clasificacion = "Reprobado"
    contador_reprobados += 1
  elif promedio_estudiante <= 3.9:
    clasificacion = "Aprobado"
    contador_aprobados += 1
  elif promedio_estudiante <= 4.5:
    clasificacion = "Sobresaliente"
    contador_aprobados += 1
  else:
    clasificacion = "Excelente"
    contador_aprobados += 1

  print(f"Promedio: {promedio_estudiante:.2f} - Clasificación: {clasificacion}")

  if promedio_estudiante > promedio_mas_alto:
    promedio_mas_alto = promedio_estudiante

  if promedio_estudiante < promedio_mas_bajo:
    promedio_mas_bajo = promedio_estudiante

promedio_general = suma_promedios_grupo / cantidad_estudiantes

print("\n--- RESULTADOS FINALES DEL GRUPO ---")
print(f"Cantidad de estudiantes aprobados: {contador_aprobados}")
print(f"Cantidad de estudiantes reprobados: {contador_reprobados}")
print(f"Promedio general del grupo: {promedio_general:.2f}")
print(f"Promedio más alto: {promedio_mas_alto:.2f}")
print(f"Promedio más bajo: {promedio_mas_bajo:.2f}")

#3
saldo = 1500000.0
depositos_count = 0
retiros_count = 0
movimientos = []

while True:
  print("\n--- CAJERO AUTOMÁTICO ---")
  print("1. Consultar saldo")
  print("2. Depositar dinero")
  print("3. Retirar dinero")
  print("4. Ver movimientos realizados")
  print("5. Salir")
  
  opcion = input("Seleccione una opción: ")

  if opcion == "1":
    print(f"Saldo actual: ${saldo:,.2f}")

  elif opcion == "2":
    while True:
      deposito = float(input("Ingrese la cantidad a depositar: "))
      if deposito > 0:
        saldo += deposito
        depositos_count += 1
        movimientos.append(f"Depósito: +${deposito:,.2f}")
        print("Depósito realizado con éxito.")
        break
      print("Error: No se permiten depósitos negativos o en cero.")

  elif opcion == "3":
    while True:
      retiro = float(input("Ingrese la cantidad a retirar (Mínimo $10.000): "))
      if retiro >= 10000:
        if (retiro + 4500) <= saldo:
          saldo -= (retiro + 4500)
          retiros_count += 1
          movimientos.append(f"Retiro: -${retiro:,.2f} (Costo: $4,500)")
          print("Retiro realizado con éxito. Se cobró una comisión de $4.500.")
          break
        else:
          print("Error: Saldo insuficiente para cubrir el retiro y el costo de $4.500.")
          break
      else:
        print("Error: La cantidad mínima a retirar es de $10.000.")

  elif opcion == "4":
    print("\n--- MOVIMIENTOS REALIZADOS ---")
    if len(movimientos) == 0:
      print("No se han realizado movimientos.")
    else:
      for mov in movimientos:
        print(mov)
    print(f"Total de depósitos: {depositos_count}")
    print(f"Total de retiros: {retiros_count}")

  elif opcion == "5":
    print("Gracias por usar el cajero automático.")
    break

  else:
    print("Opción inválida. Intente de nuevo.")
    
#4
while True:
  numero = int(input("Ingrese un número entero mayor que 1: "))
  if numero > 1:
    break
  print("Error: El número debe ser mayor que 1.")

divisores = []
for i in range(1, numero + 1):
  if numero % i == 0:
    divisores.append(i)

print(f"Divisores: {', '.join(map(str, divisores))}")

if len(divisores) == 2:
  print(f"El número {numero} es primo.")
else:
  print(f"El número {numero} no es primo.")
  
#5
while True:
  cantidad_productos = int(input("Ingrese la cantidad de productos comprados: "))
  if cantidad_productos > 0:
    break
  print("Error: La cantidad de productos debe ser mayor a cero.")

subtotal_general = 0
total_descuentos_productos = 0
detalles_productos = []

for i in range(1, cantidad_productos + 1):
  print(f"\nProducto {i}")
  nombre = input("Nombre del producto: ")
  
  while True:
    precio = float(input("Precio unitario: "))
    if precio > 0:
      break
    print("Error: El precio debe ser mayor a cero.")

  while True:
    cantidad = int(input("Cantidad: "))
    if cantidad > 0:
      break
    print("Error: La cantidad debe ser mayor a cero.")

  while True:
    tipo = input("Tipo de producto (alimento / aseo / otro): ").strip().lower()
    if tipo in ["alimento", "aseo", "otro"]:
      break
    print("Error: Tipo inválido. Ingrese alimento, aseo u otro.")

  subtotal_producto = precio * cantidad
  descuento_producto = 0

  if tipo == "alimento":
    descuento_producto = subtotal_producto * 0.05
  elif tipo == "aseo" and cantidad >= 3:
    descuento_producto = subtotal_producto * 0.10

  subtotal_general += subtotal_producto
  total_descuentos_productos += descuento_producto

  detalles_productos.append({
      "nombre": nombre,
      "subtotal": subtotal_producto,
      "descuento": descuento_producto
  })

descuento_general = 0
if subtotal_general > 300000:
  descuento_general = subtotal_general * 0.05

total_descuentos = total_descuentos_productos + descuento_general
total_definitivo = subtotal_general - total_descuentos

print("\n--- FACTURA DE SUPERMERCADO ---")
for prod in detalles_productos:
  print(f"Producto: {prod['nombre']}")
  print(f"  Subtotal: ${prod['subtotal']:,.2f}")
  print(f"  Descuento aplicado: ${prod['descuento']:,.2f}")

print(f"\nTotal antes del descuento general: ${subtotal_general:,.2f}")
print(f"Total de descuentos: ${total_descuentos:,.2f}")
print(f"Total definitivo: ${total_definitivo:,.2f}")

#6
cantidad = 0
positivos = 0
negativos = 0
pares = 0
impares = 0
suma = 0
mayor = None
menor = None

while True:
  numero = int(input("Ingrese un número entero (0 para terminar): "))
  if numero == 0:
    break
  
  cantidad += 1
  suma += numero
  
  if numero > 0:
    positivos += 1
  else:
    negativos += 1
    
  if numero % 2 == 0:
    pares += 1
  else:
    impares += 1
    
  if mayor is None or numero > mayor:
    mayor = numero
    
  if menor is None or numero < menor:
    menor = numero

if cantidad == 0:
  print("No se ingresaron números (el primer número ingresado fue 0).")
else:
  promedio = suma / cantidad
  print("\n--- ESTADÍSTICAS DE NÚMEROS ---")
  print(f"Cantidad de números ingresados: {cantidad}")
  print(f"Cantidad de positivos: {positivos}")
  print(f"Cantidad de negativos: {negativos}")
  print(f"Cantidad de pares: {pares}")
  print(f"Cantidad de impares: {impares}")
  print(f"Suma total: {suma}")
  print(f"Promedio: {promedio:.2f}")
  print(f"Número mayor: {mayor}")
  print(f"Número menor: {menor}")
  
#7
while True:
  numero = int(input("Ingrese un número entero positivo: "))
  if numero >= 0:
    break
  print("Error: El número debe ser positivo o cero.")

if numero == 0:
  binario = "0"
else:
  binario = ""
  temporal = numero
  while temporal > 0:
    residuo = temporal % 2
    binario = str(residuo) + binario
    temporal = temporal // 2

print(f"Resultado binario: {binario}")

#8
while True:
  cantidad = int(input("Ingrese la cantidad de términos (mayor o igual a 1): "))
  if cantidad >= 1:
    break
  print("Error: La cantidad de términos debe ser al menos 1.")

serie = []
suma = 0
pares = 0
impares = 0

if cantidad == 1:
  serie = [0]
else:
  a = 0
  b = 1
  serie = [a, b]
  for i in range(2, cantidad):
    siguiente = a + b
    serie.append(siguiente)
    a = b
    b = siguiente

for num in serie:
  suma += num
  if num % 2 == 0:
    pares += 1
  else:
    impares += 1

print("\n--- SERIE DE FIBONACCI ---")
print(f"La serie completa: {', '.join(map(str, serie))}")
print(f"La suma de sus términos: {suma}")
print(f"Cuántos términos son pares: {pares}")
print(f"Cuántos términos son impares: {impares}")

#9
pares = 0
impares = 0
mayores_50 = 0

for i in range(1, 11):
  print(f"\nTABLA DEL {i}")
  for j in range(1, 11):
    resultado = i * j
    print(f"{i} × {j} = {resultado}")
    
    if resultado % 2 == 0:
      pares += 1
    else:
      impares += 1
      
    if resultado > 50:
      mayores_50 += 1

print("\n--- RESUMEN FINAL ---")
print(f"Cantidad de resultados pares: {pares}")
print(f"Cantidad de resultados impares: {impares}")
print(f"Cantidad de resultados mayores que 50: {mayores_50}")

#10
while True:
  n = int(input("Ingrese un número entre 3 y 10: "))
  if 3 <= n <= 10:
    break
  print("Error: El número debe estar entre 3 y 10.")

for i in range(1, 2 * n):
  limite = i if i <= n else 2 * n - i
  for j in range(1, limite + 1):
    print(j, end=" ")
  print()
  
#11
import random

while True:
  print("\n--- JUEGO DE ADIVINANZA ---")
  print("1. Fácil (1 a 20, 6 intentos)")
  print("2. Intermedio (1 a 50, 5 intentos)")
  print("3. Difícil (1 a 100, 4 intentos)")
  opcion = input("Seleccione la dificultad: ")

  if opcion == "1":
    rango_max = 20
    intentos = 6
    break
  elif opcion == "2":
    rango_max = 50
    intentos = 5
    break
  elif opcion == "3":
    rango_max = 100
    intentos = 4
    break
  else:
    print("Opción inválida. Intente de nuevo.")

numero_secreto = random.randint(1, rango_max)
adivinado = False
intentos_restantes = 0

for i in range(1, intentos + 1):
  intento_actual = int(input(f"Intento {i}/{intentos} - Ingrese un número: "))

  if intento_actual == numero_secreto:
    print("Número correcto")
    intentos_restantes = intentos - i
    adivinado = True
    break
  elif intento_actual < numero_secreto:
    print("El número secreto es mayor")
  else:
    print("El número secreto es menor")

if adivinado:
  puntaje = intentos_restantes * 20
  print(f"¡Ganaste! Puntaje obtenido: {puntaje}")
else:
  print(f"Perdiste. El número secreto era: {numero_secreto}")
  print("Puntaje obtenido: 0")
  
#12
usuario_correcto = "administrador"
clave_correcta = "Python2026"
intentos_restantes = 3
acceso_concedido = False

while intentos_restantes > 0:
  usuario = input("Ingrese el usuario: ")
  clave = input("Ingrese la contraseña: ")

  if usuario == usuario_correcto and clave == clave_correcta:
    acceso_concedido = True
    break
  else:
    intentos_restantes -= 1
    if intentos_restantes > 0:
      print(f"Datos incorrectos. Te quedan {intentos_restantes} intentos.")
    else:
      print("Sistema bloqueado por exceder el número de intentos.")

if acceso_concedido:
  while True:
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Consultar información")
    print("2. Cambiar contraseña")
    print("3. Cerrar sesión")
    
    opcion_menu = input("Seleccione una opción: ")

    if opcion_menu == "1":
      print("Información del sistema: Acceso autorizado.")
    elif opcion_menu == "2":
      actual = input("Ingrese la contraseña actual: ")
      if actual == clave_correcta:
        nueva = input("Ingrese la nueva contraseña: ")
        clave_correcta = nueva
        print("Contraseña cambiada con éxito.")
      else:
        print("Contraseña actual incorrecta.")
    elif opcion_menu == "3":
      print("Sesión cerrada.")
      break
    else:
      print("Opción inválida.")
      
#RETO INTEGRADO
opcion = 0
cantidad_ventas = 0
total_bruto = 0
total_descuentos = 0
total_recargos = 0
total_recibido = 0

clientes_con_descuento = 0
venta_mayor = None
venta_mayor_cliente = ""
venta_menor = None
venta_menor_cliente = ""

pagos_efectivo = 0
pagos_tarjeta = 0
pagos_transferencia = 0

while opcion != 5:
    print("\nSISTEMA DE VENTAS")
    print("1. Registrar una venta")
    print("2. Consultar resumen")
    print("3. Consultar venta mayor y menor")
    print("4. Cerrar caja")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        nombre = input("Nombre del cliente: ")
        
        while True:
            cantidad = int(input("Cantidad de productos: "))
            if cantidad > 0:
                break
            print("Error: La cantidad debe ser positiva.")

        while True:
            precio_unitario = float(input("Precio de cada producto: "))
            if precio_unitario > 0:
                break
            print("Error: El precio debe ser positivo.")

        while True:
            medio_pago = input("Medio de pago (efectivo / tarjeta / transferencia): ").strip().lower()
            if medio_pago in ["efectivo", "tarjeta", "transferencia"]:
                break
            print("Error: Medio de pago inválido.")

        subtotal_venta = cantidad * precio_unitario
        total_bruto += subtotal_venta

        descuento_actual = 0
        recargo_actual = 0
        recibe_descuento = False

        if subtotal_venta > 500000:
            descuento_actual += subtotal_venta * 0.10
            recibe_descuento = True

        if medio_pago == "efectivo":
            pagos_efectivo += 1
            if subtotal_venta > 200000:
                descuento_actual += subtotal_venta * 0.03
                recibe_descuento = True
        elif medio_pago == "tarjeta":
            pagos_tarjeta += 1
            recargo_actual += subtotal_venta * 0.02
        else:
            pagos_transferencia += 1

        if recibe_descuento:
            clientes_con_descuento += 1

        total_descuentos += descuento_actual
        total_recargos += recargo_actual

        total_final_venta = subtotal_venta - descuento_actual + recargo_actual
        total_recibido += total_final_venta
        cantidad_ventas += 1

        if venta_mayor is None or total_final_venta > venta_mayor:
            venta_mayor = total_final_venta
            venta_mayor_cliente = nombre

        if venta_menor is None or total_final_venta < venta_menor:
            venta_menor = total_final_venta
            venta_menor_cliente = nombre

        print("¡Venta registrada con éxito!")

    elif opcion == 2:
        if cantidad_ventas == 0:
            print("No se pueden consultar estadísticas, todavía no existen ventas.")
        else:
            promedio = total_recibido / cantidad_ventas
            print("\n--- RESUMEN DE VENTAS ---")
            print(f"Cantidad de ventas realizadas: {cantidad_ventas}")
            print(f"Valor total antes de descuentos: ${total_bruto:,.2f}")
            print(f"Total de descuentos: ${total_descuentos:,.2f}")
            print(f"Total de recargos: ${total_recargos:,.2f}")
            print(f"Dinero definitivo recibido: ${total_recibido:,.2f}")
            print(f"Promedio de las ventas: ${promedio:,.2f}")
            print(f"Cantidad de pagos en efectivo: {pagos_efectivo}")
            print(f"Cantidad de pagos con tarjeta: {pagos_tarjeta}")
            print(f"Cantidad de pagos por transferencia: {pagos_transferencia}")
            print(f"Cantidad de clientes que recibieron descuento: {clientes_con_descuento}")

    elif opcion == 3:
        if cantidad_ventas == 0:
            print("No se pueden consultar estadísticas, todavía no existen ventas.")
        else:
            print("\n--- VENTA MAYOR Y MENOR ---")
            print(f"Venta más alta: ${venta_mayor:,.2f} (Cliente: {venta_mayor_cliente})")
            print(f"Venta más baja: ${venta_menor:,.2f} (Cliente: {venta_menor_cliente})")

    elif opcion == 4:
        if cantidad_ventas == 0:
            print("No hay ventas para realizar el cierre de caja.")
        else:
            print("\n--- CIERRE DE CAJA ---")
            print(f"Total de transacciones: {cantidad_ventas}")
            print(f"Dinero total recibido en caja: ${total_recibido:,.2f}")
            print("Cierre de caja aplicado correctamente.")

    elif opcion == 5:
        print("Programa finalizado.")

    else:
        print("Opción inválida.")
