salary = float(input("What is your salary? ")) # Convert input to float for numerical operations
percentIncrase = float(input("What is the percentage increase? ")) # Convert input to float for numerical operations

newSalary = (salary * percentIncrase / 100) + salary

print(f"\nThe gross salary is {salary} with discount from {percentIncrase}% \n")
print(f"New Salary is {newSalary}")