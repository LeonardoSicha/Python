s=input("Ingresa una frase: ")
c=input("Ingresa el caracter a contar: ")
if c in s:
    print("EL string tiene {} veces el caracter ingresado.".format(s.count(c)))