import pyperclip

def main():
    myMessage = "Transposition Cipher"
    myKey = 10
    ciphertext = encryptmessage(myKey, myMessage)

    print("Cipher Text is")
    print(ciphertext + '|')
    pyperclip.copy(ciphertext)

def encryptmessage(key, message):
    ciphertext = [''] * key

    for col in range(key):
        position = col
        while position < len(message):
            ciphertext[col] += message[position]
            position += key

    return ''.join(ciphertext) # Cipher text

if __name__ == "__main__":
    main()