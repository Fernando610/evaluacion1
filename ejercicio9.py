def ejercicio9():
    print "Dime cuantas horas trabajas"
    a=input("A= ")
    if (a<=40):
        print a*30,"euros"
    if (a>40):
        print (a*30),"euros por las horas no extra"
        print (a-40)*45,"euros por las horas extra"
ejercicio9()
