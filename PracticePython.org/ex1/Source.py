import datetime
date=datetime.datetime.now()
name=input("Enter name: ")
age=int(input("Enter your age: "))
multiply=int(input("Enter number for multiplication: "))
print(multiply * (name + " will turn 100 in " + str(date.year-age+100) + "\n"))
