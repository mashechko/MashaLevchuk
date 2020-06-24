class Person:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.subjects = []

    def set_subject(self, subject):
        self.subjects.append(subject)


class Student(Person):
    def __init__(self, name, lastname, age):
        super().__init__(name, lastname, age)
        self.estimate = {}
        self.teachers = []

    def set_teachers(self, teacher):
        self.teachers.append(teacher)

    def set_estimate(self, subject, estimate):
        if subject not in self.subjects:
            print('Сначала добавьте предмет')
        else:
            self.estimate[subject] = estimate


class Teacher(Person):
    def __init__(self, name, lastname, age):
        super().__init__(name, lastname, age)
        self.students = []

    def set_students(self, student):
        self.students.append(student)


pasha = Teacher('Pavel', 'Pavlovich', 35)
pasha.set_subject('mathematics')
pasha.set_subject('physics')

masha = Student('Masha', 'Levchuk', 19)

masha.set_teachers(pasha)
pasha.set_students(masha)

pasha_students = pasha.students

for student in pasha_students:
    print(student.name)

masha.set_estimate('economics', 8)
print(masha.estimate)
masha.set_subject('economics')
masha.set_estimate('economics', 10)
print(masha.estimate)
