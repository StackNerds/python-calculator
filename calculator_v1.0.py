
def add(first_number, second_number):
    return first_number + second_number

def substract(first_number, second_number):
    return first_number - second_number

def multiply(first_number, second_number):
    return first_number * second_number
    

def divide(first_number, second_number):
    return first_number/second_number

operations_map = {
    1: add,
    2: substract,
    3: multiply,
    4: divide
}


print("Hell enter operation number to carry out operation\n"\
      "Enter 1 for addition\n" \
      "Enter 2 for substraction\n" \
      "Enter 3 for multiplication\n" \
      "Enter 4 for division\n")


operation = int(input("Select operation waiting .... :"))
first_number = int(input("Enter first number :"))
second_number = int(input("Enter second number :"))

print(operations_map[operation](first_number, second_number))


 

