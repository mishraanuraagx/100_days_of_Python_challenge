
fizzBuzz_list = []
for i in range(1,101):
    str_replace = ""
    if i % 3 == 0:
        str_replace += "Fizz "

    if i % 5 == 0:
        str_replace += "Buzz"

    if len(str_replace) == 0:
        str_replace = str(i)

    fizzBuzz_list.append(str_replace)

print(fizzBuzz_list)


