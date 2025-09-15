import pickle

FILE_PATH = 'week05_dictionaries_and_sets/object_serialization/'

dictionary_list = []

with open(FILE_PATH + 'unknown.bin', 'rb') as in_file:
    end_of_file = False

    while not end_of_file:
        try:
            dictionary_list.append(pickle.load(in_file))
        except EOFError as err:
            print('Reached the end of file.')
            end_of_file = True

print(dictionary_list)