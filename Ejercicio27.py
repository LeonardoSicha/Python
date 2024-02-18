lista=[]
numero = int(input("Coloca el número que quieres ingresar a la lista: "))
lista.append(numero)
respuesta=input("Quieres agregar otro numero? ")
respuesta=respuesta.lower()
while respuesta=="si":
    numero = int(input("Coloca el número que quieres ingresar a la lista: "))
    lista.append(numero)
    respuesta=input("Quieres agregar otro numero? ")
    respuesta=respuesta.lower()
print(lista)
element_del=int(input("¿Que número quieres eliminar?: "))
for e in lista:
    if e==element_del:
        lista.remove(element_del)
print(lista)
