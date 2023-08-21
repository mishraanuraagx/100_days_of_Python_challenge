# -*- coding: utf-8 -*-
import argparse

ALPHABETS = "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, Ä, Ö, Ü, ß".lower().split(", ")

# not using these as the casing of the cipher can't be retained.
# SYMBOLS = ", !, @, #, $, %, ^, &, *, (, ), _, +, -, =, [, ], {, }, :, ;, ', <, >, ., ?, /";
example_text = '''example:

    python caesar_cipher.py
    # Encode: python caesar_cipher.py -e -s "String" -sh 8
    # Decode: python caesar_cipher.py -d -s "String" -sh 8'''
parser = argparse.ArgumentParser(
epilog=example_text, formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument("-s","--string", help = "Enter the string to encode-decode")
parser.add_argument("-sh","--shift", help = "Caesar-Cipher shift number", type=int)
# if -d is not used, set the value to False, if used then set it to True
parser.add_argument("-d", "--decode", nargs='?', const=True, default=False, type=bool, help="Decode the string")
# if -e is not used, set the value to False, if used then set it to True
parser.add_argument("-e", "--encode", nargs='?', const=True, default=False, type=bool, help="Encode the string")



def encode(word, shift: int):
    encoded_word = []
    for i in list(word):        
        if i.lower() in ALPHABETS:
            char_index = ALPHABETS.index(i.lower())
            encode_char = ALPHABETS[(char_index+shift)%len(ALPHABETS)]
            # save the case of the letter, ignore case save if char is ß
            if i.isupper() and encode_char != "ß": encode_char = encode_char.upper()
        else:
            encode_char = i
        encoded_word.append(encode_char)

    return "".join(encoded_word)

def decode(word, shift: int):
    decoded_word = []
    for i in list(word):
        if i.lower() in ALPHABETS:
            char_index = ALPHABETS.index(i.lower())
            decode_char = ALPHABETS[(char_index-shift)%len(ALPHABETS)]
            # get the case of the letter, ignore case save if char is ß
            if i.isupper() and decode_char != "ß": decode_char = decode_char.upper()
        else:
            decode_char = i
        decoded_word.append(decode_char)

    return "".join(decoded_word)


def get_input(arg_list):
    # use the command line args if provided
    if len(arg_list) == 3:
        print(arg_list)
        return arg_list

    action = input("Please tell us what operation would you like to do by typing 'encode' or 'decode' ")
    word = input("Enter the string:  ")
    shift = int(input("Enter the shift number:  "))
    return [action, word, shift]

def main(arg_list):    
    user_input = get_input(arg_list)
    word = encode(user_input[1],user_input[2]) if user_input[0].lower() == "encode" else decode(user_input[1],user_input[2])

    print(word)
    return

if __name__ == "__main__":
    # Read arguments from command line
    args = parser.parse_args()
    arg_list = []
    if args.shift != None and args.string != None:
        action = 'encode'if args.encode == True else 'decode'
        arg_list = [action, args.string, int(args.shift)]
    main(arg_list)
