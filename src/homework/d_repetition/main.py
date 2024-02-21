import repetition
menu = True
while menu:
    print("HOMEWORK 3 MENU")
    print("1 - FACTORIAL")
    print("2 - SUM ODD NUMBERS")
    print("3 - EXIT")
    menuSelect = int((input ('')))
    if menuSelect == 1:
        on = True
        while on:
            factorialNum = int((input("ENTER A NUMBER BETWEEN 1 AND 10: ")))
            if 0 <= factorialNum <= 10:
                returnedFactorial = repetition.get_factorial(factorialNum)
                print('     '+str(returnedFactorial) +' IS THE FACTORIAL OF '+str(factorialNum))
                print('')
                userExitQuery = input('Do you want to exit? y/n: ')
                if userExitQuery =='yes' or userExitQuery =='y':
                    menu=False
                on = False
    
    elif menuSelect == 2:
        on = True
        while on:
            sumOddNumInput = int((input("ENTER A NUMBER BETWEEN 1 AND 100: ")))
            if 0 <= sumOddNumInput <= 100:
                returnedSum = repetition.sum_odd_numbers(sumOddNumInput)
                print('THE SUM OF ODD NUMBERS UP TO '+str(sumOddNumInput)+' IS: '+str(returnedSum))
                print('')
                userExitQuery = input('Do you want to exit? y/n: ')
                if userExitQuery =='yes' or userExitQuery =='y':
                    menu=False
                on = False
    
    elif menuSelect == 3:
        on = True
        while on:
            confirmation = input('Are you sure? y/n: ')
            if confirmation == 'y' or confirmation == 'yes':
                menu = False
            on = False

    else:
        print('')
        print('ERROR. ENTER THE NUMBER OF YOUR SELECTION.')
        print('')