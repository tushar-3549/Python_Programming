def method_name(a,b):
    print("A Method")

class Person:
    def __init__(self,person_name : str,date_of_birth : int ,height : int):
        self.__name = person_name
        self.__DOB = date_of_birth
        self.__ht = height
        self.abc = None
        
    def get_name(self):
        return self.__name
    
    def set_name(self,new_name):
        if self.__has_any_number(new_name):
            print("Sorry ! person name can't have any number !")
            return 
        self.__name = new_name
    
    def get_summary(self):
        return f"Name : {self.__name} , Date Of Birth :{self.__DOB} , Height : {self.__ht}"
    
    def __has_any_number(self,string):
        return "0" in string 
        

method_name(10,20)
a_person = Person("Tushar","2000","5 feet 9 inchees")
#b_person = Person("Maruf")

print(a_person.get_name())
#print(b_person.get_name())
print(a_person.get_summary())

a_person.set_name("Sakib Al Hasan")
print(a_person.get_summary())
#print(a_person.__DOB)       # why don't show output __ 
a_person.set_name("06Tushar")
#print(a_person.name)




