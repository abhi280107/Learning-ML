
def main():
    try:
        (collatz(int(input("Give Number For Collatz Sequence: "))))
    except ValueError:
        print("Please Enter Valid Input")
def collatz(number):
    print(number)

    if number==1:
        return number
    elif  number%2==0:
        return collatz(number//2)
    else:
        return collatz(3*number+1)

main()