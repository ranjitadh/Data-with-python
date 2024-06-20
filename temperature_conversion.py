'''3. Functions
Question 3: Temperature Conversion
Write a function convert_to_fahrenheit that takes a temperature in Celsius and returns it in Fahrenheit.
Write a function convert_to_celsius that takes a temperature in Fahrenheit and returns it in Celsius.
    Create a script to test these functions with various temperatures.
File Name: temperature_conversion.py'''

# Define the function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Define the function to convert Fahrenheit to Celsius


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    while True:
        choice = input("CHOOSE THE MENU:\n 1. c-f (Celsius to Fahrenheit) \n 2. f-c (Fahrenheit to Celsius)\n")
        
        if choice == "1":
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = convert_to_fahrenheit(celsius)
            print(f"{celsius}°C = {fahrenheit}°F")
        elif choice == "2":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = convert_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F = {celsius}°C")
        else:
            print("Please enter a valid number 1 or 2")
      

main()


                    
                     