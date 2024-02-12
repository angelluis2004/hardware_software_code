def binary_to_decimal(binary):
    "Function to convert binary to decimal."
    decimal = 0
    power = 0
    for digit in binary[::-1]:
        decimal += int(digit) * (2 ** power)
        power += 1
    return decimal

def decimal_to_binary(decimal):
    "Function to convert decimal to binary."
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

def display_menu():
    "Function to display the menu."
    print("Conversion Calculator Menu:")
    print("1. Binary to Decimal")
    print("2. Decimal to Binary")
    print("3. Hexadecimal to Decimal")
    print("4. Decimal to Hexadecimal")
    print("5. Hexadecimal to Binary")
    print("6. Binary to Hexadecimal")
    print("7. Octal to Decimal")
    print("8. Decimal to Octal")
    print("9. Quit")

def main():
    "Main function to run the program."
    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            binary = input("Enter a binary number: ")
            if all(bit in '0123456789' for bit in binary):
                decimal = binary_to_decimal(binary)
                print(f"The decimal equivalent of {binary} is {decimal}.")
            else:
                print("Invalid binary number. Please enter a binary number (containing only digits).")

        elif choice == '2':
            decimal = int(input("Enter a decimal number: "))
            binary = decimal_to_binary(decimal)
            print(f"The binary equivalent of {decimal} is {binary}.")

        elif choice == '9':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please choose a number from the menu.")

if __name__ == "__main__":
    main()
