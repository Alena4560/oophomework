class Mentor:
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname


class Student:
	def __init__(self, name, surname, gender):
		self.grades = {}
		self.average = 0
		self.name = name
		self.surname = surname
		self.gender = gender
		self.finished_courses = []
		self.courses_in_progress = []
	
	def add_courses(self, course_name):
		self.finished_courses.append(course_name)
	
	def rate_hw(self, lecturer, course, grade):
		if isinstance(lecturer, Lecturer) and course in lecturer.courses_in_progress:
			if course in lecturer.grades:
				lecturer.grades[course] += [grade]
			else:
				lecturer.grades[course] = [grade]
		else:
			return 'Ошибка'
	
	def __average_rating(self):
		summa = sum(self.grades.values())
		average = summa / len(self.grades) if len(self.grades) > 0 else 0
		return f'Средняя оценка за домашние задания: {average}'
	
	def __str__(self):
		return (
			f'Имя: {self.name}\nФамилия: {self.surname}\n{self.__average_rating()}\nКурсы в процессе изучения: '
			f'{self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}\n')
	
	def __lt__(self, other):
		return self.average < other.average
	def __gt__(self, other):
		return self.average > other.average


class Lecturer(Mentor):
	def __init__(self, name, surname, course):
		super().__init__(name, surname)
		self.average = 0
		self.courses_in_progress = []
		self.grades = {'Python-разработка': 0,
			'Front-end-разработка': 0,
			'Java-разработка': 0,
			'Golang-разработка': 0,
			'C#-разработка': 0}
		self.courses_attached = course
		
	def __average_rating(self):
		summa = sum(self.grades.values())
		average = summa / len(self.grades) if len(self.grades) > 0 else 0
		return f'Средняя оценка за лекции: {average}'
	
	def __str__(self):
		return f'Имя: {self.name}\nФамилия: {self.surname}\n{self.__average_rating()}\n'
	
	def __lt__(self, other):
		return self.average < other.average
	def __gt__(self, other):
		return self.average > other.average


class Reviewer(Mentor):
	def __init__(self, name, surname):
		super().__init__(name, surname)
		self.courses_attached = None
	
	def rate_hw(self, student, course, grade):
		if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
			if course in student.grades:
				student.grades[course] += [grade]
			else:
				student.grades[course] = [grade]
		else:
			return 'Ошибка'
	
	def __str__(self):
		print('Имя: ' + str(self.name), 'Фамилия: ' + str(self.surname), sep='\n')
		return

def average_rating_for_all_student(student_list, course):
	marks_of_homework = 0
	for student in student_list:
		if isinstance(student, Student) and course in student.grades:
			marks_of_homework += student.grades[course]
	return marks_of_homework/len(student_list)

def average_rating_for_all_lecturer(lecturer_list, course):
	marks_for_lecture = 0
	for lecturer in lecturer_list:
		if isinstance(lecturer, Lecturer) and course in lecturer.grades:
			marks_for_lecture += lecturer.grades[course]
	return marks_for_lecture / len(lecturer_list)

maksim = Student('Максим', 'Кузнецов', 'муж')
lisa = Student('Лиза', 'Обухова', 'жен')
oleg = Mentor('Олег', 'Булыгин')
dmitriy = Mentor('Дмитрий', 'Иванов')
alena = Lecturer('Алена', 'Самарская', 'Python-разработка')
marina = Lecturer('Марина', 'Узелкова', 'Python-dev')
alexey = Reviewer('Алексей', 'Крупеников')
peter = Reviewer('Петр', 'Сергеев')
print(alena)
print(maksim)
maksim.rate_hw(marina, 'Python-разработка', 5)
print(maksim<lisa)
print(alena>marina)
print(average_rating_for_all_student([maksim, lisa], 'Python-разработка'))
print(average_rating_for_all_lecturer([alena, marina], 'Front-end-разработка'))
