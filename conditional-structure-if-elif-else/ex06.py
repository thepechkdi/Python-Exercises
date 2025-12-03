#ex06
nb1=float(input("saisir la valeur de nombre 1, nb1 = "))
oper = str (input ("'+','-', '*','/': "))
nb2=float(input("saisir la valeur de nombre 2, nb2 = "))
if oper == '+':
    print("nb1+nb2=",nb1+nb2)
elif oper == '-' :
    print("nb1-nb2=",nb1-nb2)
elif oper == '*':
    print("nb1*nb2=",nb1*nb2)
elif oper == '/':
    if nb2 != 0 :
        print("nb1/nb2",nb1/nb2)
    else :
        print("Entre un nomber differnt 0")
else :
    print(" svp entre un nomber")
    
 
