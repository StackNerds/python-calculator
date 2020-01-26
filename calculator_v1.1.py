
def add(first_number, second_number):
    return first_number + second_number

def substract(first_number, second_number):
    return first_number - second_number

def multiply(first_number, second_number):
    product = 0
    for i in range(first_number):
        product = product + second_number
    return product

def divide(first_number, second_number):
    quotient = 0
    while first_number >= second_number:
        first_number = first_number - second_number
        quotient = quotient + 1
    return quotient

operations_map = {
    1: add,
    2: substract,
    3: multiply,
    4: divide
}


print("Hello, enter operation number to carry out operation\n"\
      "Enter 1 for addition\n" \
      "Enter 2 for substraction\n" \
      "Enter 3 for multiplication\n" \
      "Enter 4 for division\n")


operation = int(input("Select operation waiting .... :"))
first_number = int(input("Enter first number :"))
second_number = int(input("Enter second number :"))

print(operations_map[operation](first_number, second_number))


 

