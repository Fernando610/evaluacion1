def n_primo_multiplo11():
    print "dime un numero"
    a=input("A =")
    for i in range(2,a):
        if(a%i==0):
            print "no es primo"
        else:
            print "es primo"
        break
    if (a%11==0):
        print "es multiplo de 11"
    else:
        print "no es multiplo de 11"
    
n_primo_multiplo11()
        
    
