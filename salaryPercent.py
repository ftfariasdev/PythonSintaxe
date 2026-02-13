# Salary Percent Calculator
import os

os.system("cls") # Clear the console (use "clear" for Unix/Linux/MacOS)

print("=" * 60)

salary = float(input("What is your salary? ")) # Convert input to float for numerical operations
percentIncrase = float(input("What is the percentage increase? ")) # Convert input to float for numerical operations

newSalary = (salary * percentIncrase / 100) + salary # Calculate the new salary by applying the percentage increase to the original salary

print("-" * 60)

print(f"The gross salary is ${salary:.2f} with discount from {percentIncrase:.2f}%")
print(f"New Salary is ${newSalary:.2f}")

print("=" * 60)