import dictionary
inventory_dictionary={}

on = True
while on:
    print('')
    print('1 - Add or Update Item')
    print('2 - Delete Item')
    print('3 - Exit')
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
        exitMenu = True
        while exitMenu == True:
            print('')
            confirmation = (input('Are you sure you would like to quit? y/n: ').upper())
            if confirmation == 'Y' or confirmation == 'YES':
                on = False
                exitMenu = False
            elif confirmation == 'N' or confirmation =='NO':
                exitMenu = False