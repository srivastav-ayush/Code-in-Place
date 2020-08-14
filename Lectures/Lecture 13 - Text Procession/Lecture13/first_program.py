def main():
    example = "Hi mom😊"

    # example of length function
    length = len(example)
    print(length)  # prints 6

    # example of getCharAt
    first = example[0]
    print(first)  # prints 'H'

    # loop that prints letters one-by-one
    for i in range(len(example)):
        ch = example[i]
        print(i, ch)


if __name__ == '__main__':
    main()