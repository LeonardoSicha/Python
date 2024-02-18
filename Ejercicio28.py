reversed=input("Si quiere orden descendete, escribe True. De lo contrario, dale escribe False: ")
if reversed=="True":
    reversed=True
elif reversed=="False":
    reversed=False
l=[]

for _ in range(10):
    l.append(float(input()))

l.sort(reverse=reversed)
print(l)