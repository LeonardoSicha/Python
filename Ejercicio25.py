num=int(input("Introduzca la tabla de multiplicar que desea ver: "))
stop_j=int(input("Introduzca el número máximo de multiplicaciones: "))
stop_j=stop_j+1

print(f"\nTabla de multiplicar del {num}.")
for j in range(1,stop_j):
    print(f"{num} x {j} = {num*j}")