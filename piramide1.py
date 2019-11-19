def piramide1():
    filas=input("Dime la altura en pisos")
    espacios=' '
    asteriscos='*'
    for i in range(filas):
        for nespacios in range(1,filas-i):
            espacios=espacios+' '
        for nasteriscos in range(1,2*i+1):
            asteriscos=asteriscos+'*'
        print espacios+asteriscos
        espacios=' '
        asteriscos='*'
piramide1()
