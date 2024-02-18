#99 Bottles of Rum on the Wall

#De tantas solicitudes que ha recibido, Pyratilla no cabe en sí de la emoción y se pone a cantar

#"99 bottles of rum on the wall, 99 bottles of rum.
#Take one down, pass it around, 98 bottles of rum on the wall.
#98 bottles of rum on the wall, 98 bottles of rum.
#Take one down, pass it around, 97 bottles of rum on the wall..."

#Ayuda a Pyratilla a cantar la canción al completo con un bucle while.

start=int(input("Ingresa el número de botellas: "))
s="bottles of rum on the wall"
s2="bottles of rum."
s3="Take one down, pass it around,"
print(f"{start} {s}, {start} {s2}")

while start>=0:
    print(f"{s3} {start-1} {s}.\n{start-1} {s}, {start-1} {s2}")
    start-=1

#Ayuda a Pyratilla a cantar la canción al completo con un bucle for.
    
start=int(input("Ingresa el número de botellas: "))
s="bottles of rum on the wall"
s2="bottles of rum."
s3="Take one down, pass it around,"
print(f"{start} {s}, {start} {s2}")

for i in range(start-1,-1,-1):
    print(f"{s3} {i} {s}.\n{i} {s}, {i} {s2}")