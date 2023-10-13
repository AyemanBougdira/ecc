class Student:
    def __init__(self, name, house):
        #if not name:    # if name == ""
            #raise ValueError
        #if house not in ["Rabat", "Agadir"]:
            #raise ValueError("Invalid house")
        self.name = name   # store the variables
        self.house = house     #this line calls setter methode
        #self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:    # if name == ""
            raise ValueError
        self._name = name

    

    #Getter
    @property
    def house(self):
        return self._house      # NOTE SELF._ 
    
    #Setter:
    @house.setter
    def house(self, house):
        if house not in ["Rabat", "Agadir"]:
            raise ValueError("Invalid house")
        self._house = house


    
    #invent my own function:
    #def charm(self):
        #match self.patronus:             #if elif, else
            #case "Stag":
                #return "A"
            #case "Otter":
                #return "B" 
            #case "Jack Russell terrier":
                #return "C"  
            #case _:
                #return "/"
def main():
    student = Student.get()    # ""imprtant""
    #print("Expecto Patronum!")
    #print(student.charm())
    #student.house = "111, 119"     #classe give more controle on data --> this line calls house(self,house); use the setter
    #student_.house = "111, 119"     
    print(student)


#def get_student():
    #name = input("Name:")
    #house = input("House: ")
    #patronus = input("Patronus: ")
    #return Student(name, house) #goind to instantiate a student object for me                 #able to customize the contents of that object

if __name__ == "__main__":
    main()