message = 'This is program to explain reverse cipher'
translated = '' # cipher text is stored in this variable
i = len(message) - 1

while i >= 0:
    translated += message[i]
    i -= 1

print('The cipher text is : ', translated)