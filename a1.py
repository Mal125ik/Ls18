try:
    n=int(input("Enter any number "))
    print("Number is:",n)

except ValueError as e:
    print("Exeption is:",e)

print("End of program")