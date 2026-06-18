class parent:
    def __init__(self,bran,model,fuel,color):
        self.bran=bran
        self.model=model
        self.fuel=fuel
        self.color=color
    
    def get_color(self):
        return self.color
    
    def set_color(self,new_color):
        self.color=new_color
        return self.color
    
    def showCar(self):
        print("hi i am a car of brand {}, model {}, fuel {}, color {}".format(self.bran, self.model, self.fuel, self.color))

class child(parent):
    def __init__(self, bran, model, fuel, color, year,tramsission,turbo):
        parent.__init__(self,bran,model,fuel,color)
        self.year=year
        self.tramsisson=tramsission
        self.turbo=turbo

    def showcar(self):
        print("hi i am a car of brand {}, model {} , fuel {}, color {}, year {}, tramsission {} , turbo {}".format(self.bran,self.model,self.fuel
                                                                                                                   ,self.color,self.year,self.tramsisson
                                                                                                                   ,self.turbo))
        
mini = child("mini","cooper","petrol","red","2018","automatic","no")

print(mini.get_color())
print(mini.set_color("yellow"))
print(mini.get_color())
mini.showcar()