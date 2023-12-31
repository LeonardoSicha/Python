#Ejercicio 1
s1 = "Había una vez, "
s2 = "un barquito chiquitito "
s3 = "que no podía, "
s4 = "que no podía navegar."
print(((s1+s2)*2)+(s3*2)+s4)

#Ejercicio 2
print("Érase un hombre a una nariz pegado,\nÉrase una nariz superlativa,\nÉrase una alquitara medio viva,\nÉrase un peje espada mal barbado;")

#Ejercicio 3
s = "me encantan las matemáticas"
print(s.upper())

#Ejercicio 4
s = "Mi pasión por el chocolate es superior a mis fuerzas"
print(len(s))

#Ejercicio 5
s = "Mi pasión por el chocolate es superior a mis fuerzas"
s_sub=s[s.find("chocolate"):s.find("chocolate")+len("chocolate")]
print(s_sub)

#Ejercicio 6
nombre=input("Introduce tu nombre: ")

#Ejercicio 7
apellido=input("Introduce tu apellido: ")

#Ejercicio 8
edad=int(input("Introduce tu edad: "))

#Ejercicio 9
ciudad=input("Introduce tu ciudad: ")

#Ejercicio 10
print("Su nombre es {} {}, tiene {} años y actualmente vive en {}.".format(nombre,apellido,edad,ciudad))