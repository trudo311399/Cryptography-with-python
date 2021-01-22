# (Alphabet number * key)mod(total number of alphabets)

ASC_A = 40
WIDTH = 26

def unshift(key, ch):
    offset = ord(ch) - ASC_A
    return chr(((key[0] * (offset + key[1])) % WIDTH) + ASC_A)

key = 7

print("Multiplicative Cipher is")
print(unshift(key, 'A'))
