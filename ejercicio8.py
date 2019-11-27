def ejercicio8():
    print ("dime un precio")
    a=input("A= ")
    print ("Dime el tipo de IVA:general(G),reducido(R),superreducido(S)")
    b=raw_input("letra= ")
    if (b=="G"):
        print a*1.16
    if (b=="R"):
        print a*1.07
    if (b=="S"):
        print a*1,04
ejercicio8()
    
