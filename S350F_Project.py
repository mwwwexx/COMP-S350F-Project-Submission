import tkinter as tk
from tkinter import messagebox


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Student(User):
    def __init__(self, username, password, student_id):
        super().__init__(username, password)
        self.student_id = student_id
        self.courses = []
        self.grades = {}
        self.attendance = {}

    def display_info(self):
        messagebox.showinfo("Student Information", f"Student ID: {self.student_id}\nUsername: {self.username}")

    def view_enrolled_courses(self):
        if self.courses:
            messagebox.showinfo("Enrolled Courses", "\n".join(self.courses))
        else:
            messagebox.showinfo("Enrolled Courses", "You are not enrolled in any courses.")

    def update_personal_info(self):
        new_username = input_dialog("Update Username", "Enter new username:")
        new_password = input_dialog("Update Password", "Enter new password:")
        self.username = new_username
        self.password = new_password
        messagebox.showinfo("Success", "Account information updated successfully!")
        
    def view_grades(self):
        if self.grades:
            grades_text = "\n".join([f"Course: {course} - Grade: {grade}" for course, grade in self.grades.items()])
            messagebox.showinfo("Grades", grades_text)
        else:
            messagebox.showinfo("Grades", "No grades available.")
            
    def view_attendance(self):
        if self.attendance:
            attendance_text = "\n".join([f"Course: {course} - Attendance Rate: {rate}%" for course, rate in self.attendance.items()])
            messagebox.showinfo("Attendance", attendance_text)
        else:
            messagebox.showinfo("Attendance", "No attendance records available.")
    
    def student_menu(self):
        stu_menu = tk.Tk()
        stu_menu.title("Student Menu")
        stu_menu.geometry("300x200")
        
        display_info_button = tk.Button(stu_menu, text="Show Info",command=self.display_info)
        display_info_button.pack()

        courses_button = tk.Button(stu_menu, text="View Enrolled Courses", command=self.view_enrolled_courses)
        courses_button.pack()

        info_button = tk.Button(stu_menu, text="Update Personal Information", command=self.update_personal_info)
        info_button.pack()

        grades_button = tk.Button(stu_menu, text="View Grades", command=self.view_grades)
        grades_button.pack()

        attendance_button = tk.Button(stu_menu, text="View Attendance", command=self.view_attendance)
        attendance_button.pack()

        logout_button = tk.Button(stu_menu, text="Logout", command=lambda: [stu_menu.destroy(), main()])
        logout_button.pack()
        stu_menu.mainloop()

class Teacher(User):
    def __init__(self, username, password, teacher_id):
        super().__init__(username, password)
        self.teacher_id = teacher_id

    def display_info(self):
        messagebox.showinfo("Teacher Information", f"Teacher ID: {self.teacher_id}\nUsername: {self.username}")
        
    def view_student_info(self):
        username = input_dialog("View Student Information", "Enter student username:")
        student = next((s for s in students if s.username == username), None)
        if student != None:
            student.display_info()
        else:
            messagebox.showinfo("Error", "Student not found.")

    def view_all_students_info(self):
        students_info = "\n".join([f"Student ID: {student.student_id}\nUsername: {student.username}\n" for student in students])
        messagebox.showinfo("All Students' Information", students_info)

    def update_student_courses(self):
        username = input_dialog("View Student Information", "Enter student username:")
        student = next((s for s in students if s.username == username), None)
        if student != None:
            num_courses = int(input_dialog("Update Courses", "Enter the number of courses:"))
            courses = []
            for i in range(num_courses):
                course = input_dialog("Update Courses", f"Enter course {i+1}:")
                courses.append(course)
                student.courses = courses
                messagebox.showinfo("Success", "Courses updated successfully!")
        else:
            messagebox.showinfo("Error", "Student not found.")
            
    def update_student_grades(self):
        username = input_dialog("View Student Information", "Enter student username:")
        student = next((s for s in students if s.username == username), None)
        if student != None:
            for course in student.courses:
                grade = input_dialog("Update Grades", f"Enter grade for course {course}:")
                student.grades[course] = grade
                messagebox.showinfo("Success", "Grades updated successfully!")
        else:
            messagebox.showinfo("Error", "Student not found.")
            
    def update_student_attendance(self):
        username = input_dialog("View Student Information", "Enter student username:")
        student = next((s for s in students if s.username == username), None)
        if student != None:
            for course in student.courses:
                attendance = input_dialog("Update Attendance", f"Enter attendance rate for course {course}:")
                student.attendance[course] = attendance
                messagebox.showinfo("Success", "Attendance updated successfully!")
        else:
            messagebox.showinfo("Error", "Student not found.")
            
    def teacher_menu(self):        
        tea_menu = tk.Tk()
        tea_menu.title("Teacher Menu")
        tea_menu.geometry("400x300")
        
        display_info_button = tk.Button(tea_menu, text="Show Info",command=self.display_info)
        display_info_button.pack()
                
        students_info_button = tk.Button(tea_menu, text="View Students' Information",command=self.view_student_info)
        students_info_button.pack()
        
        allstudents_info_button = tk.Button(tea_menu, text="View All Students' Information",command=self.view_all_students_info)
        allstudents_info_button.pack()

        courses_button = tk.Button(tea_menu, text="Update Student's Courses",command=self.update_student_courses)
        courses_button.pack()

        grades_button = tk.Button(tea_menu, text="Update Student's Grades",command=self.update_student_grades)
        grades_button.pack()

        attendance_button = tk.Button(tea_menu, text="Update Student's Attendance",command=self.update_student_attendance)
        attendance_button.pack()

        logout_button = tk.Button(tea_menu, text="Logout", command=lambda: [tea_menu.destroy(), main()])
        logout_button.pack()
        tea_menu.mainloop()
        
