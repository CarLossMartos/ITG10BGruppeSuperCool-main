import Student
import Teacher


class Subject:
    def __int__(self,subjectName: str, student: Student, teacher: Teacher):
        self.subjectName = subjectName
        self.student = student
        self.teacher = teacher