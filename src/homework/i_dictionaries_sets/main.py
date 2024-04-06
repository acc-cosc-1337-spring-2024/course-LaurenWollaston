import dictionary, sets
# from sets import prog1Set, prog2Set
inventory_dictionary={}

on = True
while on:
    print('')
    print('1 - Add or Update Item')
    print('2 - Delete Item')
    print('3 - Students who took prog1 and prog2')
    print('4 - Students who took prog1 or prog2')
    print('5 - Students who took prog1 not prog2')
    print('6 - Students who took prog2 not prog1')
    print('7 - Exit')
    print('')
    print('Inventory: '+str(inventory_dictionary))
    print('')
    select = int(input(''))
    if select == 1:
        updateMenu = True
        while updateMenu == True:
            print('')
            widget_name = input('Enter the widget name: ')
            print('')
            updateMenu_layer2 = True
            while updateMenu_layer2 == True:
                quantity = input('Enter the quantity: ')
                print('')
                try:
                    quantity = int(quantity)
                    print(dictionary.add_inventory(inventory_dictionary,widget_name,quantity))
                    print('')
                    updateMenu = False
                    updateMenu_layer2 = False
                except:
                    print('Error: Quantity should be an integer.')
                    print('')
    elif select == 2:
        deleteMenu = True
        while deleteMenu ==True:
            print('')
            widget_name = input('Enter the widget name: ')
            print('')
            print(dictionary.remove_inventory_widget(inventory_dictionary,widget_name))
            deleteMenu = False
    elif select == 3:
        setsMenu = True
        while setsMenu == True:
            print('')
            print(sets.get_students_who_took_prog1_and_prog2(sets.prog1Set, sets.prog2Set))
            print('')
            returnConfirmation = input('press 0 to return to the main menu. ')
            try:
                if returnConfirmation == '0' or returnConfirmation.upper() == ('OK'):
                    setsMenu = False
            except:
                print('invalid option')
    elif select == 4:
        setsMenu = True
        while setsMenu == True:
            print('')
            print(sets.get_students_who_took_prog1_or_prog2(sets.prog1Set, sets.prog2Set))
            print('')
            returnConfirmation = input('press 0 to return to the main menu. ')
            try:
                if returnConfirmation == '0' or returnConfirmation.upper() == ('OK'):
                    setsMenu = False
            except:
                print('invalid option')
    elif select == 5:
        setsMenu = True
        while setsMenu == True:
            print('')
            print(sets.get_students_who_took_prog1_not_prog_2(sets.prog1Set, sets.prog2Set))
            print('')
            returnConfirmation = input('press 0 to return to the main menu. ')
            try:
                if returnConfirmation == '0' or returnConfirmation.upper() == ('OK'):
                    setsMenu = False
            except:
                print('invalid option')
    elif select == 6:
        setsMenu = True
        while setsMenu == True:
            print('')
            print(sets.get_students_who_took_prog2_not_prog_1(sets.prog1Set, sets.prog2Set))
            print('')
            returnConfirmation = input('press 0 to return to the main menu. ')
            try:
                if returnConfirmation == '0' or returnConfirmation.upper() == ('OK'):
                    setsMenu = False
            except:
                print('invalid option')
    elif select == 7:
        exitMenu = True
        while exitMenu == True:
            print('')
            confirmation = (input('Are you sure you would like to quit? y/n: ').upper())
            if confirmation == 'Y' or confirmation == 'YES':
                on = False
                exitMenu = False
            elif confirmation == 'N' or confirmation =='NO':
                exitMenu = False