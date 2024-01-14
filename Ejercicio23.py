s=input("Ingrese una oración: ")
letter=input("Ingrese la letra a omitir: ")
num_letter=int(input("Ingrese el número máximo de la letra a omitir: "))
count=0
letter=letter.lower()
s=s.lower()

for i in s:
    if count>=num_letter:
        print("\nSe han superado el número de apariciones.")
        break
    if i==letter:
        count+=1
    elif i in ["a","e","i","o","u"]:
        continue

    print(i, end="")