class Person:
    name: str
    gender: int
    phone: str

    def __init__(self, name, gender, phone):
        super().__init__()
        self.name=name
        self.gender=gender
        self.phone=phone

    def outputPerson(self) -> str:
        result = "Ten: " + self.name + "\tGioi tinh: " + str(self.gender) + "\tSDT: " + self.phone
        return result
class Student(Person):
    studentid: str
    lop: str

    def __init__(self, name, gender, phone, studentid, lop) -> None:
        Person.__init__(self, name, gender, phone)
        self.studentid = studentid
        self.lop = lop

    def outputStudent(self) -> str:
        result = self.outputPerson() + "\n\tStudentID: " + self.studentid + "\tClass: " + self.lop
        return result
class Lecturer(Person):
    lecturerid: str
    yaersOfExperience: int

    def __init__(self, name, gender, phone, lecturerid, yearsOfExperience) -> None:
        Person.__init__(self, name, gender, phone)
        self.lecturerid = lecturerid
        self.yearsOfExperience = yearsOfExperience

    def outputLecturer(self) -> str:
        result = self.outputPerson() + "\n\tLectureID: " + self.lecturerid + "\tYears Of Experience: " + str(self.yearsOfExperience)
        return result