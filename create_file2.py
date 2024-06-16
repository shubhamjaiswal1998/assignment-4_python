'''
reate a file named Input.txt. Enter some positive numbers into the file named Input.txt. 
Read the contents of the file, if a number is odd, write it to ODD.txt; if it is even,
 write it to EVEN.txt. 
'''
def f1():
    with open("goel2.txt","w") as ob1:
        ob1.write("2\n3\n4\n5\n6\n7\n8\n9\n")
    with open("goel.txt","r") as ob1:
        content=ob1.read().split()
        print(content)#['2', '3', '4', '5', '6', '7', '8', '9']
        print(type(content))#<class 'list'>
    odd_list=[]
    even_list=[]
    for i in content:
        i2=int(i)
        if i2%2==0:
            even_list.append(i2)
        else:
            odd_list.append(i2)
                
    print(odd_list)#[3, 5, 7, 9]
    print(even_list)#[2, 4, 6, 8]
f1()

'''
Explain Exceptions and Assertions in Python with a suitable example. Explain
any two built-in exceptions.
'''    
def calculate_average(numbers):
    assert len(numbers) > 0, "List must not be empty"
    return sum(numbers) / len(numbers)
    numbers = [10, 20, 30]
    print(calculate_average(numbers))  # Output: 20.0
empty_list = []
print(calculate_average(empty_list))  # AssertionError: List must not be empty


           

