#1. taking inputs and calculate circumference Of Rectangle 


base=input("enter the base amount and press enter !")
height=input("enter the height amount and press enter !" )
print("length of height :"+str(int(height)))
print("length of base :"+str(int(base)))
print("the circumference is : "+str((int(base)*int(height))))


#2. as a function

def circunference(base,height):
  print("length of height :" + str(int(height)))
  print("length of base :" + str(int(base)))
  print("the circumference is : " + str((int(base) * int(height))))

circunference(3,4)