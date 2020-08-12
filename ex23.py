import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):  #  This will be called at the end to get thigns going.
    line = language_file.readline()     #  This reads one line from the languages file it is given. Just as before, using .readline() to deal with textfiles.


    if line:    #  The readline function will return an empty string when it reaches the end of the file and if line simply tests for this empty string.
        print_line(line, encoding, errors)  # As long as readline gives us something this will be True. If this is False, lines 9 and 10 are skipped.
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):     #  This is the function that does the actual encoding of each line from languages.txt
    next_lang = line.strip()    #  This simply strips off the trailing /n (newline) on the line string.
    raw_bytes = next_lang.encode(encoding, errors = errors)     #  Take the languages from the file and encode it into raw bytes
    cooked_string = raw_bytes.decode(encoding, errors = errors)     #  Then I call decode to decode the raw bytes into strings


    print(raw_bytes, "<===>", cooked_string)    #  Simply print both out to see what they look like.


languages = open("languages.txt", encoding = "utf-8")   # Opens the file in utf-8 coding

main(languages, input_encoding, error)      # This calls the 'main' function with all of the correct parameters and starts the loop.
#  The 'if line' statement prevents the loop from going on infinitely.