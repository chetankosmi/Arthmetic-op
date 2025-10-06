num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform calculations
sum_result = num1 + num2
subtraction_result = num1 - num2

# Display results
print("Sum:", sum_result)
print("Subtraction:", subtraction_result)

multiplication_result = num1 * num2

if num2 != 0:
    division_result = num1 / num2
else:
    division_result = "Undefined (cannot divide by zero)"

#print output for multiplication and division
print("Multiplication:", multiplication_result)
print("Division:", division_result)