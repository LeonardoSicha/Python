#Ejercicio 1
number=float(input("Introduzca un número: "))
if number>=0:
    if number==0:
        print("El número es 0.")
    else:
        print("El número es positivo.")
else:
    print("El número es negativo.")

#Ejercicio 2
name=input("Ingrese su nombre: ")
if len(name)>10:
    print("El nombre {} tiene más de 10 caracteres.".format(name))
else: print("El nombre {} no tiene más de 10 caracteres.".format(name))

#Ejercicio 3
name=input("Ingrese su nombre: ")
print("El nombre {} tiene más de 10 caracteres.".format(name)) if len(name)>10 else print("El nombre {} no tiene más de 10 caracteres.".format(name))

#Ejercicio 4
number1=int(input("Ingrese un primer número: "))
number2=int(input("Ingrese un segundo número: "))
if number1>=number2:
    print("El primer número ({}) es mayor o igual que el segundo número ({}).".format(number1,number2))
else:
    print("El primer número ({}) no es mayor o igul que el segundo número ({}).".format(number1,number2))

#Ejercicio 5
num1=int(input("Ingrese un primer número mayor: "))
num2=int(input("Ingrese un segundo número menor: "))
cociente=num1//num2
resto=num1%num2
if resto==0:
    print("El cociente es {} y el resto es {}.".format(cociente,resto))
    print("La division es exacta.")
else:
    print("El cociente es {} y el resto es {}.".format(cociente,resto))
    print("La division no es exacta.")

#Ejercicio 6
num1=int(input("Ingrese un primer número mayor: "))
num2=int(input("Ingrese un segundo número menor: "))
if num1>=num2:
    cociente=num1//num2
    resto=num1%num2
    if resto==0:
        print("El cociente es {} y el resto es {}.".format(cociente,resto))
        print("La division es exacta.")
    else:
        print("El cociente es {} y el resto es {}.".format(cociente,resto))
        print("La division no es exacta.")
else:
    print("El primer número debe ser mayor o igual al segundo número.")


#Ejercicio 7
num1=int(input("Ingrese un primer número: "))
num2=int(input("Ingrese un segundo número: "))
mayor=max(num1,num2)
menor=min(num1,num2)
if mayor%menor==0:
    print("El número {} es múltiplo de {}.".format(mayor,menor))
else:
    print("El número {} no es múltiplo de {}.".format(mayor,menor))

#Ejercicio 8
word=input("Introduzaca una palabra: ")
if word[0].isupper():
    print("La palabra {} empieza por mayúscula.".format(word))
else:
    print("La palabra {} no empieza por mayúscula.".format(word))

#Ejercicio 9
letter=input("Introduzaca una letra: ")
if len(letter)==1:
    letter=letter.lower()
    if letter in ["a","e","i","o","u"]:
        print("El caracter ingresado es la vocal {}".format(letter))
    else:
        print("El caracter ingresado no es una vocal, es la consonate {}.".format(letter))
else:
    print("El dato ingresado tiene que tener un solo caracter.")

#Ejercicio 10
a=float(input("Ingresa la coeficiente a: "))
c=float(input("Ingresa la coeficiente c: "))
b=float(input("Ingresa la coeficiente b: "))

from math import sqrt

if a!=0:
    discriminante=(b**2)-4*a*c
    if discriminante>0:
        print("La ecuación tiene dos soluciones reales diferentes.")
        x1=(-b+sqrt(discriminante))/(2*a)
        x2=(-b-sqrt(discriminante))/(2*a)
        print("Las soluciones son {} y {}.".format(x1,x2))
    elif discriminante==0:
        print("La ecuación tiene dos soluciones reales iguales.")
        x=(-b)/(2*a)
        print("La solución es {}.".format(x))
    else:
        print("La ecuación no tiene soluciones reales.")
else:
    print("No hay solución. El coeficiente 'a' debe ser distinto de 0.")