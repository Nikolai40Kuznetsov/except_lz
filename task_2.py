class Animal:
    ''''''
    def __init__(self, name:str, age:int, species:str):
        self.name = name
        self.age = age
        self.species = species


    def get_info(self):
        print(f"Имя животного: {self.name}, его возраст: {self.age}, Разновидность животного: {self.species}")


    def make_sound(self):
        pass

class Dog(Animal):

    def __init__(self, name:str ,age: int, species:str, breed:str ,guard_status:bool):
        super().__init__(name,age,species)
        self.breed = breed
        self.guard_status = guard_status

    def get_info(self):
        super().get_info()
        print(f"Порода собаки: {self.breed} ")
        
    def guard_house(self):
        
        if self.guard_status != True:
            print("Не охраняет дом")
        else:
            print("Дом под охраной")

def main():
    dog = Dog("Норд",8,"собака","хаски",False)
    dog.guard_house()
    dog.get_info()

if __name__ =="__main__":
    main()