#Reclutando tripulantes
#Pyratilla considera que ya va siendo hora de encontrar a su primer miembro de la tripulación. Para ello, lo primero que decide hacer es un anuncio.

title = "se busca tripulante"
message1 = "se ofrece puesto en la tripulación del capitán pyratilla para llevar a cabo labores de marinero."
message2 = "comida y bebida garantizada a lo largo de toda la aventura."
contact = "para más información, ir al puerto y buscar al capitán pyratilla, ya famoso en este pueblo costero (evitar preguntar en el casino)."

#Ayuda a Pyratilla a que el anuncio le quede bien:

#El título debe estar todo en mayúsculas
#El principio de cada frase debe estar en mayúscula
#Cada vez que hay un cambio de variable, debe haber un salto de línea
#El nombre de Pyratilla debe estar en mayúscula
#Pista: puede que te sea más fácil si guardas las dos frases de la variable message en dos variables diferentes y una vez las tengas listas, las vuelves a unir.

title_final=title.upper()
 
message1=message1.capitalize()
message1=message1.replace("pyratilla","Pyratilla")
 
message2=message2.capitalize()
message2=message2.replace("pyratilla","Pyratilla")
 
contact=contact.capitalize()
contact=contact.replace("pyratilla","Pyratilla")
 
print(title_final+"\n"+message1+"\n"+message2+"\n"+contact)

#Ayuda a Pyratilla a crear un formulario donde se pida amablemente el nombre, la edad, el hobby y el sueño al interesado en formar parte de la tripulación del capitán Pyratilla.

name=input("Introduzca su nombre: ")
age=int(input("Introduzca su edad: "))
hobby=input("¿Cuál es su hobby?: ")
dream=input("¿Cuál es su sueño?: ")