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
#ryan rinvil (author)
def find_sum(num1,num2):
    """

    this functaion takes two numbers as input and returns their sum.
    """
    num_sum = num1 + num2
    return num_sum 

my_sum = find_sum(-10,-5)
print(my_sum)
"when the program is run, it will calculate the sum of 111 and 222, store it in my_sum, and then print the valm"

#test case 1
result_1 = find_sum(5,7)
#test case 2 
result_2 = find_sum(-3,8)
#test case 3
result_3 = find_sum(0,0)
#test case 4
result_4 = find_sum(-10,-5)
print("all test cases passed successfully")



#lab7-5

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
