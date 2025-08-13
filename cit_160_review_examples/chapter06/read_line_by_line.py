

def read_four_lines():
    input_file = open('cit_160_review_examples/chapter06/stopping_by_the_woods.txt', 'r')

    for line_number in range(1, 5):
        next_line: str = input_file.readline()
        print(next_line)
    

def read_all_lines():
    input_file = open('cit_160_review_examples/chapter06/stopping_by_the_woods.txt', 'r')

    for next_line in input_file:
        print(next_line)   


def main():
    # read the first four lines
    read_four_lines()

    print()
    print()

    read_all_lines()
   

if __name__ == '__main__':
    main()