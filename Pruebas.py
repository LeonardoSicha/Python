title = "se busca tripulante"
message1 = "se ofrece puesto en la tripulación del capitán pyratilla para llevar a cabo labores de marinero." 
message2 = "comida y bebida garantizada a lo largo de toda la aventura."
contact = "para más información, ir al puerto y buscar al capitán pyratilla, ya famoso en este pueblo costero (evitar preguntar en el casino)."

title_final=title.upper()

message1=message1.capitalize()
message1=message1.replace("pyratilla","Pyratilla")

message2=message2.capitalize()
message2=message2.replace("pyratilla","Pyratilla")

contact=contact.capitalize()
contact=contact.replace("pyratilla","Pyratilla")

print(title_final+"\n"+message1+"\n"+message2+"\n"+contact)

name=input("Introduzca su nombre: ")
age=int(input("Introduzca su edad: "))
hobby=input("¿Cuál es su hobby?: ")
dream=input("¿Cuál es su sueño?: ")
print("gols")