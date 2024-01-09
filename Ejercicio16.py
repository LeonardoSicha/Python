n = int(input("Introduce una rotación: "))
i = 65

while i <= 90:
  if i + n <= 90:
    print(chr(i) + ": " + chr(i + n))
  else:
    print(chr(i) + ": " + chr((i - 26) + n))
  i += 1