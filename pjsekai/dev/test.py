import json
import tkinter
import time

with open("data_test.json") as file:
    data = json.load(file)


class program:
    def __init__(self):
        self.add = False
        self.window = tkinter.Tk()
        ancho_pantalla = self.window.winfo_screenwidth()
        alto_pantalla = self.window.winfo_screenheight()
        self.window.geometry(f"{ancho_pantalla}x{alto_pantalla}")
        program.main(self)
        self.window.mainloop()
    
    def main(self):
        self.labeli = tkinter.Label(self.window, text="Bienvenido al menu.")
        self.labeli.pack()
        self.buttoni1 = tkinter.Button(self.window, text="Ver grupos", command=lambda:program.main_pack_forget(self, 0))
        self.buttoni1.pack()
        self.buttoni2 = tkinter.Button(self.window, text="¿Qué personaje subo?", command=lambda:program.main_pack_forget(self, 1))
        self.buttoni2.pack()
        self.buttoni3 = tkinter.Button(self.window, text="Añadir datos", command=lambda:program.main_pack_forget(self, 2))
        self.buttoni3.pack()
        self.buttoni4 = tkinter.Button(self.window, text="Salir", command=self.window.destroy)
        self.buttoni4.pack()

    def main_pack_forget(self, aux):
        self.labeli.pack_forget()
        self.buttoni1.pack_forget()
        self.buttoni2.pack_forget()
        self.buttoni3.pack_forget()
        self.buttoni4.pack_forget()
        if aux == 0:
            program.group(self)
        elif aux == 1:
            program.nextrankreward(self)
        elif aux == 2:
            self.add = True
            program.group(self)
        
    def group(self):

        self.labelg = tkinter.Label(self.window, text="Elija una opción.")
        self.labelg.pack()
        self.buttong1 = tkinter.Button(self.window, text=data["groups"][0]["nameg"], command= lambda:program.group_pack_forget(self, 0))
        self.buttong1.pack()
        self.buttong2 = tkinter.Button(self.window, text=data["groups"][1]["nameg"], command= lambda:program.group_pack_forget(self, 1))
        self.buttong2.pack()
        self.buttong3 = tkinter.Button(self.window, text=data["groups"][2]["nameg"], command= lambda:program.group_pack_forget(self, 2))
        self.buttong3.pack()
        self.buttong4 = tkinter.Button(self.window, text=data["groups"][3]["nameg"], command= lambda:program.group_pack_forget(self, 3))
        self.buttong4.pack()
        self.buttong5 = tkinter.Button(self.window, text=data["groups"][4]["nameg"], command= lambda:program.group_pack_forget(self, 4))
        self.buttong5.pack()
        self.buttong6 = tkinter.Button(self.window, text=data["groups"][5]["nameg"], command= lambda:program.group_pack_forget(self, 5))
        self.buttong6.pack()
        self.buttong7 = tkinter.Button(self.window, text="Atrás", command= lambda: program.group_pack_forget(self, 6))
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
        if aux == 6:
            self.add = False
            program.main(self)
        elif self.add is True:
            program.add_data(self,aux)
        elif aux == 0:
            program.character(self, data["groups"][0]["idg"])
        elif aux == 1:
            program.character(self, data["groups"][1]["idg"])
        elif aux == 2:
            program.character(self, data["groups"][2]["idg"])
        elif aux == 3:
            program.character(self, data["groups"][3]["idg"])
        elif aux == 4:
            program.character(self, data["groups"][4]["idg"])
        elif aux == 5:
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
    

    def keepadding(self,vgroup,vintegrant, new_exp):
        maxexp = data["groups"][vgroup]["integrants"][vintegrant]["maxexp"]
        new_exp += data["groups"][vgroup]["integrants"][vintegrant]["exp"]
        if new_exp==0:
            program.totalexp_pack_forget(self,1,vgroup,vintegrant)
        elif new_exp<maxexp:
            data["groups"][vgroup]["integrants"][vintegrant]["exp"] = new_exp
        elif new_exp==maxexp:
            data["groups"][vgroup]["integrants"][vintegrant]["exp"] = 0
            data["groups"][vgroup]["integrants"][vintegrant]["rank"] +=1
            with open("data_test.json", mode='w') as f:
                    json.dump(data, f)
            program.calculaterank(self,vgroup,vintegrant, data["groups"][vgroup]["integrants"][vintegrant]["rank"])
        elif new_exp>maxexp:
            aux = new_exp-maxexp
            data["groups"][vgroup]["integrants"][vintegrant]["exp"] = 0
            data["groups"][vgroup]["integrants"][vintegrant]["rank"] +=1
            data["groups"][vgroup]["integrants"][vintegrant]["maxexp"] = program.new_maxexp(data["groups"][vgroup]["integrants"][vintegrant]["rank"])
            with open("data_test.json", mode='w') as f:
                    json.dump(data, f)
            program.keepadding(self,vgroup,vintegrant, aux)
        
        with open("data_test.json", mode='w') as f:
                json.dump(data, f)
        program.totalexp_pack_forget(self,1,vgroup,vintegrant)

    def calculaterank(self,vgroup,vintegrant, newrank):
        rexp = {1:1,2:1,3:2,4:3,5:3,6:4,7:4,8:4,9:4,10:4,11:5,12:5,13:5,14:5,15:5,16:6,17:6,18:6,19:6,20:6,
                21:7,22:7,23:7,24:7,25:7,26:8,27:8,28:8,29:8,30:8,31:9,32:9,33:9,34:9,35:9}
        if(newrank>=36 and newrank<110):
            data["groups"][vgroup]["integrants"][vintegrant]["maxexp"] = 10
        else:
            data["groups"][vgroup]["integrants"][vintegrant]["maxexp"] = rexp[newrank]

        with open("data_test.json", mode='w') as f:
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

    def add_data(self, vgroup):
        if vgroup == 0:
            self.labelar1 = tkinter.Label(self.window, text=data["groups"][vgroup]["integrants"][0]["namei"])
            self.labelar1.pack()

            self.new_rank1 = tkinter.Entry()
            self.new_rank1.insert(0,data["groups"][vgroup]["integrants"][0]["rank"])
            self.new_rank1.pack()

            self.new_exp1 = tkinter.Entry()
            self.new_exp1.insert(0,data["groups"][vgroup]["integrants"][0]["exp"])
            self.new_exp1.pack()

            self.labelar2 = tkinter.Label(self.window, text=data["groups"][vgroup]["integrants"][1]["namei"])
            self.labelar2.pack()

            self.new_rank2 = tkinter.Entry()
            self.new_rank2.insert(0,data["groups"][vgroup]["integrants"][1]["rank"])
            self.new_rank2.pack()

            self.new_exp2 = tkinter.Entry()
            self.new_exp2.insert(0,data["groups"][vgroup]["integrants"][1]["exp"])
            self.new_exp2.pack()

            self.labelar3 = tkinter.Label(self.window, text=data["groups"][vgroup]["integrants"][2]["namei"])
            self.labelar3.pack()

            self.new_rank3 = tkinter.Entry()
            self.new_rank3.insert(0,data["groups"][vgroup]["integrants"][2]["rank"])
            self.new_rank3.pack()

            self.new_exp3 = tkinter.Entry()
            self.new_exp3.insert(0,data["groups"][vgroup]["integrants"][2]["exp"])
            self.new_exp3.pack()

            self.labelar4 = tkinter.Label(self.window, text=data["groups"][vgroup]["integrants"][3]["namei"])
            self.labelar4.pack()

            self.new_rank4 = tkinter.Entry()
            self.new_rank4.insert(0,data["groups"][vgroup]["integrants"][3]["rank"])
            self.new_rank4.pack()

            self.new_exp4 = tkinter.Entry()
            self.new_exp4.insert(0,data["groups"][vgroup]["integrants"][3]["exp"])
            self.new_exp4.pack()

            self.labelar5 = tkinter.Label(self.window, text=data["groups"][vgroup]["integrants"][4]["namei"])
            self.labelar5.pack()

            self.new_rank5 = tkinter.Entry()
            self.new_rank5.insert(0,data["groups"][vgroup]["integrants"][4]["rank"])
            self.new_rank5.pack()

            self.new_exp5 = tkinter.Entry()
            self.new_exp5.insert(0,data["groups"][vgroup]["integrants"][4]["exp"])
            self.new_exp5.pack()


            self.labelar6 = tkinter.Label(self.window, text=data["groups"][vgroup]["integrants"][5]["namei"])
            self.labelar6.pack()

            self.new_rank6 = tkinter.Entry()
            self.new_rank6.insert(0,data["groups"][vgroup]["integrants"][5]["rank"])
            self.new_rank6.pack()

            self.new_exp6 = tkinter.Entry()
            self.new_exp6.insert(0,data["groups"][vgroup]["integrants"][5]["exp"])
            self.new_exp6.pack()


        else:
            self.labelar1 = tkinter.Label(self.window, text=data["groups"][vgroup]["integrants"][0]["namei"])
            self.labelar1.pack()

            self.new_rank1 = tkinter.Entry()
            self.new_rank1.insert(0,data["groups"][vgroup]["integrants"][0]["rank"])
            self.new_rank1.pack()

            self.new_exp1 = tkinter.Entry()
            self.new_exp1.insert(0,data["groups"][vgroup]["integrants"][0]["exp"])
            self.new_exp1.pack()

            self.labelar2 = tkinter.Label(self.window, text=data["groups"][vgroup]["integrants"][1]["namei"])
            self.labelar2.pack()

            self.new_rank2 = tkinter.Entry()
            self.new_rank2.insert(0,data["groups"][vgroup]["integrants"][1]["rank"])
            self.new_rank2.pack()

            self.new_exp2 = tkinter.Entry()
            self.new_exp2.insert(0,data["groups"][vgroup]["integrants"][1]["exp"])
            self.new_exp2.pack()

            self.labelar3 = tkinter.Label(self.window, text=data["groups"][vgroup]["integrants"][2]["namei"])
            self.labelar3.pack()

            self.new_rank3 = tkinter.Entry()
            self.new_rank3.insert(0,data["groups"][vgroup]["integrants"][2]["rank"])
            self.new_rank3.pack()

            self.new_exp3 = tkinter.Entry()
            self.new_exp3.insert(0,data["groups"][vgroup]["integrants"][2]["exp"])
            self.new_exp3.pack()

            self.labelar4 = tkinter.Label(self.window, text=data["groups"][vgroup]["integrants"][3]["namei"])
            self.labelar4.pack()

            self.new_rank4 = tkinter.Entry()
            self.new_rank4.insert(0,data["groups"][vgroup]["integrants"][3]["rank"])
            self.new_rank4.pack()

            self.new_exp4 = tkinter.Entry()
            self.new_exp4.insert(0,data["groups"][vgroup]["integrants"][3]["exp"])
            self.new_exp4.pack()
        
        self.buttonar1 = tkinter.Button(self.window, text="Añadir datos", command= lambda:program.overwrite(self, vgroup))
        self.buttonar1.pack()
        self.buttonar2 = tkinter.Button(self.window, text="Atrás", command= lambda:program.add_data_pack_forget(self, vgroup, 0))
        self.buttonar2.pack() 
        self.buttonar3 = tkinter.Button(self.window, text="Salir", command= self.window.destroy)
        self.buttonar3.pack() 

    def add_data_pack_forget(self, vgroup, aux):
        self.add=False
        
        self.labelar1.pack_forget()
        self.labelar2.pack_forget()
        self.labelar3.pack_forget()
        self.labelar4.pack_forget()
        self.buttonar1.pack_forget()
        self.buttonar2.pack_forget()
        self.buttonar3.pack_forget()

        self.new_rank1.pack_forget()
        self.new_exp1.pack_forget()
        self.new_rank2.pack_forget()
        self.new_exp2.pack_forget()
        self.new_rank3.pack_forget()
        self.new_exp3.pack_forget()
        self.new_rank4.pack_forget()
        self.new_exp4.pack_forget()

        if vgroup == 0:
            self.labelar5.pack_forget()
            self.new_rank5.pack_forget()
            self.new_exp5.pack_forget()
            self.labelar6.pack_forget()
            self.new_rank6.pack_forget() 
            self.new_exp6.pack_forget()

        if aux == 0:
            program.main(self)
        else:
            window2 = tkinter.Tk()
            window2.geometry("200x50")
            labelextra = tkinter.Label(window2, text="Datos actualizados correctamente.")
            labelextra.pack()
            buttonextra = tkinter.Button(window2, text="Ok", command= window2.destroy)
            buttonextra.pack()
            program.main(self) 
            window2.mainloop()
            

    def overwrite(self, vgroup): #TODO: hacer tratamiento de excepciones, rank mayor, exp no cuadra, etc. type (numero) == int
        if vgroup == 0:
            data["groups"][vgroup]["integrants"][0]["rank"] = int(self.new_rank1.get())
            data["groups"][vgroup]["integrants"][0]["exp"] = int(self.new_exp1.get())

            data["groups"][vgroup]["integrants"][1]["rank"] = int(self.new_rank2.get())
            data["groups"][vgroup]["integrants"][1]["exp"] = int(self.new_exp2.get())

            data["groups"][vgroup]["integrants"][2]["rank"] = int(self.new_rank3.get())
            data["groups"][vgroup]["integrants"][2]["exp"] = int(self.new_exp3.get())

            data["groups"][vgroup]["integrants"][3]["rank"] = int(self.new_rank4.get())
            data["groups"][vgroup]["integrants"][3]["exp"] = int(self.new_exp4.get())

            data["groups"][vgroup]["integrants"][4]["rank"] = int(self.new_rank5.get())
            data["groups"][vgroup]["integrants"][4]["exp"] = int(self.new_exp5.get())

            data["groups"][vgroup]["integrants"][5]["rank"] = int(self.new_rank6.get())
            data["groups"][vgroup]["integrants"][5]["exp"] = int(self.new_exp6.get())
        
        else:
            data["groups"][vgroup]["integrants"][0]["rank"] = int(self.new_rank1.get())
            data["groups"][vgroup]["integrants"][0]["exp"] = int(self.new_exp1.get())

            data["groups"][vgroup]["integrants"][1]["rank"] = int(self.new_rank2.get())
            data["groups"][vgroup]["integrants"][1]["exp"] = int(self.new_exp2.get())

            data["groups"][vgroup]["integrants"][2]["rank"] = int(self.new_rank3.get())
            data["groups"][vgroup]["integrants"][2]["exp"] = int(self.new_exp3.get())

            data["groups"][vgroup]["integrants"][3]["rank"] = int(self.new_rank4.get())
            data["groups"][vgroup]["integrants"][3]["exp"] = int(self.new_exp4.get())

        with open("data_test.json", mode='w') as f:
            json.dump(data, f)

        program.add_data_pack_forget(self, vgroup, 1)
          

if __name__ == '__main__':
    program()

#TODO: mirar max_exp en data_test.json