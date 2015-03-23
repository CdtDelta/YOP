# This program takes a copy of the base64 encoded string floating around in
# malicious office files right now, reassembles them into one line
# getting rid of the carriage returns, and then decodes that part of the file

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', dest='input_file', required=True, help='This is the input file for the base64 file to correct')
parser.add_argument('-o', dest='output_file', required=True, help='This is the output file for the corrected base64 file')
parser.add_argument('-b', dest='base64_file', required=True, help='This is the final decoded base64 file')
args = parser.parse_args()

# This function just takes out all the return characters and puts it in one line
def fix_file(filename):
    with open(filename, "r") as oldfile:
        with open(args.output_file, "w") as newfile:
            for oldfile_line in oldfile:
                oldfile_clean = oldfile_line.rstrip()
                newfile.write(oldfile_clean)
    return

# This takes the assembled file from the previous function and decodes it
def decode_base64(filename):
    with open(filename, "r") as file_to_decode:
        with open(args.base64_file, "w") as decoded_file:
            base64_decode = file_to_decode.read()
            decoded_file.write(base64_decode.decode('base64', 'strict'))
    return

fix_file(args.input_file)
decode_base64(args.output_file)