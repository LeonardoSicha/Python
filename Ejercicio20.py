start=int(input("Introduce el término inicial de una progresión aritmética: "))
stop=int(input("Indica la cota para finalizar: "))
step=int(input("Introduce la diferencia de dicha progresión aritmética: "))
suma=0
stop=stop+1

for i in range(start,stop,step):
    print(i)
    suma+=i
print(f"La suma de los términos de la sucesión que has indicado es: {suma}")