inventory_dictionary = {}

def add_inventory(type_dictionary,widget_name,quantity):
    if not widget_name in type_dictionary:
        type_dictionary.update({str(widget_name):{'quantity':quantity}})
        return('widget added.')
    else:
        type_dictionary[str(widget_name)]['quantity']+=quantity
        return('widget updated')

def remove_inventory_widget(type_dictionary,widget_name):
    if not widget_name in type_dictionary:
        return('Item not found.')
    else:
        type_dictionary.pop(str(widget_name))
        return('Deletion successful.')
