#Taller= JUAN LEGUIA TORREGROSA
#1R// Se utiliza la funcion input() para solicitar datos al usuario y almacenarlos en variables.()
#2R// Devuelve siempre una cadena de texto (str)
#3R// int() convierte un valor a un número entero, float() convierte un valor a un numero decimal (punto flotante)
#4R// Sirve para conectar (unir) dos o mas cadenas de texto
#5R// El operador (/) realiza una division flotante (devuelve el resultado con decimales) y el operador (//) realiza una division entera (devuelve el resultado sin decimales), mientras que (//) realiza una dision entera (elimina pate decimal)

#PARTE 2 EJERCICIOS
#1
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
ciudad = input("Ingrese su ciudad: ")
print(f"Hola {nombre}, tienes {edad} años y vives en {ciudad}.")

#2
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
suma = numero1 + numero2
print(f"La suma de {numero1} y {numero2} es: {suma}")

#3
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
print(f"suma: {numero1 + numero2}")
print(f"resta: {numero1 - numero2}")
print(f"multiplicación: {numero1 * numero2}")
print(f"división: {numero1 / numero2 if numero2 != 0 else 'Error: División por cero'}")

#4
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
promedio = (nota1 + nota2 + nota3) / 3
print(f"El promedio de las notas es:", promedio)

#5
nombre = input("Ingrese su nombre: ")
apellido1 = input("Ingrese su apellido: ")
apellido2 = input("Ingrese su segundo apellido: ")
print(f"Su nombre completo es: {nombre} {apellido1} {apellido2}")

#6
edad = int(input("Ingrese su edad: "))
meses = edad * 12
print(f"Su edad en meses es: {meses} meses")

#7
base = float(input("Ingrese la base "))
altura = float(input("Ingrese la altura "))
area = (base * altura)
print(f"El área es: {area}")

#8
radio = float(input("Ingrese el radio: "))
area = 3.1416 * (radio ** 2)
print(f"El área del círculo es: {area}")

#9
producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad: "))
total = precio * cantidad
print(f"Total a pagar: ${total}")

#10
empleado = input("Ingrese el nombre del empleado: ")
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
valor_hora = float(input("Ingrese el valor por hora: "))
sueldo = horas_trabajadas * valor_hora
print(f"empleado: {empleado}, sueldo a pagar: ${sueldo}")

#Parte 3 cadenas
#11
texto = input("Ingrese una palabra: ")
print(texto.upper())
print(texto.lower())

#12
nombre_completo = input("Ingrese su nombre completo: ")
print(f"cantidad de caracteres: {len(nombre_completo)}")

#13
nombre = input("Ingrese su nombre: ")
carrera = input("Ingrese su carrera: ")
universidad = input("Ingrese su universidad: ")
print(f"Nombre: {nombre}, Carrera: {carrera}, Universidad: {universidad}")

#parte 4 Retos praticos
#Reto 1
cliente = input("Ingrese el nombre del cliente: ")
comida = float(input("Ingrese el precio de la comida: "))
bebida = float(input("Ingrese el precio de la bebida: "))
persona = int(input("cantidad de personas: "))
total_cuenta = (comida + bebida)
valor_persona = total_cuenta / persona if personas > 0 else 0
print(f"total de la cuenta: ${total_cuenta}")
print(f"valor por persona: ${valor_persona}")

#Reto 2
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"Temperatura en Fahrenheit: {fahrenheit}°F")

#Reto 3
pesos = float(input("Ingrese la cantidad en pesos colombianos: "))
valor_dolar = float(input("Ingrese el valor del dólar: "))
total_dolares = pesos / valor_dolar if valor_dolar > 0 else 0
print(f"Total en dólares: ${total_dolares:.2f}")

#Reto 4
vendedor = input("Nombre del vendedor: ")
cliente = input("Nombre del cliente: ")
producto = input("Producto: ")
cantidad = int(input("Cantidad: "))
precio_unitario = float(input("Precio unitario: "))

subtotal = cantidad * precio_unitario
descuento = subtotal * 0.10
subtotal_con_descuento = subtotal - descuento
iva = subtotal_con_descuento * 0.19
total_final = subtotal_con_descuento + iva

print("\n========= VENTA =========")
print(f"Vendedor: {vendedor}")
print(f"Cliente: {cliente}")
print(f"Producto: {producto}")
print(f"Cantidad: {cantidad}")
print(f"\nSubtotal: ${subtotal}")
print(f"Descuento: ${descuento}")
print(f"IVA: ${iva}")
print(f"\nTOTAL A PAGAR: ${total_final}")

#Reto 5
vendedor = input("Nombre del vendedor: ")
cliente = input("Nombre del cliente: ")
producto = input("Producto: ")
cantidad = int(input("Cantidad: "))
precio_unitario = float(input("Precio unitario: "))

subtotal = cantidad * precio_unitario
descuento = subtotal * 0.10
subtotal_con_descuento = subtotal - descuento
iva = subtotal_con_descuento * 0.19
total_final = subtotal_con_descuento + iva

print("\n========= VENTA =========")
print(f"Vendedor: {vendedor}")
print(f"Cliente: {cliente}")
print(f"Producto: {producto}")
print(f"Cantidad: {cantidad}")
print(f"\nSubtotal: ${subtotal}")
print(f"Descuento: ${descuento}")
print(f"IVA: ${iva}")
print(f"\nTOTAL A PAGAR: ${total_final}")

