numbre=float(input("Introduzca un número: "))
suma=0

while numbre!=0:
    suma+=numbre
    numbre=float(input("Introduzca un número: "))
else:
    print(f"La suma total es: {suma}")