#Pyratilla hizo un formulario para que los interesados en formar parte de su tripulación rellenaran y así poder evitarse más de una entrevista innecesaria.

#Ahora es momento de filtrar las convocatorias:

#El nombre debe empezar por mayúscula. Si es un nombre compuesto, entonces todos deben empezar por mayúscula.
#La edad debe ser mayor o igual a 16 y menor o igual a 40.
#El hobby indicado debe tener más de 10 caracteres.
#La casilla del sueño no puede haber sido dejada en blanco.
#Ayuda a Pyratilla a crear este filtro para descartar solicitudes que no cumplan estos requisitos.

print("Rellene el siguiente formulario con su información personal")

interview=False
ConditionName=False
ConditionAge=False
ConditionHobby=False
ConditionDream=False

name=input("Ingrese su nombre:\n")
age=int(input("Ingrese su edad:\n"))
hobby=input("Ingrese su hobby y detallelo:\n")
dream=input("Ingrese su sueño o meta:\n")

if name.find(" ")==-1:
    if  name[0].isupper:
        ConditionName=True
else:
    if name.istittle():
        ConditionName=True

if (age>=16 and age<=40):
    ConditionAge=True

if len(hobby)>10:
    ConditionHobby=True

if dream!="":
    ConditionDream=True

if ConditionName and ConditionAge and ConditionHobby and ConditionDream:
    interview=True
    print("Se le concederà una entrevista.")
else:
    print("No cumple con los requisitos.")