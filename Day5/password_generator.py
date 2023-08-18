import argparse
import random

example_text = '''example:

 python password_generator.py
 python password_generator.py -l 20 -ns 5 -ni 10
 python password_generator.py -d'''

# Initialize parser
# You need to use the epilog and the formatter_class arguments to ArgumentParser if you want to have the help the example printed at the end (epilog) and to preserve the whitespace/formatting (formatter_class set to RawDescriptionHelpFormatter).
parser = argparse.ArgumentParser(
    epilog=example_text, formatter_class=argparse.RawDescriptionHelpFormatter)

# Adding optional argument
parser.add_argument("-l","--length", help = "Length of the password")
parser.add_argument("-ns","--symbolCount", help = "Number of Symbols to be included")
parser.add_argument("-ni","--integerCount", help = "Number of integer to be included")
# if -d is not used, set the value to False, if used then set it to True
parser.add_argument("-d", "--default", nargs='?', const=True, default=False, type=bool, help="Use default settings")
# Read arguments from command line
args = parser.parse_args()
print(args)



if args.default:
    length = 15
    intCount = 5
    symbolCount = 5
else:
    if args.length == None:
        #print(f"Displaying value of length: {args.length}")
        args.length = input("How many letters would you like in your password? ")

    if args.symbolCount == None:
        #print(f"Displaying value of length: {args.length}")
        args.symbolCount = input(
            "How many symbols would you like in your password? ")


    if args.integerCount == None:
        #print(f"Displaying value of length: {args.length}")
        args.integerCount = input(
            "How many numbers would you like in your password? ")


    length = int(args.length)
    intCount = int(args.integerCount)
    symbolCount = int(args.symbolCount)

if length - intCount - symbolCount < 0:
    print(
        "Length of the password is short to include {intCount} Integers & {symbolCount} Symbols")
    exit()

password = ""
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbolList = "!#$%&*()_+?/"
numbersList = "1234567890"
# Generate Password
for _ in range(length):
    char = random.choice(list(alphabets))
    password += char

password = list(password)
argList = [i for i in range(length)]
number_argsList = random.sample(argList,intCount)
symbol_argsList = random.sample(list(set(argList) - set(number_argsList)), symbolCount)

for i in number_argsList:
    password[i] = random.choice(list(numbersList))

for i in symbol_argsList:
    password[i] = random.choice(list(symbolList))

print("".join(password))

