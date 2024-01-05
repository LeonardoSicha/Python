year=int(input("Año: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("El año {} es bisiesto.".format(year))
        else:
            print("El año {} no es bisiesto.".format(year))    
    else:
        print("El año {} es bisiesto.".format(year))    
else:
    print("El año {} no es bisiesto.".format(year))