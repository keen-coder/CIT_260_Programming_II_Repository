# When working with File I/O, it is a good idea to use Exception Handling to deal with any
# file not found errors


def main():
    filename = input('Enter a filename: ')
    try:
        with open(filename, 'r') as infile:
            contents = infile.read()
            print(contents)
    except FileNotFoundError:
        print(f'The file {filename} does not exist.')

if __name__ == '__main__':
    main()