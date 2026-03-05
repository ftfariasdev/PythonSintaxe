# Salary Increase Based on Position

import os
os.system("cls") # Clear the console (use "clear" for Unix/Linux/MacOS)
isContinue = "Y"

def calcSalary(percentIncrease, salary):
    return (salary * percentIncrease / 100) + salary

print("=" * 60)

print("Welcome to the Salary Increase Calculator!")

while isContinue != "N":

    print("=" * 60)

    salary = float(input("What is your salary? ")) # Convert input to float for numerical operations
    seniority = input("What is your position? (Junior, Mid, Senior) ").upper()
    newSalary = 0

    if(seniority == "JUNIOR"):
        newSalary = calcSalary(10, salary)
        newSalary += 200 if newSalary <= 1000 else newSalary
    elif(seniority == "MID"):
        newSalary = calcSalary(15, salary)
    elif(seniority == "SENIOR"):
        newSalary = calcSalary(20, salary)

        hasChildren = input("Do you have children? (Y/N) ").upper()

        if(hasChildren == "Y"):
            numberChildren = int(input("How Many you have children? "))
            newSalary = (numberChildren * 500) + newSalary

    else:
        print("Invalid Option")

    print(f"New Salary is ${newSalary:.2f}")
    isContinue = input("Do you want to calculate another salary increase? (Y/N) ").upper()
print("=" * 60)