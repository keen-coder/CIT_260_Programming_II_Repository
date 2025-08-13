def main():
    # open the file in read mode using the 'r' argument
    input_file = open('cit_160_review_examples/chapter06/my_data.txt', 'r')
   
    file_data = input_file.read()

    print(file_data)

if __name__ == '__main__':
    main()