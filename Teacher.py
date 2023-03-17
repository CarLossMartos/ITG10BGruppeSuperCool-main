import LoginData
import Student


class Teacher:
    def __int__(self, subject: list, student: Student, loginData: LoginData, surname: str, name: str):
        self.subject = subject
        self.student = student
        self.loginData = loginData
        self.surname = surname
        self.name = name