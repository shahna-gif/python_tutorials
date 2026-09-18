Name = input("Enter your name:")
print("Welcome", Name)
Age = input("Enter your Age:")
print("Yoe are", Age ,"year old")
City = input("Enter your place:")
print(f"My Name is {Name}. I'm {Age} old.I'm from {City}" )
Number1 = float(input("Enter first number:"))
Number2 = float(input("Enter second number:"))
print("Sum:",Number1 + Number2)
print("Difference:",Number1 - Number2)
print("Product:",Number1 * Number2)
print("Division:",Number1 / Number2)
#Rectangle
Length = float(input("Enter the length of the Rectangle:"))
Width = float(input("Enter the width of the Rectangle:"))
print("Area of the Rectangle:",Length*Width)
print("Perimeter of the Rectangle:",2*Length+Width)
#Square
side = float(input("Enter the side of the Square:"))
print("Area of the square:",side*side)
print("Perimeter of the square:",4*side)
#Circle
Radius = float(input("Enter the radius of the Circle:"))
print("Area of the Circle:",3.14*Radius**2)
#Temperature
Celsius = float(input("Enter temperature in celsius:"))
Fahrenheit = ( Celsius *9/5 ) + 32
print("Temperature in Fahrenheit:",Fahrenheit)
Fahrenheit = float(input("Enter temperature in Fahrenheit:"))
Celsius = (Fahrenheit - 32) * 5/9
print("Temperature in Celsius:",Celsius)
#Age Calculation
Birth_Year = int(input("Enter your Date of Birth:"))
Current_Year = 2026
Age = Current_Year - Birth_Year
print("Your approximate age is:",Age)
#Days
Days = int(input("Enter number of days:"))
Weeks = Days // 7
Remaining_Days = Days % 7
print("Weeks:",Weeks, "Remaining_Days:", Remaining_Days)
#Time
Seconds = int(input("Enter number of Seconds:"))
Minutes = Seconds // 60
Remaining_Seconds = Seconds % 60
print("Minutes:", Minutes,"Remaining_Seconds:",Remaining_Seconds)
#Amount
Amount = float(input("Enter amount in rupees:"))
Discount_percent = float(input("Enter discount in percentage:"))
Discount_amount = ( Amount * Discount_percent) / 100
Final_Price = Amount - Discount_amount
print("Discount amount:", Discount_amount)
print("Final price:",Final_Price)
#Bill
Price = int(input("Enter the price of product:"))
Quantity = int(input("Enter quantity of product:"))
Total_Bill = Price * Quantity
print("Total Bill:",Total_Bill )
Total_Bill = int(input("Enter  total bill Amount:"))
Number_of_people = int(input("Enter  number of people:"))
Share = Total_Bill / Number_of_people
print("Each person should pay:",Share)
#Salary
Salary = int(input("Enter the basic salary:"))
HRA = 0.20 * Salary
DA = 0.10 * Salary
Gross_salary = Salary + HRA + DA
print("HRA:", HRA )
print("DA:",DA)
print("Gross salary:",Gross_salary)
#Interest
Pricipal = float(input("Enter the pricipal:"))
Rate_of_interest = float(input("Enter the rate of interest:"))
Time =float(input("Enter the time (in years):"))
Simple_interest = (Pricipal*Rate_of_interest*Time)/100 
print("simple interest:",Simple_interest)
#Mark
Mark1 = float(input("Enter the mark of subject1:"))
Mark2 = float(input("Enter the mark of subject2:"))
Mark3 = float(input("Enter the mark of subject3:"))
Mark4 = float(input("Enter the mark of subject4:"))
Mark5 = float(input("Enter the mark of subject5:"))
Total_Marks = Mark1 + Mark2 + Mark3 + Mark4 + Mark5 
print("Total mark:",Total_Marks)
Average =  (Mark1 + Mark2 + Mark3 + Mark4 + Mark5)/5
print("Average:",Average)
#Square and Cube
Num = float(input("Enter a number:"))
Square = Num ** 2
Cube = Num ** 3
print("Square:",Square)
print("Cube:",Cube)