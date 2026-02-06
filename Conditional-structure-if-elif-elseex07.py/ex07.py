#ex07:
age=int(input("Entre votre age svp, age = "))
if age > 0:
    if age < 12 :
        print("Grtuit")
    elif age >= 12 and age < 17:
        print("Paye 5€")
    elif age > 18 :
        print (" Paye 10€")
else  :
   print("error")
