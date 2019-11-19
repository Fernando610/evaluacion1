def ejercicio5():
    repetir1=True
    repetir2=True
    print "dime un dia"
    while(repetir1==True):
        a=input("A= ")
        repetir1=a<1 or a>31
        if (repetir1==True):
            print("ERROR. Este dia no existe")
    print "dime un mes"
    while(repetir2==True):
        b=input("B= ")
        repetir2=b<1 or b>12
        if(repetir2==True):
            print("ERROR. Este mes no exite")
        if (b==1):
            b="Enero" 
        if (b==2):
            b="Febrero"
        if (b==3):
            b="Marzo"
        if (b==4):
            b="Abril"
        if (b==5):
            b="Mayo"
        if (b==6):
            b="Junio"
        if (b==7):
            b="Julio"
        if (b==8):
            b="Agosto"
        if (b==9):
            b="Septiembre"
        if (b==10):
            b="Octubre"
        if (b==11):
            b="Noviembre"
        if (b==12):
            b="Diciembre"
    print "dime un año"
    c=input("C= ")
    print a,"de",b,"de",c
                  
ejercicio5()
