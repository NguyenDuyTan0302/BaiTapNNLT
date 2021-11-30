from Nguoi import Person,Student,Lecturer
def main():
    tan=Student("Nguyễn Duy Tân",1,"0815316393","614510320","Năm 1")
    thaycuong=Lecturer("Nguyễn Đình Hoa Cương",1,"0321646198","6481348548",10)
    print(tan.outputStudent())
    print(thaycuong.outputLecturer())
if __name__=="__main__":
    main()