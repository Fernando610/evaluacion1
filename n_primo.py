def n_primo():
    print "dime un numero"
    a=input("A =")
    for i in range(2,a):
        if(a%i==0):
            print "no es primo"
        else:
            print "es primo"
        break
    
n_primo()
        
    
