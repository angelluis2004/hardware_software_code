def menu_display():
    menu_dict = {
        '1': 'decimal_to_binary',
        '2': 'binary_to_decimal',
        'X': 'Exit_Program'
    }
    return menu_dict

def execute_display(menu_dict):
    for items, values in menu_dict.items():
        print("{}. {} ".format(items, values.capitalize()))
    menu_selection = list(menu_dict.keys())  # Use keys() instead of key()
    selection = "#"

    while selection not in menu_selection:
        selection = input("Enter: ")
        if selection not in menu_selection:
            print("Invalid entry!")
    return selection, menu_dict[selection]

def main():
    menu_dict = menu_display()  # Call menu_display() to get the dictionary
    sel, choice = execute_display(menu_dict)
    print("Hey, you selected '{}' and want to '{}'.".format(sel, choice))

if __name__ == "__main__":
    main()
                     
