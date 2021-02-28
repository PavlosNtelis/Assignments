print("Enter the file name with the .txt extension")
x = input()
ascii = ""
with open(x) as f: 
    regular = f.read()
for letter in regular:
    asc = ord(letter)
    ascii += chr(128 - asc)
reverse = ascii[::-1]
print(ascii)

