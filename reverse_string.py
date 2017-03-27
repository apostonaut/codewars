def reverse(str):
    # base case
    reverse_str = ""
    if len(str) == 1:
        return str


    # recursive case
    else:

        return str[-1] + reverse(str[:-1])

str = "abcdefg"
print(reverse(str))