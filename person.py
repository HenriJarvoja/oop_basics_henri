class Person():
    name = 'Person name'
    age = 0

    def setPerson(self, name, age):
        self.name = name
        self.age = age

def birthday(self):
    self.age = self.age + 1

    def info(self):
        print(self.name)
        print(self.age)

henri = Person()
henri.setPerson('Henri', 17)
henri.info()
henri.birthday()
henri.info()
