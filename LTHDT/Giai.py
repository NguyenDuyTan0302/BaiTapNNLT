from Bai3 import Person,Student,Professor
def main():
  import pickle
  nguoi_list=[]
  hocsinh_list=[]
  thay_list=[]
  n=2
  for i in range(n):
    nguoi=Person(str(input()),str(input()),str(input()))
    nguoi_list.append(nguoi)
    hocsinh=Student(str(input()),str(input()),str(input()),str(input()),input())
    thay=Professor(str(input()),str(input()),str(input()),input())
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
        nguoi_list[i].name,nguoi_list[j].name=nguoi_list[j].name,nguoi_list[i].name
      if(hocsinh_list[i].diemTB<hocsinh_list[j].diemTB):
        hocsinh_list[i].diemTB,hocsinh_list[j].diemTB=hocsinh_list[j].diemTB,hocsinh_list[i].diemTB
      if(thay_list[i].salary<thay_list[j].salary):
        thay_list[i].salary,thay_list[j].salary=thay_list[j].salary,thay_list[i].salary
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
  with open('nguoi.txt','r',errors='ignore') as f1:
    x=f1.read()
  f1.close()
  print(x)
  with open('hocsinh.txt','r',errors='ignore') as f2:
    y=f2.read()
  f2.close()
  print(y)
  with open('thay.txt','r',errors='ignore') as f3:
    z=f3.read()
  f3.close()
  print(z)
if __name__=="__main__":
    main()
