#print("Hello, World!")
#X, Y, Z = "Azul", "Rojo", "Verde"
#print(X)
#print(Y)
#print(Z)
#x = "python"
#y = "es un"
#z = "lenguaje de programación"
#print(x, y, z)
#a = 1
#b = 1.2
#c = "hola"
#d = True
#e = [1, 2, 3, 4, 5]
#print(a, type(a))
#print(b, type(b))
#print(c, type(c))
#print(d, type(d))
#print(e, type(e))
#x = 1
#y = 2.8
#z = 1j
#print(type(x))
#print(type(y))
#print(type(z))
#x = 35e3
#y = 12E4
#z = -87.7e100
#print(type(x))
#print(type(y))
#print(type(z))
#x = 3+5j
#y = 5j
#z = -5j
#print(type(x))
#print(type(y))
#print(type(z))
#x = 1
#y = 2.8
#z = 1j
#a = float(x)
#b = int(y)
#c = complex(x)
#print (a)
#print (b)
#print (c)
#print(type(a))
#print(type(b))
#print(type(c))
#print(10 > 9)
#print(10 == 9)
#print(10 < 9)
#print(bool("Hola"))
#print(bool(15))

##Taller
a = 10
b = 3.1416
c = "Hola Python"
d = True
e = [1, 2, 3]
f = (4, 5, 6)
g = {7, 8, 9}
h = {"clave": "valor"}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))

print("Suma", 5 + 3)
print("Resta:", 10 - 4)
print("Multiplicación:", 4 * 2)
print("División:", 10 / 2)
print("División entera:", 10 // 3)
print("Módulo:", 10 % 3)
print("Potencia:", 2 ** 3)

print(5 == 5)
print(5 != 3)
print(5 > 3)
print(3 < 5)
print(5 >= 5)
print(3 <= 5)

print(5 & 3)
print(5 | 3)
print(5 ^ 3)
print(~5)
print(5 << 1)
print(5 >> 1)

x = 10
x += 1
print(x)
print(1 in [1, 2])
print(3 not in [1, 2])
print(True is True)
print(True is not False)

valores = [True, False]

print("TABLA DE VERDAD AND")
for a in valores:
    for b in valores:
        print(f"{a} AND {b} = {a and b}")

print("\nTABLA DE VERDAD OR")
for a in valores:
    for b in valores:
        print(f"{a} OR {b} = {a or b}")

print("\nTABLA DE VERDAD NOT")
for a in valores:
    print(f"NOT {a} = {not a}")

z1 = 3 + 4j
z2 = complex(2, -5)
suma = z1 + z2
print("SUMA DE NÚMEROS COMPLEJOS")
print(z1)
print(z2)
print(suma)
print(suma.real)
print(suma.imag)