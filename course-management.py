print('============================================================')
print('                                                            ')
print('                 Course Management System                   ')
print('                                                            ')
print('============================================================')
print('                                                            ')
print('                                                            ')
print('Menu:')
print('1. Add student')
print('2. Add course')
print('3. Enroll student in course')
print('4. Show student courses')
print('5. Show course students')
print('6. Exit')
print( '                          ')


class student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.student_course = []

class course:
    def __init__(self, course_id, title):
        self.course_id = course_id
        self.title = title
        self.course_student = []


class process_data:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, student_id, name):
        students = student(student_id, name)
        self.student_list.append(students)
    
    def add_course(self, course_id, title):
        courses = course(course_id, title)
        self.course_list.append(courses)

    def enroll(self, student_id, course_id):
        for s in self.student_list:
            for c in self.course_list:
                if c.course_id == course_id and s.student_id == student_id:
                    s.student_course.append(c.title)
                    c.course_student.append(s.name)
                    

    def student_c_list(self, student_id):
        for s in self.student_list:
            if student_id == s.student_id:
                print(f'Course attended by {s.name}')


        for s in self.student_list:
            for i in s.student_course:
                if student_id == s.student_id:
                    print(f'- {i}')
    
    def course_s_list(self, course_id):
        for c in self.course_list:
            if course_id == c.course_id:
                print(f'Course {c.title} attendants: ')


        for c in self.course_list:
            for i in c.course_student:
                if course_id == c.course_id:
                    print(f'- {i}')
        
    def running_app(self):
        while True:
            try:
                option = input('Choose and option: ')

                if option == '1':
                    student_id = input('Enter student ID: ').title()
                    name = input('Enter student name: ').title()
                    self.add_student(student_id, name)

                    print('Student added!')
                
                elif option == '2':
                    course_id = input('Enter course code: ').title()
                    title = input('Enter course title: ').title()

                    self.add_course(course_id, title)

                    print('Course added!')
                
                elif option == '3':
                    if not self.student_list or not self.course_list:
                        print('No courses or students added yet')
                    else:
                        student_id = input('Enter student ID: ').title()
                        course_id = input('Enter course code: ').title()

                        self.enroll(student_id, course_id)
                        print('Student enroll in course!')

                elif option == '4':
                    if not self.student_list:
                        print('No students on the list')
                    else:
                        student_id = input('Enter student ID: ').title()

                        self.student_c_list(student_id)

                        for s in self.student_list:
                            if not student_id == s.student_id:
                                print('No student by that ID')
                
                elif option == '5':
                    if not self.course_list:
                        print('No course enroll by students yet')
                    else:
                        course_id = input('Enter course code: ').title()
                        
                        self.course_s_list(course_id)
                        
                        for c in self.course_list:
                            if not course_id == c.course_id:
                                print('No course by that code')
                        

                elif option == '6':
                    print('Thank you for using the app')
                    break
                
                else:
                    raise ValueError
                
            except ValueError:
                print('Error: Invalid input')

            print('')

if __name__  == '__main__':
    manajemen = process_data()
    manajemen.running_app()



            

        