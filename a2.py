try:
    n1=int(input("Enter first number:"))
    n2=int(input("Enter second number:"))
    result=n1/n2
    print("Result is",result)

except ZeroDivisionError:
    print("Division by zero is not allowed")

except ValueError:
    print("Invalid input. Please enter a number")

except NameError as e:
    print("NameError is:", e)

finally:
    print("Project is created by MR.Abdul Malik")

