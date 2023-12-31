import json
import tkinter

with open("data.json") as file:
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
        self.buttoni2 = tkinter.Button(self.window, text="¿Qué personaje subo?", command=lambda:program.main_pack_forget(self, 1))
        self.buttoni2.pack()
        self.buttoni3 = tkinter.Button(self.window, text="Salir", command=self.window.destroy)
        self.buttoni3.pack()

    def main_pack_forget(self, aux):
        self.labeli.pack_forget()
        self.buttoni1.pack_forget()
        self.buttoni2.pack_forget()
        self.buttoni3.pack_forget()
        if aux == 0:
            program.group(self)
        elif aux == 1:
            program.nextrankreward(self)
        
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
        self.buttong8 = tkinter.Button(self.window, text="Salir", command= self.window.destroy)
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
        self.labelc = tkinter.Label(self.window, text="Elija un personaje.")
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

        self.buttonc7 = tkinter.Button(self.window, text="Atrás", command= lambda: program.character_pack_forget(self, 0, vgroup))
        self.buttonc7.pack()
        self.buttonc8 = tkinter.Button(self.window, text="Salir", command= self.window.destroy)
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


    def totalexp(self,vgroup,vintegrant):

        self.labelte1 = tkinter.Label(self.window, text=data["groups"][vgroup]["integrants"][vintegrant]["namei"])
        self.labelte1.pack()
        texto_aux1 = "Rango:",data["groups"][vgroup]["integrants"][vintegrant]["rank"]
        self.labelte2 = tkinter.Label(self.window, text= texto_aux1 )
        self.labelte2.pack()
        texto_aux2 = "Experiencia:",data["groups"][vgroup]["integrants"][vintegrant]["exp"],"/", data["groups"][vgroup]["integrants"][vintegrant]["maxexp"]
        self.labelte3 = tkinter.Label(self.window, text= texto_aux2 )
        self.labelte3.pack()
        self.labelte4 = tkinter.Label(self.window, text= "Elige una opción:" )
        self.labelte4.pack()
        self.new_exp = tkinter.Entry()
        self.new_exp.insert(0,"0")
        self.new_exp.pack()
        self.buttonte1 = tkinter.Button(self.window, text="Añadir experiencia", command= lambda:program.keepadding(self,vgroup, vintegrant, int(self.new_exp.get())))
        self.buttonte1.pack()
        self.buttonte2 = tkinter.Button(self.window, text="Atrás", command= lambda: program.totalexp_pack_forget(self, 0, vgroup, vintegrant))
        self.buttonte2.pack()
        self.buttonte3 = tkinter.Button(self.window, text="Salir", command= self.window.destroy)
        self.buttonte3.pack()
            

    def totalexp_pack_forget(self, aux, vgroup, vintegrant):
        self.labelte1.pack_forget()
        self.labelte2.pack_forget()
        self.labelte3.pack_forget()
        self.labelte4.pack_forget()
        self.new_exp.pack_forget()
        self.buttonte1.pack_forget()
        self.buttonte2.pack_forget()
        self.buttonte3.pack_forget()
        if aux == 0:
            program.character(self, vgroup)
        else:
            program.totalexp(self, vgroup, vintegrant)
    

    def keepadding(self,vgroup,vintegrant, new_exp): #TODO: error en la rellamada
        maxexp = data["groups"][vgroup]["integrants"][vintegrant]["maxexp"]
        new_exp += data["groups"][vgroup]["integrants"][vintegrant]["exp"]
        if new_exp==0:
            program.totalexp_pack_forget(self,1,vgroup,vintegrant)
        elif new_exp<maxexp:
            data["groups"][vgroup]["integrants"][vintegrant]["exp"] = new_exp
        elif new_exp==maxexp:
            data["groups"][vgroup]["integrants"][vintegrant]["exp"] = 0
            data["groups"][vgroup]["integrants"][vintegrant]["rank"] +=1
            with open("data.json", mode='w') as f:
                    json.dump(data, f)
            program.calculaterank(self,vgroup,vintegrant, data["groups"][vgroup]["integrants"][vintegrant]["rank"])
        elif new_exp>maxexp:
            aux = new_exp-maxexp
            data["groups"][vgroup]["integrants"][vintegrant]["exp"] = 0
            data["groups"][vgroup]["integrants"][vintegrant]["rank"] +=1
            data["groups"][vgroup]["integrants"][vintegrant]["maxexp"] = program.new_maxexp(data["groups"][vgroup]["integrants"][vintegrant]["rank"])
            with open("data.json", mode='w') as f:
                    json.dump(data, f)
            program.keepadding(self,vgroup,vintegrant, aux)
        
        with open("data.json", mode='w') as f:
                json.dump(data, f)
        program.totalexp_pack_forget(self,1,vgroup,vintegrant)

    def calculaterank(self,vgroup,vintegrant, newrank):
        rexp = {1:1,2:1,3:2,4:3,5:3,6:4,7:4,8:4,9:4,10:4,11:5,12:5,13:5,14:5,15:5,16:6,17:6,18:6,19:6,20:6,
                21:7,22:7,23:7,24:7,25:7,26:8,27:8,28:8,29:8,30:8,31:9,32:9,33:9,34:9,35:9}
        if(newrank>=36 and newrank<110):
            data["groups"][vgroup]["integrants"][vintegrant]["maxexp"] = 10
        else:
            data["groups"][vgroup]["integrants"][vintegrant]["maxexp"] = rexp[newrank]

        with open("data.json", mode='w') as f:
            json.dump(data, f)
        program.totalexp_pack_forget(self,1,vgroup,vintegrant)

    def new_maxexp(rank):
        rexp = {1:1,2:1,3:2,4:3,5:3,6:4,7:4,8:4,9:4,10:4,11:5,12:5,13:5,14:5,15:5,16:6,17:6,18:6,19:6,20:6,
                21:7,22:7,23:7,24:7,25:7,26:8,27:8,28:8,29:8,30:8,31:9,32:9,33:9,34:9,35:9}
        if rank<36:
            return rexp[rank]
        else:
            return 10

    def nextrankreward(self):
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

        text1 = "A punto de subir (300 cristales):",bo
        self.labelnr1 = tkinter.Label(self.window, text="A punto de subir (300 cristales):")
        self.labelnr1.pack()
        self.labelnr2 = tkinter.Label(self.window, text=str(bo))
        self.labelnr2.pack()
        text2 = "A punto de subir (100 cristales) ",co
        self.labelnr3 = tkinter.Label(self.window, text="A punto de subir (100 cristales) ")
        self.labelnr3.pack()
        self.labelnr4 = tkinter.Label(self.window, text=str(co))
        self.labelnr4.pack()
        text3 = "Personajes que te van a dar 300 cristales: ",cry3
        self.labelnr5 = tkinter.Label(self.window, text="Personajes que te van a dar 300 cristales: ")
        self.labelnr5.pack()
        self.labelnr6 = tkinter.Label(self.window, text=str(cry3))
        self.labelnr6.pack()
        text4 = "Personajes que te van a dar 100 cristales: ",cry1
        self.labelnr7 = tkinter.Label(self.window, text="Personajes que te van a dar 100 cristales: ")
        self.labelnr7.pack()
        self.labelnr8 = tkinter.Label(self.window, text=str(cry1))
        self.labelnr8.pack()
        self.buttonnr1 = tkinter.Button(self.window, text="Atrás", command= lambda:program.nextrankreward_pack_forget(self))
        self.buttonnr1.pack()
        self.buttonnr2 = tkinter.Button(self.window, text="Salir", command= self.window.destroy)
        self.buttonnr2.pack()
    
    def nextrankreward_pack_forget(self):
        self.labelnr1.pack_forget()
        self.labelnr2.pack_forget()
        self.labelnr3.pack_forget()
        self.labelnr4.pack_forget()
        self.labelnr5.pack_forget()
        self.labelnr6.pack_forget()
        self.labelnr7.pack_forget()
        self.labelnr8.pack_forget()
        self.buttonnr1.pack_forget()
        self.buttonnr2.pack_forget()
        program.main(self)

    def prueba():
        pass
        

if __name__ == '__main__':
    program()