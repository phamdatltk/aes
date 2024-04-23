import aes, os
key = os.urandom(16)
iv = os.urandom(16)

################## Encrypt from sender from Sender folder
# Open file
print("Plaintext file content: ")
f = open('Sender/send.txt', 'r')
text = f.read()
f.close()
print(text)

plaintext = text.encode('utf-8')
print("Plaintext: ")
print(plaintext)

# Encrypt file and send it to Receiver
encrypted = aes.AES(key).encrypt_ctr(plaintext, iv)
f = open('Receiver/cipher.txt', "wb")
f.write(encrypted)
f.close()


################## Decrypt from receiver to Receiver folder
# Decrypt file cipher.txt
f = open('Receiver/cipher.txt', "rb")
encrypted = f.read()
decrypted = aes.AES(key).decrypt_ctr(encrypted, iv)
print("Decrypted: ")
print(decrypted)

# Create file receiver.txt
f = open('Receiver/receiver.txt', "w")
f.write(decrypted.decode('utf-8'))