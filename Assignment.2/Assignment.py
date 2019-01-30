import os.path
import pickle


class DictionaryEncoder:

    """This class provides both encoding and decoding of text files into an integer only format with dictionary
        encoding key for integer to word translation."""
    # these two aren't actually used, they're just stubs for reminder,
    # doesn't matter if I use them they're only in one place in the class
    encoding = 0
    decoding = 1

    def __init__(self, input_file_name, output_file_name, opr):
        self.operation = opr
        self.dictionary = dict()
        self.encoded_string = str()
        self.decoded_string = str()
        self.input_file = None
        self.output_file = None
        self.encoding_key = 0
        self.read_file(input_file_name, output_file_name)

    def read_file(self, input_file_name, output_file_name):
        """Read a text format file and begin encoding, this method only executes the first iteration, actual encoding
                takes place in another method"""
        # check the operation required
        if self.operation == 0:
            # encoding
            # open the input file in read only mode
            self.input_file = open(input_file_name, 'r')
            # read the entire input file into a string
            lines = self.input_file.read()
            # initial pass to insert unique characters in the dictionary
            for s in lines:
                # only insert new characters that haven't been inserted in the dictionary
                if s not in self.dictionary:
                    # the dictionary format is integer:word
                    self.dictionary[self.encoding_key] = s
                    # increment the encoding key in preparation for next word
                    self.encoding_key += 1
            # reset file cursor to beginning of file
            self.input_file.seek(0)
            # close the file as it's no longer needed, we've already read it into a string
            self.input_file.close()
            # call the method that does the actual encoding
            self.encode_string(lines)
            # open the output file in overwrite binary mode
            self.output_file = open(output_file_name, 'wb')
            # serialize the dictionary to the beginning of file
            pickle.dump(self.dictionary, self.output_file, pickle.HIGHEST_PROTOCOL)
            # serialize the encoded string after the dictionary
            pickle.dump(self.encoded_string, self.output_file, pickle.HIGHEST_PROTOCOL)
            # close the output file, this is the end of encoding
            self.output_file.close()
            # get the compression ratio and print it
            print("Compression ratio [uncompressed size/compressed size] is",
                  "{:.3f}".format(os.path.getsize(input_filename) / os.path.getsize(output_file_name)),
                  "or exactly", os.path.getsize(input_filename) / os.path.getsize(output_file_name))
        else:
            # decoding
            # open the input file in read only binary mode as it's a binary file
            self.input_file = open(input_file_name, 'rb')
            # unpickle the pickled dictionary key from file
            self.dictionary = pickle.load(self.input_file)
            # unpickle the pickled encoded string from the file
            self.encoded_string = pickle.load(self.input_file)
            # call the function that does the actual decoding
            self.decode_string(self.encoded_string)
            # open the output file in overwrite mode
            self.output_file = open(output_file_name, 'w')
            # write the decoded string to output file
            self.output_file.write(self.decoded_string)
            # close the file, this is the end of decoding
            self.output_file.close()

    def encode_string(self, string):
        # the encoding will be done in the encoded_string by replacement so initially it has the plaintext string
        self.encoded_string = string
        # initialize the loop counter, its value never actually changes, it always stays 0, it's the iterable string
        # that gets truncated with every iteration
        i = 0
        # iterate over the string
        while i < len(string):
            # how many characters ahead of current character to check
            lookahead = len(max(self.dictionary.values(), key=len))
            # iterate decreasingly over the lookahead range
            for j in range(lookahead, 0, -1):
                # if the current word is in dictionary then encode, if not continue loop decreasing the lookahead
                if string[i:i+j] in self.dictionary.values():
                    # replace the word with its encoding in the encoded string
                    # this statement is quite packed, it's simply a replacement of the plaintext word in the string
                    # with its corresponding encoding in the dictionary and separates encodings with ','
                    self.encoded_string = self.encoded_string\
                        .replace(string[i:i+j],
                                 str(list(self.dictionary.keys())[list(self.dictionary.values()).index(string[i:i+j])])
                                 + ',', 1)
                    # this is how the loop terminates, the string keeps getting sliced shorter
                    # as parts of it are encoded
                    string = string[i+j:]
                    try:
                        # encode the currently encoded word plus the first character in the next block
                        self.dictionary[self.encoding_key] = string[i:i+j+1]
                        # increment the current encoding index
                        self.encoding_key += 1
                    except BaseException:
                        # this is only in case [:i+j+1] goes beyond the string bounds but this shouldn't happen
                        print("There was an error trying to read plaintext string out of bounds")
                    break
        # remove the trailing separator ','
        self.encoded_string = self.encoded_string[:-1]
        return self.encoded_string

    def decode_string(self, string):
        """Decode the string in a straightforward process by simply replacing integers with their corresponding words
                in the dictionary"""
        # string the string just for cleanliness
        string = string.strip()
        # if there is a trailing ',' remove it. This is already done during encoding, it's just for redundancy.
        if string[-1] == ',':
            string = string[:-1]
        # split the string around the separator and iterate over the elements
        for i in string.split(','):
            # if the current integer code is found in the dictionary do a translating, the check is redundant
            if int(i) in self.dictionary:
                # simply append the corresponding work to the integer to the decoded string
                self.decoded_string += self.dictionary.get(int(i))
        return self.decoded_string


# get the input file name
input_filename = input("Input filename or absolute or relative path: ")
# if the input file name or path can't be found loop until a new file name is found
while not os.path.isfile(input_filename):
    print("File can't be found on disk. Check the name or path")
    input_filename = input("Input filename or absolute or relative path: ")
# get the output file name
output_filename = input("Output filename or absolute or relative path (if file exists it will be overwritten): ")
# get the code for the desired operation
while True:
    try:
        operation = int(input("Operation [0:Encode/1:Decode]: "))
    except ValueError:
        print("Invalid input, integer 0/1 only")
        continue
    if operation != 0 and operation != 1:
        print("Invalid input, possible values 0/1")
        continue
    break
print("Staring process...")
# initialize the encoder, it takes care of the rest
DictionaryEncoder(input_filename, output_filename, operation)
