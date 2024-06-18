'''
2. Control Structures
Question 2: Number Analysis
Ask the user for a number.
Use an if statement to determine if the number is even or odd. Use a for 
loop to print all even numbers up to the user's number. Use a while loop to 
sum the digits of the number.
File Name: number_analysis.py
'''
num=int(input("Enter the number: "))
num=num%2
if num==0:
    
    print("this is even number")
else:
    print("this is odd number")
