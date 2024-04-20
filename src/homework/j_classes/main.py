from class_a import die
power = 1
dice = die()


def selectMenu(select):
    try:
        (int(select)==1 or int(select)==2)
        if int(select)==1:
            return(2)
        elif int(select)==2:
            return(3)
        else:
            print('Error: please enter one of the listed options')
            return(1)
    except:
        print('Error - Please enter one of the listed options.')
        return(1)

def quitMenu(select):
    try:
        if select.upper()=='Y' or select.upper()=='N' or select=='1' or select=='2':
            if(select=='1' or select.upper()=='Y'):
                return(0)
            elif(select=='2' or str(select).upper()=='N'):
                return(1)
            else:
                print('Error: an unexpected error occurred.')
                return(1)
        else:
            print('Error: please enter one of the listed options')
            return(1)
    except:
        print('Error: please enter one of the listed options')
        return(1)

while power == 1:
    print('')
    print('1 - Roll Dice')
    print('2 - Quit')
    print('________________')
    print('')
    select = input('')
    power = selectMenu(select)
    while power ==2:
        print('')
        dice.roll()
        print(dice)
        print('')
        print('Enter 1 to roll again, or press 2 to quit.')
        select = input('')
        power = selectMenu(select)
    
    while power == 3:
        print('')
        print('Would you really like to quit?')
        print('To confirm enter y, or 1. To return to the program, enter n or 2')
        print('')
        select = input('')
        power = quitMenu(select)
