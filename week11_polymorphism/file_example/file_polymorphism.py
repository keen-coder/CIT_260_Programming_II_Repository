# I know I always say to put your classes in separate modules...and you should! This example is a 
# do as I say... not as I do situation :)

# File Processing Classes====================================================================

class FileProcessor:
    def process(self):
        raise NotImplementedError("Subclasses must implement this method")

class TextFile(FileProcessor):
    def process(self):
        print("Reading and analyzing text content...")

class ImageFile(FileProcessor):
    def process(self):
        print("Loading image and applying filters...")

class AudioFile(FileProcessor):
    def process(self):
        print("Decoding audio and extracting waveform...")


# DEMO CODE STARTS HERE================================================================================



def main():
    # Example usage
    files = [TextFile(), ImageFile(), AudioFile()]

    for f in files:
        handle_file(f)   

# Polymorphic behavior
def handle_file(file: FileProcessor):
    file.process()


if __name__ == '__main__':
    main()
