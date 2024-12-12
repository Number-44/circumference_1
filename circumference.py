base=input("enter the base amount and press enter : ")
height = input("enter the height and press enter : ")


[print(_ * "<=>") for _ in range (5)]



try:
    base=int(base)
    height=int(height)
    print("the base amount is : "+ str(base))
    print("the amount of height is : "+ str(height))
    print("the circomference of the " +str(2*(base * height)))



except ValueError:
    print("the amount is not acceptable !  enter a digit !")
