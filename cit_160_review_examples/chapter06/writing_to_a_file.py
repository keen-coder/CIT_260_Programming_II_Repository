# Use the open function to open a file and the 'w' to indicate you will open it in write mode.
# If the file does not exist, the file will be created. If it does exist the old data in the file
# will be overwritten (the old data is destroyed and replaced with the new data.)

# NOTE: All file i/o is relative to your workspace folder.

def main():
    # open the file in write mode
    # Note the relative path used here.  This will put the output file in the chapter06 package
    output_file = open('cit_160_review_examples/chapter06/my_data.txt', 'w')

    for x in range(0, 100):
        # NOTE: the data to write to the file must be converted to a string.
        output_file.write(str(x)+'\n')

    output_file.close()    

if __name__ == '__main__':
    main()