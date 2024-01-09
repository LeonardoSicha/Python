a=int(input("Ingresa el extremo izquiero del intervalo: "))
b=int(input("Ingresa el extremo derecho del intervalo: "))

n=a
while n<=b:
    if n%2==0 and n%3==0 and n%5==0:
        print("El número es: {}".format(n))
        break
    n+=1

if n==b+1:
    print("No hay números divisibles entre 2,3 y 5.")    