class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def display_info(self):
        messagebox.showinfo("Admin Information", f"Admin Username: {self.username}")

    def create_user_account(self):
        username = input_dialog("Create User Account", "Enter new username:")
        password = input_dialog("Create User Account", "Enter new password:")
        role = input_dialog("Create User Account", "Enter role (student/teacher):")

        if role == "student":
            student_id = input_dialog("Create User Account", "Enter student ID:")
            student = Student(username, password, student_id)
            students.append(student)
            messagebox.showinfo("Success", "Student account created successfully!")
        elif role == "teacher":
            teacher_id = input_dialog("Create User Account", "Enter teacher ID:")
            teacher = Teacher(username, password, teacher_id)
            teachers.append(teacher)
            messagebox.showinfo("Success", "Teacher account created successfully!")
        else:
            messagebox.showinfo("Error", "Invalid role. User account creation failed.")

    def delete_user_account(self):
        username = input_dialog("Delete User Account", "Enter username of the account to delete:")
        student = next((s for s in students if s.username == username), None)
        teacher = next((t for t in teachers if t.username == username), None)
       
        if student:
            students.remove(student)
            messagebox.showinfo("Success", "Student account deleted successfully!")
        elif teacher:
            teachers.remove(teacher)
            messagebox.showinfo("Success", "Teacher account deleted successfully!")
        else:
            messagebox.showinfo("Error", "Account not found. Deletion failed.")
    
    def admin_menu(self):
        adm_menu = tk.Tk()
        adm_menu.title("Admin Menu")
        adm_menu.geometry("300x200")
        
        display_info_button = tk.Button(adm_menu, text="Show Info",command=self.display_info)
        display_info_button.pack()

        create_button = tk.Button(adm_menu, text="Create User Account", command=self.create_user_account)
        create_button.pack()

        delete_button = tk.Button(adm_menu, text="Delete User Account", command=self.delete_user_account)
        delete_button.pack()

        logout_button = tk.Button(adm_menu, text="Logout", command=lambda: [adm_menu.destroy(), main()])
        logout_button.pack()
        adm_menu.mainloop()

# Sample data
admins = [
    Admin("admin", "adminpassword")
]

students = [
    Student("student1", "password1", "S001"),
    Student("student2", "password2", "S002"),
    Student("student3", "password3", "S003")
]

teachers = [
    Teacher("teacher1", "password1", "T001"),
    Teacher("teacher2", "password2", "T002"),
    Teacher("teacher3", "password3", "T003")
]

def input_dialog(title, prompt):
    return tk.simpledialog.askstring(title, prompt)

def login_menu():
    login = tk.Tk()
    login.title("User Login")
    login.geometry("300x200")     
    username_label = tk.Label(login, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(login)
    username_entry.pack()

    password_label = tk.Label(login, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(login, show="*")
    password_entry.pack()
    
    login_button = tk.Button(login, text="Login")
    login_button.pack() 
    
    login.mainloop()
def get_username():
    username = login_menu().username_entry.get()
    password = login_menu().password_entry.get()
    return username, password

# Login function
def login():
    
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    user = None
    user_type = None
    for admin in admins:
        if admin.username == username and admin.password == password:
            user = admin
            user_type = "admin"
            break

    for student in students:
        if student.username == username and student.password == password:
            user = student
            user_type = "student"
            break

    for teacher in teachers:
        if teacher.username == username and teacher.password == password:
            user = teacher
            user_type = "teacher"
            break

    return user, user_type

# Main program
def main():
    while True:
        user, user_type = login()

        if user== None or user_type == None:
            print("Invalid username or password.")
            break
        else:
            print(f"Logged in as {user_type}.")
            if user_type == "student":
                student = user
                student.display_info()
                student.student_menu()
                
            elif user_type == "teacher":
                teacher = user
                teacher.display_info()
                teacher.teacher_menu()
                
            elif user_type == "admin":
                admin = user
                admin.display_info()
                admin.admin_menu()
       
        


# Run the program
main()
