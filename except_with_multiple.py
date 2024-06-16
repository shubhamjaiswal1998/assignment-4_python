
def process_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(content)
            # Intentionally raising an exception for demonstration purposes
            user_input=int(input("enter a number"))
            result = 10 /user_input  # This might raise ValueError or ZeroDivisionError
            print("result of division is ",result)
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
    except Exception as e:  # Catching any other exceptions
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File processing completed.")

process_file("goel.txt") 

#m-2
def exception_process():
    try:
        j=int(input("enter user input"))
        res=5/j
        print("division is ",res)

        list1=[1,2,3,4]
        size=int(input("enter a size "))
        print()
        print(list1[size])

        input_value=input("enter a user input")
        res1="5"+input_value
        #res1= 5 +input_value , this line can give error
        print(res1)

    except ZeroDivisionError as e:
        print(e)#will print only error name
        print(e.with_traceback())   #will print all track
    except IndexError as e:
        print(e)  
    except Exception as e:
        print(e)      
    finally:print("it have completed sucessfully ")

exception_process()         