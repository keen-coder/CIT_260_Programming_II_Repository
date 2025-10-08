from dog import Dog

def main():
    default_dog = Dog()
    dog_w_name = Dog('Sparky')
    # NOTE: If you aren't passing the data in order
    # you have to specify the name of the attribute
    dog_w_breed = Dog(breed='Golden Retriever')

    print(f'default_dog: {default_dog.get_name()}, {default_dog.get_breed()}')
    print(f'dog_w_name: {dog_w_name.get_name()}, {dog_w_name.get_breed()}')
    print(f'dog_w_breed: {dog_w_breed.get_name()}, {dog_w_breed.get_breed()}')


if __name__ == '__main__':
    main()