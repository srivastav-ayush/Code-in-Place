def main():
    raw_string = input('Enter a string: ')
    num_string = just_number(raw_string)
    print(num_string)

def just_number(str):
    '''
    Takes a string and returns a reversed copy
    >>> just_number('My phone number is 6508675309. Please call!')
    '6508675309'
    >>> just_number('abc123def456')
    '123456'
    '''
    return ''

if __name__ == '__main__':
    main()