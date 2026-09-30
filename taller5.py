TASA_ANUAL = 0.15

capital = 0
while capital <= 0:
    capital = float(input("Ingrese el capital a invertir: "))
    if capital <= 0:
        print("El capital debe ser mayor que cero.")

tasa_mensual = (1 + TASA_ANUAL) ** (1 / 12) - 1
ganancia = capital * tasa_mensual

print(f"Ganancia después de un mes: ${ganancia:,.2f}")

#ejercicio 2
sueldo_base = float(input("Ingrese el sueldo base: "))

total_ventas = 0
i = 1
while i <= 3:
    venta = float(input(f"Ingrese la venta {i}: "))
    if venta >= 0:
        total_ventas += venta
        i += 1
    else:
        print("La venta no puede ser negativa.")

comisiones = total_ventas * 0.10

print(f"Comisiones: ${comisiones:,.2f}")
print(f"Total del mes: ${sueldo_base + comisiones:,.2f}")

#ejercicio 3
compra = -1
while compra < 0:
    compra = float(input("Ingrese el total de la compra: "))
    if compra < 0:
        print("El total no puede ser negativo.")

descuento = compra * 0.15

print(f"Descuento: ${descuento:,.2f}")
print(f"Total a pagar: ${compra - descuento:,.2f}")

#ejercicio 4
suma_parciales = 0
i = 1
while i <= 3:
    nota = float(input(f"Ingrese el parcial {i}: "))
    if 0 <= nota <= 5:
        suma_parciales += nota
        i += 1
    else:
        print("La nota debe estar entre 0 y 5.")

examen = float(input("Ingrese la nota del examen final: "))
trabajo = float(input("Ingrese la nota del trabajo final: "))

promedio = suma_parciales / 3
final = promedio * 0.40 + examen * 0.50 + trabajo * 0.10

print(f"Promedio de parciales: {promedio:.2f}")
print(f"Calificación final: {final:.2f}")

#ejercicio 5
pesos = -1
while pesos < 0:
    pesos = float(input("Ingrese la cantidad en pesos: "))
    if pesos < 0:
        print("La cantidad no puede ser negativa.")

tasa = 0
while tasa <= 0:
    tasa = float(input("Ingrese cuántos pesos vale 1 dólar: "))
    if tasa <= 0:
        print("La tasa debe ser mayor que cero.")

print(f"Equivalencia: US${pesos / tasa:,.2f}")

#ejercicio 6
continuar = "s"
while continuar == "s":
    numero = float(input("Ingrese un número: "))

    if numero < 0:
        absoluto = -numero
    else:
        absoluto = numero

    print(f"El valor absoluto de {numero} es {absoluto}")
    continuar = input("¿Otro número? (s/n): ").strip().lower()
    
#ejercicio 7
presion = -1
while presion < 0:
    presion = float(input("Ingrese la presión: "))
    if presion < 0:
        print("La presión no puede ser negativa.")

volumen = -1
while volumen < 0:
    volumen = float(input("Ingrese el volumen: "))
    if volumen < 0:
        print("El volumen no puede ser negativo.")

temperatura = float(input("Ingrese la temperatura: "))

masa = (presion * volumen) / (0.37 * (temperatura + 460))

print(f"Masa de aire: {masa:.4f}")

#ejercicio 8
edad = -1
while edad < 0 or edad > 220:
    edad = float(input("Ingrese la edad: "))
    if edad < 0 or edad > 220:
        print("La edad debe estar entre 0 y 220.")

num_pulsaciones = (220 - edad) / 10

print(f"Pulsaciones por cada 10 segundos: {num_pulsaciones:.1f}")