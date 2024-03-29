def check_selection(numbers):
    # Verify if it is a hexadecimal
    hex_list = ["A", "B", "C", "D", "E", "F", "0", "1",
                "2", "3" ,"4" ,"5", "6", "7", "8", "9"]
    for number in numbers:
        if number.upper() not in hex_list:
            print("Not a hexadecimal number. Try again.")
            return False  # Return False if any character is not a valid hexadecimal digit
    return True  # Return True only if all characters are valid hexadecimal digits

def main():
    good_selection = False
    while not good_selection:
        selection = input("Provide a hexadecimal number:")
        good_selection = check_selection(selection)
    print("Nice Job Angel!", selection, "This is a hexadecimal number!")

if __name__ == "__main__":
    main()
