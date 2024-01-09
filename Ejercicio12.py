s=input("Ingrese una frase: ")
s=s.lower
i=0
count=0
while i<len(s):
    if s[i] in ["a","e","i","o","u"]:
        count+=1
    i+=1

print("En total hay {} vocales.".format(count))