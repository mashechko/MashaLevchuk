# 3. Добавить два метода в класс Dog: jump и run. Методы выводят на экран Jump! и Run! соответственно.
class Dog:
    @classmethod
    def jump(cls):
        print('Jump!')

    @classmethod
    def run(cls):
        print('Run!')


Dog.jump()
Dog.run()
