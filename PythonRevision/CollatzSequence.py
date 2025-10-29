"""
Collatz Sequence Generator
--------------------------
This program is part of my Python revision projects.
It demonstrates recursion, basic error handling, and function calls.
"""
def main():
    """
    Main function:
    - Handles user input
    - Performs exception handling for invalid input
    """
    try:
        (collatz(int(input("Give Number For Collatz Sequence: "))))
    except ValueError:
        print("❌ Please Enter Valid Input")
def collatz(number: int) -> int:
    """
    Recursively prints the Collatz sequence starting from 'number'.

    The sequence follows these rules:
    - If number is even: next = number // 2
    - If number is odd: next = 3 * number + 1
    - Ends when number becomes 1
    """
    print(number)
    if number==1:
        return number
    elif  number%2==0:
        return collatz(number//2)
    else:
        return collatz(3*number+1)

# Standard python Practice

if __name__=="__main__":
    main()