#Ejercicio 1
number=float(input("Ingrese un número: "))

while number!=0:
    if number%2==0:
        print("El número es par.")
        break
    else: 
        print("El número es impar.")
        break

#Ejercicio 2
s=input("Ingresa una palabra: ")
letter=input("Ingresa la letra a comprobar: ")
s=s.lower()
letter=letter.lower()

if letter in s:
     print(f"La letra {letter} se encuentra en la palabra.")
else:
     print(f"La letra {letter} no se encuentra en la palabra.")

#Ejercicio 3
price=float(input("Introduzca los precios a sumar (para finalizar introduzaca 0): "))
suma=0

while price!=0:
    suma=price+suma
    if suma>200:
        print("El presupuesto se acabó.")
        break
    price=float(input("Introduzca los precios a sumar (para finalizar introduzaca 0): "))
    if price==0:
        print(f"El total de la compra es {suma}.")
        break

#Ejercicio 4
number=int(input("Introduzca un número entero (Para salir introduce 0): "))
count_pos=0
count_neg=0

while number!=0:
    if number>0:
        count_pos+=1
    elif number<0:
        count_neg+=1
    number=int(input("Introduzca un número entero (Para salir introduce 0): "))
print(f"Haz introducido {count_pos} números positivos y {count_neg} números negativos.")

#Ejercicio 5
number=int(input("Introduzca un número entero (Para salir introduce 0): "))
count=0
media=0
suma=0

while number!=0:
    count+=1
    suma+=number
    number=int(input("Introduzca un número entero (Para salir introduce 0): "))
else:
    media=suma/count
    print(f"La media aritmética es {media}")

#Ejercicio 6
n1=int(input("Introduzca el extremo izquierdo del intervalo: "))
n2=int(input("Introduzca el extremo derecho del intervalo: "))
n2+=1

for i in range(n1,n2):
    print(i)

#Ejercicio 7
n1=int(input("Introduzca el extremo izquierdo del intervalo: "))
n2=int(input("Introduzca el extremo derecho del intervalo: "))
n2+=1
suma=0

for i in range(n1,n2):
    if i%3==0:
        suma+=i
print(f"La suma de todos los multiplos de 3 es: {suma}")

#Ejercicio 8
ni=int(input("Cuantos número piensa introducir: "))
ni+=1
product=1
for i in range(1,ni):
    number=int(input("Introduzca un número: "))
    product*=number
else:
    print(f"El producto total es: {product}")

#Ejercicio 9
age=int(input("Introduzca su edad: "))
year=int(input("Introduzca el año actual: "))
year_birth=year-age

for i in range(year_birth,year+1):
    print(i)

#Ejercicio 10
num=int(input("Introduzaca el tamaño de la figura: "))

for i in range(1,num+1):
    print("* "*i, end="")
    print(" "*(2*(num-i)), end="")
    print("* "*num)