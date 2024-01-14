s=input("Ingrese una oración: ")
print(f"La oración es: {s}")
letter=input("Ingrese la letra a omitir: ")

s=s.lower()
letter=letter.lower()

for i in s:
    if i==letter:
        continue
    print(i, end="")    