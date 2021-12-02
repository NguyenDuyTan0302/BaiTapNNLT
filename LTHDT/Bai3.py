class Person:
    name: str
    phone: str
    email:str

    def __init__(self, name, phone, email):
        super().__init__()
        self.name=name
        self.phone=phone
        self.email=email

    def outputPerson(self) -> str:
        result = "Ten: " + self.name  + "\tSDT: " + self.phone + "\tEmail: " + self.email
        return result
class Student(Person):
    studentid: str
    diemTB: float

    def __init__(self, name, phone, email, studentid, diemTB) -> None:
        Person.__init__(self, name, phone, email)
        self.studentid = studentid
        self.diemTB=diemTB

    def outputStudent(self) -> str:
        result = self.outputPerson() + "\n\tStudentID: " + self.studentid + "\tDiem TB: " + str(self.diemTB)
        return result
class Professor(Person):
    salary: int

    def __init__(self, name, phone, email,salary) -> None:
        Person.__init__(self, name, phone, email)
        self.salary=salary

    def outputProfessor(self) -> str:
        result = self.outputPerson() + "\n\tSalary: " + str(self.salary)
        return result