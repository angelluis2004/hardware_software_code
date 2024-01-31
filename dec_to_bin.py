def binary_to_decimal(number):
    result = ""
    number = int(number)  # Convert input to integer
    while number > 0:       # Keep dividing until reaching 0
        remainder = number % 2
        number = number // 2
        result = str(remainder) + result  # Convert remainder to string before concatenating
    return result

def is_binary(number):
    return all(bit in '01' for bit in number)  # Check if all characters are '0' or '1'

def main():
    num = input("Enter Binary Number:")
    if is_binary(num):
        print("Decimal: {}, Binary: {}".format(binary_to_decimal(num), num))
    else:
        print("Invalid input. Please enter a binary number consisting of '0' and '1'.")

if __name__ == "__main__":
    main()
