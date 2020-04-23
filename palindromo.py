n = input('Cadena: ')
arg = list(n)
lon = len(arg)
l=lon
conteo=0
centro=0
for i in range(lon):
    l=lon
    for j in range(lon):
        try: 
            if arg[i]==arg[l]:
                conteo+=1
            elif arg[i-1]==arg[i+1] and conteo!=0:
                centro=i
            else:
                conteo=0
        except:
            asd=0
        l-=1
if centro!=0:
    largo = centro + conteo
    larg = centro - conteo
    longitud = conteo * 2 + 1
    print(arg[larg:largo+1])
    print("longitud: ", longitud)
If conteo==0:
    print(arg[0])
