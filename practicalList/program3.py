#Write a program in python to implement conditional statements.	
    #WAP in python to make a calculator.	
print()
print("---Welcome in Calculator program!---")
    
def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
  
    if operation in ('+','-','*','/'):
         number_1 = int(input('Please enter the first number: '))
         number_2 = int(input('Please enter the second number: '))

         if operation == '+':
            print('{} + {} = '.format(number_1, number_2))
            print(number_1 + number_2)
            
         elif operation == '-':
            print('{} - {} = '.format(number_1, number_2))
            print(number_1 - number_2)
            
         elif operation == '*':
            print('{} * {} = '.format(number_1, number_2))
            print(number_1 * number_2)

         elif operation == '/':
            print('{} / {} = '.format(number_1, number_2))
            print(number_1 / number_2)   

    else:
        print('You have not typed a valid operator, please enter a valid choice.')

    # again() function allows to calculate again
    again()

def again():
    calc_again = input('''
                        Do you want to calculate again?
                        Please type Y for YES or N for NO.
                        ''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Goodbye!Thanks for using our program.')
    else:
        again()

calculate()
