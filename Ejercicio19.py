start=int(input("Ingrese el número inicial: "))
stop=int(input("Ingrese el número final: "))
step=int(input("Ingrese el número de saltos: "))

if stop<start:
    step=-step

stop = stop + 1 if step > 0 else stop - 1

for i in range(start,stop,step):
    print(i)