import string
example_string = "a-A"

ascii_str = string.ascii_letters
points = example_string.split("-")
start, end = ascii_str.index(points[0]), ascii_str.index(points[1])

result = ""
for i in range(start, end + 1):
    result += ascii_str[i]
print(result)
