print("Introduce una palabra y yo te la devuelvo en mayúsculas: ")
word=input()
print(word.upper())

print("Introduce una frase y yo te devuelvo todas las palabras empezando en mayúscula: ")
s = input()
print(s.title())

print("Introduce una palabra con 3 letras o más y yo te devuelvo todas sus letras en minúscula salvo la tercera: ")
word2 = input()
word2 = word[:2].lower() + word[2].upper() + word[3:].lower()
print(word)

print("Introduce una palabra y yo te devuelvo todas sus letras en mayúscula salvo la primera y la última")
word = input()
word = word[0].lower() + word[1:(len(word) - 1)].upper() + word[-1].lower()
print(word)

subs = "su"
print("Introduce una frase y yo te la devuelvo sustituyendo las dos primeras letras de la primera palabra por las letras {}".format(subs))
s = input()
print(s.replace(s[:2], subs))