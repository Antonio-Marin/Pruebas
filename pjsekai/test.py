import json

with open("data.json") as file:
    data = json.load(file)

#print(data["groups"][0]["integrants"])


def main():
    print("\nBienvenido al menu.")
    print("\n\tElige una opción:")
    print("\n\t1. Ver grupos")
    print("\t2. Salir\n")

    var = input("Indica el número de la opción deseada:")

    if var == "1":
        group()
    elif var == "2":
        pass
    else:
        print("\nPOR FAVOR INTRODUZCA UN NÚMERO DE LOS QUE SE MUESTRAN")
        main()
    
def group():
    number = 0
    print("\n")
    for i in data["groups"]:
        number+=1
        print("\t",number,".",i["nameg"])
    number+=1
    print("\t",number,". Atrás")
    number+=1
    print("\t",number,". Salir\n")

def character(vgroup):
    pass  

if __name__ == '__main__':
    main()