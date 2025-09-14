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
      
