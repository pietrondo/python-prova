
def somma(a, b):
    return(a+b)

def moltiplicazione(a, b):
    return(a*b)

def main():
    a=1
    a=int(input("Quale funzione? somma = 1, moltiplicazione = 2"))
    while a !=0:
            if a == 1:
                    print("Dimmi cosa sommare?\n")
                    b = int(input("primo valore\n"))
                    c = int(input("secondo valore\n"))
                    print( int(somma(b, c)) )
            elif a == 2:
                    print("Dimmi cosa moltiplicare?\n")
                    b = int(input("primo valore\n"))
                    c = int(input("secondo valore\n"))
                    print( int(moltiplicare(b, c)) )


        
main()
