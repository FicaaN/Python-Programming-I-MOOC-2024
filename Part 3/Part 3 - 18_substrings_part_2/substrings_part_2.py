string = input("Please type in a string: ")

length = len(string)
index = 0

for index in range(length + 1):
    print(string[length:])
    length -= 1   