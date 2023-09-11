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
    r=list()
    print("\n")
    for i in data["groups"]:
        number = i["idg"]
        r.append(number+1)
        print("\t",number+1,".",i["nameg"])
    print("\t",number+2,". Atrás")
    print("\t",number+3,". Salir\n")
    number+=3
    var = input("Indica el número de la opción deseada:")

    if var in str(r):
        character(int(var)-1)
    elif var == str(number-1):
        main()
    elif var == str(number):
        pass
    else:
        print("\nPOR FAVOR INTRODUZCA UN NÚMERO DE LOS QUE SE MUESTRAN")
        group()

def character(vgroup):
    print("\n")
    idis = list()
    for i in data["groups"][vgroup]["integrants"]:
        idis.append(i["idi"]+1)
        print("\t",i["idi"]+1,".",i["namei"])
    number = len(data["groups"][vgroup]["integrants"]) +1
    print("\t",number,". Atrás")
    print("\t",number+1,". salir","\n")

    var = input("Indica el número de la opción deseada:")

    if var in str(idis):
        totalstar(vgroup,int(var)-1)
    elif var == str(number):
        group()
    elif var == str(number+1):
        pass
    else:
        print("\nPOR FAVOR INTRODUZCA UN NÚMERO DE LOS QUE SE MUESTRAN")
        character(vgroup)

def totalstar(vgroup,vintegrant):
    print(data["groups"][vgroup]["integrants"][vintegrant])
    #TODO: Implementar una "interfaz" mejor que muestre los datos necesarios
    pass

#TODO: Implementar funcion(es) para implementar añadir estrellas directamente, quitar o modificar los datos (esta última podría pedirtela al ejecutar el código por 1ª vez)

if __name__ == '__main__':
    main()