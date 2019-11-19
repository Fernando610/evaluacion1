def Ejercicio_7():
    print"Dime 2 numeros enteros"
    a=input("A= ")
    b=input("B= ")
    print "Elige:sumar(S),restar(R),multiplicacion(M) o division(D)"
    operacion=raw_input("letra= ")
    if (operacion=="S"):
        print ("Suma= "),a+b
    if (operacion=="R"):
        print ("Resta= "),a-b
    if (operacion=="M"):
        print ("Multiplicar= "),a*b
    if(operacion=="D"):
        if (b==0):
            print("Error, no se puede dividir entre 0")
        else:
            print("División= "),a/b
Ejercicio_7()
    
