#ex02
nb1=int(input("entre nb1 = "))
op=str(input())
nb2=int(input("entre nb2 = "))
match op:
    case '+':
        print("nb1+nb2=",nb1+nb2)
    case '-':
        print("nb1-nb2=",nb1-nb2)
    case '*':
        print("nb1*nb2=",nb1*nb2)
    case '/':
        if nb2 != 0:
            print("nb1/nb2=",nb1/nb2)
        else :
            print('La division impossible')
    case _:
        print("Entre  op corrct")