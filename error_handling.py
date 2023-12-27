def sum(num1, num2):
    while True:
        try:
            return num1+num2
        # Also you can do raise your won error as
        #raise ValueError("The message to print")
        #the above is used when you want to raise your won
        #custom error.
        except  TypeError as err:
            print("You have made a mistake!", err)
        else:
        #or we can do it as below
        #except (Type error, division error or so...) as err:
        #    print(err)
        #It will get the error raised and then print it
            print("I run if no error or no break")
            print("I also can not come right after try")
        finally:
            print("I run no matter what")
            break
        
sum(1,2)