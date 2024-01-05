x=float(input("Ingrese la coordenada en x: "))
y=float(input("Ingrese la coordenada en y: "))

if x>=0 and x<=1 and y>=0 and y<=1:
    print("El punto ({}, {}) se encuentra en el cuadro unidad.".format(x,y))
else:
    print("El punto ({}, {}) no se encuentra en el cuadro unidad.".format(x,y))    