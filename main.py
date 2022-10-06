class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades1:
                lecturer.grades1[course] += [grade]
            else:
                lecturer.grades1[course] = [grade]
        else:
            return 'Ошибка'
    def mid1(self):
        sum = 0
        count = 0
        for x in self.grades.values():
            for y in x:
                sum += y
                count += 1
        return sum/count

    def __str__(self):
        r = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {round(self.mid1(), 2)}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return r

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        n = self.mid1() > other.mid1()
        if n == True:
            return f'Средняя оценка выше у {self.name}'
        else:
            return f'Средняя оценка выше у {other.name}'
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

        def rate_lec(self):
            return super().best_lecturer
        def rate_hw(self):
            return super().rate_hw

      
        
    
class Lecturer(Mentor):
  def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades1 = {}
  def mid1(self):
        sum = 0
        count = 0
        for x in self.grades1.values():
            for y in x:
                sum += y
                count += 1
        return sum/count
         
  def __str__(self):
        r = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self.mid1(), 2)}\n'
        return r
    
  def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        n = self.mid1() > other.mid1()
        if n == True:
            return f'У {self.name} больше'
        else:
            return f'Больше у {other.name}'      
    

  
class Reviewer(Mentor):
  def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
  def __str__(self):
        r = f'Имя: {self.name}\nФамилия: {self.surname}'
        return r

student1 = Student('Max', 'Verstappen', 'man')
student2 = Student('Checo', 'Perez', 'man')
reviewer1 = Reviewer('Lewis', 'Hamilton')
reviewer2 = Reviewer('George', 'Russel')
best_lectrer1 = Lecturer('Zhou', 'Guaniu')
best_lectrer2 = Lecturer('Valteri', 'Bottas')

student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']
student1.finished_courses += ['Введение в программирование']
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['Git']
student2.finished_courses += ['Введение в программирование']

reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['Git']
reviewer2.courses_attached += ['Python']
reviewer2.courses_attached += ['Git']

best_lectrer1.courses_attached += ['Python']
best_lectrer1.courses_attached += ['Git']
best_lectrer2.courses_attached += ['Python']
best_lectrer2.courses_attached += ['Git']

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Git', 10)
reviewer2.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'Python', 10)
reviewer2.rate_hw(student2, 'Git', 9)

student1.rate_lec(best_lectrer1, 'Python', 10)
student1.rate_lec(best_lectrer1, 'Python', 9)
student1.rate_lec(best_lectrer1, 'Git', 10)
student2.rate_lec(best_lectrer2, 'Python', 10)
student2.rate_lec(best_lectrer2, 'Python', 10)
student2.rate_lec(best_lectrer2, 'Git', 8)

def average_student(list, name_cource):
    sum = 0
    count = 0
    for x in list:
        for y in x.grades[name_cource]:
            sum += y
            count += 1
    return round(sum/count, 2)

def average_lectrer(list, name_cource):
    sum = 0
    count = 0
    for x in list:
        for y in x.grades1[name_cource]:
            sum += y
            count += 1
    return round(sum/count, 2)
  


print(student1.grades)
print(student2.grades)
print(best_lectrer1.grades1)
print(best_lectrer2.grades1)
print(reviewer1)
print(reviewer2)
print(best_lectrer1)
print(best_lectrer2)
print(student1)
print(student2)
print(student1 < student2)
print(best_lectrer1 < best_lectrer2)
print(average_student([student1, student2], 'Python'))
print(average_lectrer([best_lectrer1, best_lectrer2], 'Git'))



