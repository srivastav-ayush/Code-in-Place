def main():
    x = input('Enter a string: ')
    rev = reversed(x)
    print(x + ' backwards is ' + rev)

def reversed(str):
    '''
    Takes a string and returns a reversed copy
    >>> reversed('stressed')
    'desserts'
    >>> reversed('hello')
    'olleh'
    '''
    rev = ''
    for ch in str:
        rev = ch + rev
    return rev

if __name__ == '__main__':
    main()