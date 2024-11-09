# add your code here

abc = "abcdefghijklmnopqrstuvwxyz"

shift = 5
#shift = int(input("Please enter the number of places to shift: "))
index = abc.find("z")
index = (index + shift) % 26
char = abc[index]
#print(char)


original_text = input("Please enter a  sentence: ")
original_text = original_text.lower()


encrypted_text = ""
for char in original_text:
    if char in abc:
        index = abc.find(char)
        index = (index + shift) % 26
        char = abc[index]
    encrypted_text += char

print(original_text)
print (encrypted_text)
