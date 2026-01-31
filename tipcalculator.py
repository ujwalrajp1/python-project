print("Welcome to the tip calculator")
bill = float(input("enter the amount of the bill received : "))
tip = int(input("how much tip do you want to give in percentage : "))
splitbill = int(input("entern the number of members you wanna split the bill : "))
calculate_tip = (bill * (tip/100))
totalamt = bill + calculate_tip
splited = round((totalamt / splitbill),2)
print(f"the amount that should be paid by every single person is {splited} and the total amount of the bill after adding tip is {totalamt}")
