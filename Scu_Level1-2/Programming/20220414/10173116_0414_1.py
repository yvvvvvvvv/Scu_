class Animals():
    '''基底類別'''
    def __init__(self,animal_name,animal_age):
        self.name = animal_name #動物名稱
        self.age = animal_age #動物年齡
    def run(self):
        print(self.name.title(), 'is running')

class Dogs(Animals):
    '''衍生類別'''
    def __init__(self, dog_name, dog_age):
        self.name1 = dog_name
        super().__init__('My pet ' + dog_name.title(), dog_age)
    def sleep(self):
        print(self.name1.title(), 'is sleeping')

class Birds(Animals):
    '''衍生類別'''
    def __init__(self, bird_name, bird_age):
        self.name2 = bird_name
        super().__init__('My pet ' + bird_name.title(), bird_age)
    def fly(self):
        print(self.name2.title(), 'is flying')

mycat = Animals('lucy', 5)
print(mycat.name.title(), 'is', mycat.age, 'years old')
mycat.run()

mydog = Dogs('lily', 6)
print(mydog.name.title(), 'is', mydog.age, 'years old')
mydog.run()
mydog.sleep()

mybird = Birds('cici', 8)
print(mybird.name.title(), 'is', mybird.age, 'years old')
#mybird.run()
mybird.fly()