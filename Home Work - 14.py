try:
    num1 = str(input("Enter first letter: "))
    num2 = str(input("Enter second letter: "))
except ValueError:
    print("Please enter valid letters.")
except:
    print("Wrong input.")    
else:
    print("No exceptions.") 
finally:
    print("This will execute no matter what.")
                   