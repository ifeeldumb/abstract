import abc

class Animal(abc.ABC):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
        
    @abc.abstractmethod
    def get_type(self):
        pass

class Mammal(Animal):
    def get_type(self):
        return "Млекопитающее"

class Bird(Animal):
    def get_type(self):
        return "Птица"

class Reptile(Animal):
    def get_type(self):
        return "Рептилия"

# "База данных" животных
animals_db = {
    1: [Mammal("Лев", 5), Mammal("Слон", 10), Mammal("Тигр", 4)],
    2: [Bird("Орел", 3), Bird("Попугай", 2), Bird("Сова", 6)],
    3: [Reptile("Крокодил", 12), Reptile("Змея", 7), Reptile("Черепаха", 50)]
}