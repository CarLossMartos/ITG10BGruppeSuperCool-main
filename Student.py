import LoginData
import Subject
import Marks


class Student:
    def __int__(self, subject: Subject, surname: str, name: str, loginData: LoginData, marks: Marks):
        self.subject = subject
        self.surname = surname
        self.name = name
        self.loginData = loginData
        self.marks = marks