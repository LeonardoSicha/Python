age=int(input("Introduzca su edad: "))
name=input("Introduzaca su nombre: ")

if age >= 18:
  if name.startswith("M") or name.startswith("m"):
    print("Eres mayor de edad pues tienes {} años y tu nombre, que es {}, empieza por M.".format(age, name))
  else:
    print("Eres mayor de edad pues tienes {} años.".format(age))
else:
  print("Eres muy joven.")