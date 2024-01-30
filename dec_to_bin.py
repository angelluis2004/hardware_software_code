def binary_to_decimal(number):
    result = ""
    number = int(number)  # Convert input to integer
    while number > 0:       # Keep dividing until reaching 0
        remainder = number % 2
        number = number // 2
        result = str(remainder) + result  # Convert remainder to string before concatenating
    return result

def main():
    num = input("Enter Binary Number:")
    print("Number entered: {}, Binary: {}".format(num, binary_to_decimal(num)))

if __name__ == "__main__":
    main()
