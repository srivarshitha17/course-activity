#program to find no of digits,capital case letters, small case letters in a string
def check(string):
    lc_count,d_count,c_count = 0,0,0
    for i in string:
        if i >= '0' and i <= '9':
            d_count += 1
        elif i.islower():
            lc_count += 1
        elif i.isupper():
            c_count += 1
        else:
            pass
    return d_count, lc_count, c_count

input_str = input("Enter a string : ")
d_count, lc_count, c_count = check(input_str)
print(f"No of digits = {d_count}")
print(f"No of Capital case letters = {c_count}")
print(f"No of small case letters = {lc_count}")
