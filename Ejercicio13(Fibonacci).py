fibo_ant = 1
fibo = 1 
idx = 3 

print("El término {} ocupa la posición {}".format(fibo_ant, 1))
print("El término {} ocupa la posición {}".format(fibo, 2))

while idx<=20:
  temp = fibo 
  fibo = fibo + fibo_ant
  fibo_ant = temp

  print("El término {} ocupa la posición {}".format(fibo, idx))

  idx += 1 # Incrementamos el valor del índice