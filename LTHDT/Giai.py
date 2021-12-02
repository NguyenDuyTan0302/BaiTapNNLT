from Bai3 import Person,Student,Professor
import pickle
def main():

  nguoi_list=[]
  hocsinh_list=[]
  thay_list=[]
  n=2
  for i in range(n):
    nguoi=Person(input(),input(),input())
    nguoi_list.append(nguoi)
    hocsinh=Student(input(),input(),input(),input(),input())
    thay=Professor(input(),input(),input(),input())
    hocsinh_list.append(hocsinh)
    thay_list.append(thay)
  for i in range(n):
    print(nguoi_list[i].outputPerson())
  for i in range(n):
    print(hocsinh_list[i].outputStudent())
  for i in range(n):
    print(thay_list[i].outputProfessor())
  for i in range(n):
    for j in range(i+1,n):
      if(nguoi_list[i].name>nguoi_list[j].name):
        nguoi_list[i],nguoi_list[j]=nguoi_list[j],nguoi_list[i]
      if(hocsinh_list[i].diemTB<hocsinh_list[j].diemTB):
        hocsinh_list[i],hocsinh_list[j]=hocsinh_list[j],hocsinh_list[i]
      if(thay_list[i].salary<thay_list[j].salary):
        thay_list[i],thay_list[j]=thay_list[j],thay_list[i]
  for i in range(n):
    print(nguoi_list[i].outputPerson())
  for i in range(n):
    print(hocsinh_list[i].outputStudent())
  for i in range(n):
    print(thay_list[i].outputProfessor())
  for i in range(n):
    str(hocsinh_list[i].diemTB)
    str(thay_list[i].salary)
  f1=open('nguoi.txt',"wb")
  pickle.dump(nguoi_list,f1)
  f1.close()
  f2=open('hocsinh.txt',"wb")
  pickle.dump(hocsinh_list,f2)
  f2.close()
  f3=open('thay.txt',"wb")
  pickle.dump(thay_list,f3)
  f3.close()
  f1=open('nguoi.txt','rb')
  x=pickle.load(f1)
  print(x)
  f1.close()
  f2=open('hocsinh.txt','rb')
  y=pickle.load(f2)
  print(y)
  f2.close()
  f3=open('thay.txt','rb')
  z=pickle.load(f3)
  print(z)
  f3.close()
if __name__=="__main__":
    main()
