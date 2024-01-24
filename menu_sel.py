def get_menu():  # used to display a menu
    menu_dict = {
        '1': 'apples',
        '2': 'bananas',
        '3': 'cherries',
        '4': 'pears',
        'X': 'done_ordering'
    }
    return menu_dict

def display_menu(menu_dict):
    for item, value in menu_dict.items():
        print(item + ". " + value.replace('_', ' ').capitalize())

    menu_selection = input("What would you like to buy? ").upper()

    print("You selected {}".format(menu_dict.get(menu_selection, "Invalid selection")))
    return menu_selection

def display_purchases(items_list):
    print("You purchased {} items: {}".format(len(items_list), ", ".join(items_list)))

def main():
    menu_selection = ''
    items_list = []

    while menu_selection != 'X':
        menu_dict = get_menu()
        menu_selection = display_menu(menu_dict)

        if menu_selection != 'X':
            items_list.append(menu_dict.get(menu_selection, "Invalid selection"))

        input("Hit Enter to Continue!!")

    display_purchases(items_list)

if __name__ == "__main__":
    main()
