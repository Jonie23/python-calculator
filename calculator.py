#welcome user
def welcome():
    print('''
    Welcome to Jones's calculator built with python
    ''')

welcome()
# calculator()


#define a function to run program many times
def calculator():
    #ask what operation user will want to run
    operation = input('''
Please type in the calculator operation you will want to run
+ for addition
-  for subtraction
*  for multiplication
/  for division
** for exponent
%  for modulus
''')


    #prompt user for inputs
    #And convert input to float data type to take floats(decimals)

    first_number = float(input('Enter the first number: '))
    second_number = float(input('Enter the second number: '))



    #Addition Operators
    if operation == '+' :
        print(' {} + {} = '.format(first_number, second_number)) #use string format to provide more feedback
        print(first_number + second_number)

     #Subtraction Operator
    elif operation == '-' :
        print(' {} - {} = '.format(first_number, second_number))
        print(first_number - second_number)


    #Multiplication Operator
    elif operation == '*' :
        print(' {} * {} = '.format(first_number, second_number))
        print(first_number * second_number)

    #Division
    elif operation == '/' :
        print(' {} / {} = '.format(first_number, second_number))
        print(first_number / second_number)

    elif operation == '**':
        print(' {} / {} = '.format(first_number, second_number))
        print(first_number ** second_number)

    elif operation == '%':
        print(' {} / {} ='.format(first_number, second_number))
        print(first_number % second_number)

    else:
        print('Please type a valid operator and run again.')
    
    repeat()





    #function to repeat calculator
def repeat(): 
    repeat_calc = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')
    if repeat_calc.upper() == 'Y':
        calculator()

    elif repeat_calc.upper() == 'N':
        print('Alright. Hope to see you another time')

    else:
        repeat()
    


#Call calculator
calculator()
     








