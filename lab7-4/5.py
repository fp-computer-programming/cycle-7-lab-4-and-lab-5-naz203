"""
Create a Python file named lab_7-4.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Copy your lab 7-2 code into the file
Add 4 test cases to the end of the file, with comments
Ensure your lab runs accurately




________________________________________________________________________________

Create a Python file named lab_7-5.py


Copy the code from your labs 6-5 through 6-8
Turn each of the programs into a function
Add 4 test cases to the functions
Ensure your code runs accurately


"""
num1 = int
num2 = int
num3 = int
num_list = []
def double_input_values ():
    num1 = int(input ("Enter number 1: "))
    num2 = int(input ("Enter number 2: "))
    num3 = int(input ("Enter number 3: "))
    num_list.append(num1)
    num_list.append(num2)
    num_list.append(num3)
    return num_list
                 
double_input_values()

print(num_list)

doubled_list = [num * 2 for num in num_list] 
print (doubled_list)
double_input_values()
# Test Case 1
result_1 = double_input_values () == [2, 4, 6]
# Test Case 2
result_2 = double_input_values () == [-2, -4, -6]
# Test Case 3
result_3 = double_input_values () == [0, 0, 0]
# Test Case 4
result_4 = double_input_values () == [20, 40, 60]
