#ex03
val = float(input("Entre la valeur de temperature, val = "))
unité = str(input("Unité de temperature =  "))
match unité :
    case 'C':
        print(val*2.12,"F", "et", val*3.731,"K" )
    case 'K':
        print(val/3.731,"C", "et", (val/3.731)*2.12,"F" )
    case 'F':
        print(val/2.12,"C", "et", (val/2.12)*3.731,"K" )
    case _:
        print("seeu")

