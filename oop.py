class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lecture(self, lecturer, course, grade):
        if not (0 <= grade <= 10):
            return "Ошибка: оценка должна быть от 0 до 10"
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return

    def average_grade(self):
        total_grades = []
        for grades_list in self.grades.values():
            total_grades.extend(grades_list)
        if total_grades:
            return sum(total_grades) / len(total_grades)
        else:
            return 0
     
    def __str__(self):
        avg_grade = round(self.average_grade(), 1)
        courses_in_progress = ", ".join(self.courses_in_progress)
        finished_courses = ", ".join(self.finished_courses)
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {avg_grade}\n"
            f"Курсы в процессе изучения: {courses_in_progress}\n"
            f"Завершенные курсы: {finished_courses}"
        )
    
    def __lt__(self, other):
        if not isinstance (other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()
    
    def __gt__(self, other):
        if not isinstance (other, Student):
            return NotImplemented
        return self.average_grade() > other.average_grade()
    
    def __eq__(self, other):
        if not isinstance (other, Student):
            return NotImplemented
        return self.average_grade() == other.average_grade()
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def average_grade(self):
        total_grades = []
        for grades_list in self.grades.values():
            total_grades.extend(grades_list)
        if total_grades:
            return sum(total_grades) / len(total_grades)
        else:
            return 0

    def __str__(self):
        avg_grade = round(self.average_grade(), 1)
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade}")
    
    def __lt__(self, other):
        if not isinstance (other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()
    
    def __gt__(self, other):
        if not isinstance (other, Lecturer):
            return NotImplemented
        return self.average_grade() > other.average_grade()
    
    def __eq__(self, other):
        if not isinstance (other, Lecturer):
            return NotImplemented
        return self.average_grade() == other.average_grade()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}")


# 4 задание
    
def average_grade_course(students, course):
    total_grades = []
    for student in students:
        total_grades.extend(student.grades[course])
    if total_grades:
        return sum(total_grades) / len(total_grades)
    else:
        return 0
    
def average_lecturer_grade_course(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
            total_grades.extend(lecturer.grades[course])
    if total_grades:
        return sum(total_grades) / len(total_grades)
    else:
        return 0
      
student1 = Student('Alice', 'Ivanova', 'F')
student2 = Student('Bob', 'Petrov', 'M')
student1.courses_in_progress += ['Python', 'Math']
student2.courses_in_progress += ['Python', 'English']
student1.finished_courses += ['Intro to Programming']
student2.finished_courses += ['Basics of Python']

lecturer1 = Lecturer('Dr.', 'Smith')
lecturer2 = Lecturer('Prof.', 'Johnson')
lecturer1.courses_attached += ['Python', 'Math']
lecturer2.courses_attached += ['Python', 'English']

reviewer1 = Reviewer('Mr.', 'Brown')
reviewer2 = Reviewer('Ms.', 'Davis')
reviewer1.courses_attached += ['Python', 'Math']
reviewer2.courses_attached += ['Python', 'English']

# Студенты ставят оценки лекторам
student1.rate_lecture(lecturer1, 'Python', 9)
student1.rate_lecture(lecturer2, 'Python', 8)
student2.rate_lecture(lecturer2, 'Python', 7)

# Ревьюверы ставят оценки студентам
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Math', 9)
reviewer2.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student2, 'English', 7)

# Вывод информации
print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

# Сравнение лекторов и студентов
print(f"lecturer1 > lecturer2? {lecturer1 > lecturer2}")
print(f"student1 < student2? {student1 < student2}")

# Подсчет среднего балла по курсу
students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print(f"Средняя оценка студентов за курс Python: {average_grade_course(students, 'Python'):.1f}")
print(f"Средняя оценка лекторов за курс Python: {average_lecturer_grade_course(lecturers, 'Python'):.1f}")