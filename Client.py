import base64
import hashlib

from Crypto import Random
from Crypto.Cipher import AES

import requests
import random

class AESCipher(object):
    """
    A classical AES Cipher. Can use any size of data and any size of password thanks to padding.
    Also ensure the coherence and the type of the data with a unicode to byte converter.
    """
    def __init__(self, key):
        self.bs = 32
        self.key = hashlib.sha256(AESCipher.str_to_bytes(key)).digest()

    @staticmethod
    def str_to_bytes(data):
        u_type = type(b''.decode('utf8'))
        if isinstance(data, u_type):
            return data.encode('utf8')
        return data

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * AESCipher.str_to_bytes(chr(self.bs - len(s) % self.bs))

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

    def encrypt(self, raw):
        raw = self._pad(AESCipher.str_to_bytes(raw))
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw)).decode('utf-8')

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

IP = ['http://127.0.0.1:8000', 'http://127.0.0.1:8001', ...
'http://127.0.0.1:8002', 'http://127.0.0.1:8003']

IP = random.shuffle(IP)

cipher = AESCipher(key='mykey')
encrypted = cipher.encrypt("hey")
print("Encryption Layer 1: ",encrypted, '\n')

cipher2 = AESCipher(key='mykey2')
encrypted2 = cipher2.encrypt(encrypted)
print("Encryption Layer 2: ", encrypted2, '\n')

cipher3 = AESCipher(key='mykey3')
encrypted3 = cipher3.encrypt(encrypted2)
print("Encryption Layer 3: ", encrypted3, '\n')

new_cipher3 = AESCipher(key='mykey3')
decrypted3 = new_cipher3.decrypt(encrypted3)
print("Decryption Layer 3: ", decrypted3, '\n')

new_cipther2 = AESCipher(key='mykey2')
decrypted2 = new_cipther2.decrypt(decrypted3)
print("Decryption Layer 2: ", decrypted2, '\n')

new_cipher = AESCipher(key='mykey')
decrypted = new_cipher.decrypt(decrypted2)
print("Decryption Layer 1: ", decrypted, '\n')

def send_post_request(data):
    r = requests.post('http://127.0.0.1:8000', data)
   

    print(r.text)

if __name__ == '__main__':
    send_post_request(encrypted3)
 #    send_post_request(decrypted)
 