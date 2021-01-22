from Crypto import Random
from Crypto.PublicKey import RSA
import base64

def generate_keys():
    # Key length must be a multiple of 256 and >= 1024
    modulus_length = 256*4
    privatekey = RSA.generate(modulus_length, Random.new().read)
    publickey = privatekey.publickey()
    return privatekey, publickey

def encrypt_message(a_message, publickey):
    encrypted_msg = publickey.encrypt(a_message, 32)[0]
    encoded_encrypted_msg = base64.b64encode(encrypted_msg)
    return encoded_encrypted_msg

def decrypt_message(encoded_encrypted_msg, privatekey):
    decoded_encrypted_msg = base64.b64decode(encoded_encrypted_msg)
    decoded_decrypted_msg = privatekey.decrypt(decoded_encrypted_msg)
    return decoded_decrypted_msg

a_message = b'This is the illustration of RSA algorithm of asymmetric cryptography'
privatekey, publickey = generate_keys()
encrypted_msg = encrypt_message(a_message, publickey)
decrypted_msg = decrypt_message(encrypted_msg, privatekey)

print('%s - (%d)' % (privatekey.exportKey(), len(privatekey.exportKey())))
print('%s - (%d)' % (publickey.exportKey(), len(publickey.exportKey())))
print('Original content: %s - (%d)' % (a_message, len(a_message)))
print('Encrypted message: %s - (%d)' % (encrypted_msg, len(encrypted_msg)))
print('Decrypted message: %s - (%d)' % (decrypted_msg, len(decrypted_msg)))