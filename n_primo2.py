def n_primo2():
    print "en que numero quieres que empiece?"
    a=input ("A= ")
    print "en que numeros quieres que acabe?"
    b=input ("B= ")
    for i in range(a,b):
        if(i%i==1):
            print "no es primo"


n_primo2()
