def main():
    print("Enter a sequence of non-decreasing numbers.")
    seq = 0
    num1 = float(input("Enter num: "))
    num2 = float(input("Enter num: "))
    while num2 >= num1:
        num1 = num2
        seq = seq + 1
        num2 = float(input("Enter num: "))

    print("Thanks for playing!")
    print("Sequence length: "+str(seq+1))


if __name__ == "__main__":
    main()