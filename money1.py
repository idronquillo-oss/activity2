n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
# these are the global variables

def calculate_sum():
    # sum is local variable
    sum = n1 + n2
    print(f"Sum: {sum}")
def calculate_difference():
    # sum is local variable
    difference = n1 - n2
    print(f"Difference: {difference}")

calculate_sum()
calculate_difference()









































