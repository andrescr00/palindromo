def impar(arg):
    lon = len(arg)
    longitud = 0
    valores = []
    resImpar = []
    for i in range(1,lon-1):
        valores = []
        if arg[i-1]==arg[i+1]:
            longitud+=1
            centro = arg[i]
            valores.insert(0,arg[i+1])
            for a in range(2,lon//2):
                try:
                    if arg[i-a]==arg[i+a]:
                        longitud+=1
                        valores.insert(0,arg[i-a])
                    else:
                        break
                except: asd=0
            l = len(valores)
            for m in reversed(valores):
                valores.append(m)
            valores.insert(l,centro)
            cadena = "".join(str(v) for v in valores)
            resImpar.append(cadena)
    return (resImpar)
def par(arg):
    lon = len(arg)
    longitud = 0
    valores1 = []
    resPar = []
    for i in range(1,lon-1):
        valores1 = []
        if arg[i]==arg[i+1]:
            valores1.insert(0,arg[i])
            ad = 2
            at = 1
            for b in range(lon//2):
                try:
                    if arg[i+ad]==arg[i-at]:
                        valores1.insert(0,arg[i+ad])
                        ad+=1
                        at+=1
                    else:
                        break
                except:
                    asd=0
            for m in reversed(valores1):
                valores1.append(m)
            cad = "".join(str(v) for v in valores1)
            resPar.append(cad)
    return (resPar)
def palindromo(n):
    n = str(n)
    arg = list(n)
    lon = len(arg)
    longitud = 0
    if lon == 0:
        return ('')
    if arg == arg[::-1]:
        cad = "".join(str(v) for v in arg)
        return (cad)
    centro = None
    if impar(arg):
        return max(impar(arg))
    elif par(arg):
        return max(par(arg))
    else:
        return arg[0]