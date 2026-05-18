try: 
    num = int(input("Enter Number: "))
    print("The value is", num)

except ValueError as ex: 
    print("Exception", ex)
