import argparse

import simplecrypt
from simplecrypt import decrypt
import sys

def read_encrypted(password, filename, string=True):
    with open(filename, 'rb') as input:
        ciphertext = input.read()
        plaintext = decrypt(password, ciphertext)
        if string:
            return plaintext.decode('utf8')
        else:
            return plaintext

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--encrypted_filename")
    parser.add_argument('-p', '--passwords')
    args = parser.parse_args()
    if args.encrypted_filename:
        encrypted_filename = args.encrypted_filename
    else:
        encrypted_filename = 'encrypted.bin'
    if args.passwords:
        passwords = args.passwords
    else:
        passwords = "passwords.txt"
    try:
        with open(passwords, "r") as ps:
            for line in ps:
                try:
                    encrypted = read_encrypted(line.strip(), encrypted_filename)
                    print('Password is', line.strip())
                    print("Secret is", encrypted)
                    break
                except simplecrypt.DecryptionException:
                    continue
    except KeyboardInterrupt:
        print("Interrupted by user")
        sys.exit(0)
    except FileNotFoundError:
        print("Error:", encrypted_filename, "or", passwords,  "not found")
        sys.exit(1)
    except Exception as s:
        print(type(s), s)
        sys.exit(2)
