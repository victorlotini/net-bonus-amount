# a program to give bonus to employee
year_of_service= int(input("enter year of service"))
salary= int(input("enter your salary"))
if (year_of_service>10):
    print(0.1*salary)
elif (year_of_service>= 6) and (year_of_service<=10):
    print(0.08*salary)
elif (year_of_service<6):
    print(0.05*salary)
else:
    print("not eligible for a bonus at the moment")