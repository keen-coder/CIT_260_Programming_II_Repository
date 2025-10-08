from dog import Dog

def main():
    dog1 = Dog('Sparky', 'Chihuahua')
    dog2 = Dog('Annabelle', 'German Shephard')

    # NOTE: Objects should always be manipulated through their public
    # methods!
    # Display information for dog1
    print('Dog 1 Info w/ Methods:')
    print(f'\t{dog1.get_name()}')
    print(f'\t{dog1.get_breed()}')

    # Display information for dog2
    print('Dog 2 Info w/ Methods:')
    print(f'\t{dog2.get_name()}')
    print(f'\t{dog2.get_breed()}')

    # Change the information for dog 2 and display both objects again
    dog2.set_name('Fido')
    dog2.set_breed('Greyhound')

    print('Dog 1 Info w/ Methods:')
    print(f'\t{dog1.get_name()}')
    print(f'\t{dog1.get_breed()}')

    # Display information for dog2
    print('Dog 2 Info w/ Methods:')
    print(f'\t{dog2.get_name()}')
    print(f'\t{dog2.get_breed()}')

    # The following shows how to access the internal data through the
    # public data fields
    # THIS IS BAD BAD BAD DESIGN
    print(dog1.name)
    print(dog1.breed)

    dog2.name = 'Some Name'
    dog2.breed = 'Some Breed'

if __name__ == '__main__':
    main()