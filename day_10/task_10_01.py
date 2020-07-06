# Задание 1 Переопределить методы change_weight, change_height в классе Parrot. В случае не передачи параметра - вес
# изменяется на 0.05
class Pet:
    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height

    @classmethod
    def jump(cls):
        print('Jump!')

    @classmethod
    def run(cls):
        print('Run!')

    @classmethod
    def sleep(cls):
        print('Time to sleep...')

    def birthday(self):
        self.age += 1

    def change_weight(self, change=None):
        if change:
            self.weight += change
        else:
            self.weight += 0.2

    def change_height(self, change=None):
        if change:
            self.height += change
        else:
            self.height += 0.2


class Parrot(Pet):
    def __init__(self, name, age, master, weight, height):
        super().__init__(name, age, master, weight, height)

    def fly(self):
        if self.weight > 0.1:
            print('This parrot cannot fly')
        else:
            print('Fly!')

    def change_weight(self, change=None):
        if change:
            self.weight += change
        else:
            self.weight = 0.05

    def change_height(self, change=None):
        if change:
            self.height += change
        else:
            self.height += 0.05


parrot = Parrot('Kesha', 1, 'Masha', 0.7, 50)
parrot.fly()
parrot.change_weight()
parrot.fly()