try: 
    num1, num2 = eval(input("Enter two inputs seperated by a coma: "))
    Div = num1 / num2

except SyntaxError: 
    print("Comma Missing")

except ZeroDivisionError: 
    print("Cannot Divide By 0")

except:
    print("Wrong Input")

else: 
    print("No Exceptions")

finally: 
    print("This line will be excecuted")
