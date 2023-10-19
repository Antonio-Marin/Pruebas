import json
import tkinter

with open("data_test.json") as file:
    data = json.load(file)


class program:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry("400x300")
        program.main(self)
        self.window.mainloop()
    
    def main(self):
        self.labeli = tkinter.Label(self.window, text="Bienvenido al menu.")
        self.labeli.pack()
        self.buttoni1 = tkinter.Button(self.window, text="Ver grupos", command=lambda:program.main_pack_forget(self, 0))
        self.buttoni1.pack()
        self.buttoni2 = tkinter.Button(self.window, text="¿Qué personaje subo?", command=program.nextrankreward)
        self.buttoni2.pack()
        self.buttoni3 = tkinter.Button(self.window, text="Salir", command=quit)
        self.buttoni3.pack()

    def main_pack_forget(self, aux):
        self.labeli.pack_forget()
        self.buttoni1.pack_forget()
        self.buttoni2.pack_forget()
        self.buttoni3.pack_forget()
        if aux == 0:
            program.group(self)
        elif aux == 1:
            program.nextrankreward()
        
    def group(self):
        self.labelg = tkinter.Label(self.window, text="Elija una opción.")
        self.labelg.pack()
        self.buttong1 = tkinter.Button(self.window, text=data["groups"][0]["nameg"], command= lambda:program.group_pack_forget(self, 1))
        self.buttong1.pack()
        self.buttong2 = tkinter.Button(self.window, text=data["groups"][1]["nameg"], command= lambda:program.group_pack_forget(self, 2))
        self.buttong2.pack()
        self.buttong3 = tkinter.Button(self.window, text=data["groups"][2]["nameg"], command= lambda:program.group_pack_forget(self, 3))
        self.buttong3.pack()
        self.buttong4 = tkinter.Button(self.window, text=data["groups"][3]["nameg"], command= lambda:program.group_pack_forget(self, 4))
        self.buttong4.pack()
        self.buttong5 = tkinter.Button(self.window, text=data["groups"][4]["nameg"], command= lambda:program.group_pack_forget(self, 5))
        self.buttong5.pack()
        self.buttong6 = tkinter.Button(self.window, text=data["groups"][5]["nameg"], command= lambda:program.group_pack_forget(self, 6))
        self.buttong6.pack()
        self.buttong7 = tkinter.Button(self.window, text="Atrás", command= lambda: program.group_pack_forget(self, 0))
        self.buttong7.pack()
        self.buttong8 = tkinter.Button(self.window, text="Salir", command= quit)
        self.buttong8.pack()

    def group_pack_forget(self, aux):
        self.labelg.pack_forget()
        self.buttong1.pack_forget()
        self.buttong2.pack_forget()
        self.buttong3.pack_forget()
        self.buttong4.pack_forget()
        self.buttong5.pack_forget()
        self.buttong6.pack_forget()
        self.buttong7.pack_forget()
        self.buttong8.pack_forget()
        if aux == 0:
            program.main(self)
        elif aux == 1:
            program.character(self, data["groups"][0]["idg"])
        elif aux == 2:
            program.character(self, data["groups"][1]["idg"])
        elif aux == 3:
            program.character(self, data["groups"][2]["idg"])
        elif aux == 4:
            program.character(self, data["groups"][3]["idg"])
        elif aux == 5:
            program.character(self, data["groups"][4]["idg"])
        elif aux == 6:
            program.character(self, data["groups"][5]["idg"])

    def character(self, vgroup):
        self.labelc = tkinter.Label(self.window, text="Elija un persnaje.")
        self.labelc.pack()
        if vgroup == 0:
            self.buttonc1 = tkinter.Button(self.window, text=data["groups"][vgroup]["integrants"][0]["namei"], command= lambda:program.character_pack_forget(self, 1, vgroup))
            self.buttonc1.pack()
            self.buttonc2 = tkinter.Button(self.window, text=data["groups"][vgroup]["integrants"][1]["namei"], command= lambda:program.character_pack_forget(self, 2, vgroup))
            self.buttonc2.pack()
            self.buttonc3 = tkinter.Button(self.window, text=data["groups"][vgroup]["integrants"][2]["namei"], command= lambda:program.character_pack_forget(self, 3, vgroup))
            self.buttonc3.pack()
            self.buttonc4 = tkinter.Button(self.window, text=data["groups"][vgroup]["integrants"][3]["namei"], command= lambda:program.character_pack_forget(self, 4, vgroup))
            self.buttonc4.pack()
            self.buttonc5 = tkinter.Button(self.window, text=data["groups"][vgroup]["integrants"][4]["namei"], command= lambda:program.character_pack_forget(self, 5, vgroup))
            self.buttonc5.pack()
            self.buttonc6 = tkinter.Button(self.window, text=data["groups"][vgroup]["integrants"][5]["namei"], command= lambda:program.character_pack_forget(self, 6, vgroup))
            self.buttonc6.pack()
        else:
            self.buttonc1 = tkinter.Button(self.window, text=data["groups"][vgroup]["integrants"][0]["namei"], command= lambda:program.character_pack_forget(self, 1, vgroup))
            self.buttonc1.pack()
            self.buttonc2 = tkinter.Button(self.window, text=data["groups"][vgroup]["integrants"][1]["namei"], command= lambda:program.character_pack_forget(self, 2, vgroup))
            self.buttonc2.pack()
            self.buttonc3 = tkinter.Button(self.window, text=data["groups"][vgroup]["integrants"][2]["namei"], command= lambda:program.character_pack_forget(self, 3, vgroup))
            self.buttonc3.pack()
            self.buttonc4 = tkinter.Button(self.window, text=data["groups"][vgroup]["integrants"][3]["namei"], command= lambda:program.character_pack_forget(self, 4, vgroup))
            self.buttonc4.pack()

        self.buttonc7 = tkinter.Button(self.window, text="Atrás", command= lambda: program.character_pack_forget(self, 0))
        self.buttonc7.pack()
        self.buttonc8 = tkinter.Button(self.window, text="Salir", command= quit)
        self.buttonc8.pack()

    def character_pack_forget(self, aux, vgroup):
        self.labelc.pack_forget()
        self.buttonc1.pack_forget()
        self.buttonc2.pack_forget()
        self.buttonc3.pack_forget()
        self.buttonc4.pack_forget()
        self.buttonc7.pack_forget()
        self.buttonc8.pack_forget()

        if vgroup == 0:
            self.buttonc5.pack_forget()
            self.buttonc6.pack_forget()

        if aux == 0:
            program.group(self)
        elif aux == 1:
            program.totalexp(self, vgroup, data["groups"][vgroup]["integrants"][0]["idi"])
        elif aux == 2:
            program.totalexp(self, vgroup, data["groups"][vgroup]["integrants"][1]["idi"])
        elif aux == 3:
            program.totalexp(self, vgroup, data["groups"][vgroup]["integrants"][2]["idi"])
        elif aux == 4:
            program.totalexp(self, vgroup, data["groups"][vgroup]["integrants"][3]["idi"])
        elif aux == 5:
            program.totalexp(self, vgroup, data["groups"][vgroup]["integrants"][4]["idi"])
        elif aux == 6:
            program.totalexp(self, vgroup, data["groups"][vgroup]["integrants"][5]["idi"])


    def totalexp(self, vgroup,vintegrant):

        print("\n \t",data["groups"][vgroup]["integrants"][vintegrant]["namei"],"\n")
        print("\t \t","Rango:",data["groups"][vgroup]["integrants"][vintegrant]["rank"])
        print("\t \t", "Experiencia:",data["groups"][vgroup]["integrants"][vintegrant]["exp"],"/", data["groups"][vgroup]["integrants"][vintegrant]["maxexp"])
        print("\n\tElige una opción:")
        print("\n\t1. Añadir Experiencia")
        print("\t2. Atrás")
        print("\t3. Salir\n")

        var = input("Indica el número de la opción deseada:")

        if var == "1":
            program.addexp(vgroup,vintegrant)
        elif var == "2":
            program.character(vgroup)
        elif var == "3":
            pass
        else:
            print("\nPOR FAVOR INTRODUZCA UN NÚMERO DE LOS QUE SE MUESTRAN")
            program.totalexp(vgroup, vintegrant)

    def addexp(vgroup,vintegrant):
        new_exp = input("\tExperiencia a añadir:")
        program.keepadding(vgroup,vintegrant, int(new_exp))

    def keepadding(vgroup,vintegrant, new_exp):

        maxexp = data["groups"][vgroup]["integrants"][vintegrant]["maxexp"]

        if(new_exp==0):
            program.totalexp(vgroup,vintegrant)
        elif(new_exp<maxexp):
            data["groups"][vgroup]["integrants"][vintegrant]["exp"] += int(new_exp)
        elif(new_exp==maxexp):
            data["groups"][vgroup]["integrants"][vintegrant]["exp"] = 0
            data["groups"][vgroup]["integrants"][vintegrant]["rank"] +=1
            program.calculaterank(vgroup,vintegrant, data["groups"][vgroup]["integrants"][vintegrant]["rank"])
        else:
            data["groups"][vgroup]["integrants"][vintegrant]["rank"] +=1
            aux = int(new_exp) - maxexp
            if(aux<maxexp):
                data["groups"][vgroup]["integrants"][vintegrant]["exp"] += aux
            else:
                program.keepadding(vgroup,vintegrant, aux)
        
        with open("data_test.json", mode='w') as f:
                json.dump(data, f)
        program.totalexp(vgroup,vintegrant)

    def calculaterank(vgroup,vintegrant, newrank):
        rexp = {1:1,2:1,3:2,4:3,5:3,6:4,7:4,8:4,9:4,10:4,11:5,12:5,13:5,14:5,15:5,16:6,17:6,18:6,19:6,20:6,
                21:7,22:7,23:7,24:7,25:7,26:8,27:8,28:8,29:8,30:8,31:9,32:9,33:9,34:9,35:9}
        if(newrank>=36 and newrank<110):
            data["groups"][vgroup]["integrants"][vintegrant]["maxexp"] = 10
        else:
            data["groups"][vgroup]["integrants"][vintegrant]["maxexp"] = rexp[newrank]
        with open("data_test.json", mode='w') as f:
            json.dump(data, f)
        program.totalexp(vgroup,vintegrant)

    def nextrankreward():
        wr = [1,2,6,8,13,16,18,22,23,28,33,38,43,48,53,58,63,68,73,78,83,88,93,98,103,108]
        cry3 = list()
        bo=list()
        cry1 = list()
        co = list()
        for group in data["groups"]:
            for integrant in group["integrants"]:
                nextrank = integrant["rank"]+1
                if nextrank not in wr:
                    if nextrank%5 == 0:
                        if (integrant["maxexp"]-integrant["exp"]) == 1:
                            bo.append(integrant["namei"])
                        else:
                            cry3.append(integrant["namei"])
                    else:
                        if (integrant["maxexp"]-integrant["exp"]) == 1:
                            co.append(integrant["namei"])
                        else:
                            cry1.append(integrant["namei"])

        print("\nA punto de subir (300 cristales):", bo,"\n")
        print("A punto de subir (100 cristales) ",co,"\n")
        print("Personajes que te van a dar 300 cristales: ",cry3,"\n")
        print("Personajes que te van a dar 100 cristales: ",cry1,"\n")

if __name__ == '__main__':
    program()