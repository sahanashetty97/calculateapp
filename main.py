from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide

def main():
    # Example usage of functions
    result_add = add(5, 3)
    result_subtract = subtract(10, 4)
    result_multiply = multiply(2, 7)
    result_divide = divide(20, 5)

    print("Result of addition:", result_add)
    print("Result of subtraction:", result_subtract)
    print("Result of multiplication:", result_multiply)
    print("Result of division:", result_divide)

if __name__ == "__main__":
    main()
