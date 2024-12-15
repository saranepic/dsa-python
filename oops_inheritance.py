class Pet:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    def show(self):
        print(f'I am {self.name} and {self.age} years old')
    def speak(self):
        print('I don\'t speak')

class Cat(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color
    def speak(self):
        print(f"Meow, I am {self.name}")

p = Pet("Saran",24)
c = Cat("Walter",12,"Pink") 
c.show()
print(c.speak())
