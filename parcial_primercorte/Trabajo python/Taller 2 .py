#Jen Jesús Leal Ruiz
#Juan Leguia

#¿Qué es una variable?
#Una variable es un espacio en la memoria de la computadora que se utiliza para almacenar datos.
#Ejercicios
#Punto 1
nombre = "Pepito Juarez"
edad = 31
semestre = 2
programa = "Ingeniería de Sistemas"
promedio = 4.7

print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Semestre: {semestre}")
print(f"Programa: {programa}")
print(f"Promedio: {promedio}")
#Punto 2
nombre = "Patroclo"
edad = 24
estatura = 1.73
matriculado = True

print(type(nombre))
print(type(edad))
print(type(estatura))
print(type(matriculado))
#Punto 3
nombre = input("Nombre del estudiante: ")
edad = int(input("Edad: "))
carrera = input("Carrera: ")
semestre = int(input("Semestre: "))

print(f"Hola {nombre}, tienes {edad} años, estudias {carrera} y estás en {semestre} semestre.")
#Punto 4
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

print(f"Suma: {numero1 + numero2:.0f}")
print(f"Resta: {numero1 - numero2:.0f}")
print(f"Multiplicación: {numero1 * numero2:.0f}")
print(f"División: {numero1 / numero2:.0f}")
#Punto 5
a = 10
b = 25

a, b = b, a

print(f"a = {a}")
print(f"b = {b}")

#Punto 6
nombre = input("Ingrese su nombre: ")
anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
anio_actual = int(input("Ingrese el año actual: "))

edad = anio_actual - anio_nacimiento

print(f"{nombre} tiene aproximadamente {edad} años.")

#Punto 7
nombre_producto = input("Nombre del producto: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))

subtotal = precio * cantidad

print(f"Producto: {nombre_producto}")
print(f"Precio unitario: ${precio:.0f}")
print(f"Cantidad: {cantidad}")
print(f"Total: ${subtotal:.0f}")

#Punto 8
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

promedio = (nota1 + nota2 + nota3) / 3

print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Nota 3: {nota3}")
print(f"Promedio: {promedio:.2f}")

#Punto 9
celsius = float(input("Temperatura Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32

print(f"Temperatura Celsius: {celsius:.0f}")
print(f"Temperatura Fahrenheit: {fahrenheit:.0f}")

#Punto 10
dolares = float(input("Dólares: "))
valor_dolar = float(input("Valor del dólar: "))
total_pesos = dolares * valor_dolar

print(f"Dólares: {dolares:.0f}")
print(f"Valor del dólar: {valor_dolar:.0f}")
print(f"Total en pesos colombianos: ${total_pesos:.0f}")

#Retos
#Reto1
nombre_emp = input("Nombre del empleado: ")
horas = float(input("Número de horas trabajadas: "))
valor_hora = float(input("Valor de cada hora: "))

salario = horas * valor_hora

print(f"Empleado: {nombre_emp}")
print(f"Horas trabajadas: {horas:.0f}")
print(f"Valor hora: ${valor_hora:.0f}")
print(f"Salario: ${salario:.0f}")

#Reto2
cliente = input("Nombre del cliente: ")
comida = float(input("Valor de la comida: "))
bebidas = float(input("Valor de las bebidas: "))

subtotal = comida + bebidas
propina = subtotal * 0.10
total = subtotal + propina

print(f"Cliente: {cliente}")
print(f"Subtotal: ${subtotal:.0f}")
print(f"Propina (10%): ${propina:.0f}")
print(f"Total a pagar: ${total:.0f}")

#Reto3
nombre = input("Nombre: ")
peso = float(input("Peso: "))
estatura = float(input("Estatura: "))

imc = peso / (estatura ** 2)

print(f"Nombre: {nombre}")
print(f"Peso: {peso}")
print(f"Estatura: {estatura}")
print(f"IMC: {imc:.2f}")

#Reto4
codigo = input("Código del equipo: ")
marca = input("Marca: ")
procesador = input("Procesador: ")
ram = input("Memoria RAM: ")
disco = input("Capacidad del disco: ")
so = input("Sistema operativo: ")
estado = input("Estado del equipo: ")

print(f"Código: {codigo}")
print(f"Marca: {marca}")
print(f"Procesador: {procesador}")
print(f"RAM: {ram}")
print(f"Disco: {disco}")
print(f"Sistema Operativo: {so}")
print(f"Estado: {estado}")

#Reto5
codigo = input("Código: ")
nombre = input("Estudiante: ")
edad = int(input("Edad: "))
programa = input("Programa: ")
semestre = input("Semestre: ")
materias = int(input("Materias: "))
valor_materia = float(input("Valor por materia: "))

total_matricula = materias * valor_materia

print("====================")
print("REGISTRO DE MATRÍCULA")
print(f"Código: {codigo}")
print(f"Estudiante: {nombre}")
print(f"Edad: {edad}")
print(f"Programa: {programa}")
print(f"Semestre: {semestre}")
print(f"Materias: {materias}")
print(f"Valor por materia: ${valor_materia:.0f}")
print(f"Total matrícula: ${total_matricula:.0f}")
print("====================")

#Analisis
# A: Intenta sumar una cadena de texto (str) con un número entero (int), lo que genera un error de tipo TypeError. Además, en la última línea intenta imprimir nueva edad separada por espacio, lo cual causa un error de sintaxis SyntaxError.

# B: Devuelve un tipo de dato cadena de texto (str).

# C:Convirtiendo la entrada de edad a número entero mediante int() y corrigiendo el nombre de la variable a nueva_edad.

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
nueva_edad = edad + 5
print(nombre)
print(nueva_edad)

#Mini Desafio
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = int(input("Edad: "))
ciudad = input("Ciudad: ")
universidad = input("Universidad: ")
carrera = input("Carrera: ")
semestre = input("Semestre: ")
promedio = float(input("Promedio: "))

print("==================== PERFIL DEL ESTUDIANTE ====================")
print(f"Nombre completo: {nombre} {apellido}")
print(f"Edad: {edad}")
print(f"Ciudad: {ciudad}")
print(f"Universidad: {universidad}")
print(f"Carrera: {carrera}")
print(f"Semestre: {semestre}")
print(f"Promedio: {promedio}")