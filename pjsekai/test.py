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
        totalexp(vgroup,int(var)-1)
    elif var == str(number):
        group()
    elif var == str(number+1):
        pass
    else:
        print("\nPOR FAVOR INTRODUZCA UN NÚMERO DE LOS QUE SE MUESTRAN")
        character(vgroup)

def totalexp(vgroup,vintegrant):

    #TODO: Implementar una "interfaz" mejor que muestre los datos necesarios
    print("\n \t",data["groups"][vgroup]["integrants"][vintegrant]["namei"],"\n")
    print("\t \t","Rango:",data["groups"][vgroup]["integrants"][vintegrant]["rank"])
    print("\t \t", "Experiencia:",data["groups"][vgroup]["integrants"][vintegrant]["exp"],"/", data["groups"][vgroup]["integrants"][vintegrant]["maxexp"])
    print("\n\tElige una opción:")
    print("\n\t1. Añadir Experiencia")
    print("\t2. Modificar datos")
    print("\t3. Atrás")
    print("\t4. Salir\n")

    var = input("Indica el número de la opción deseada:")

    if var == "1":
        pass
    elif var == "2":
        pass
    elif var == "3":
        character(vgroup)
    elif var == "4":
        pass
    else:
        print("\nPOR FAVOR INTRODUZCA UN NÚMERO DE LOS QUE SE MUESTRAN")
        totalexp(vgroup, vintegrant)

#TODO: Implementar funcion(es) para implementar añadir Experiencia directamente, quitar o modificar los datos (esta última podría pedirtela al ejecutar el código por 1ª vez)

if __name__ == '__main__':
    main()