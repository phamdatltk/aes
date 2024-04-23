import aes, os
key = os.urandom(16)
iv = os.urandom(16)

path_sender_image = "Sender/Group4.png"

################## Encrypt from sender from Sender folder
# Open file
f = open(path_sender_image, "rb")
text = f.read()
f.close()

# Encrypt file and send it to Receiver
encrypted = aes.AES(key).encrypt_ctr(text, iv)
f = open('Receiver/cipherImage', "wb")
f.write(encrypted)
f.close()


################## Decrypt from receiver to Receiver folder
# Decrypt file cipher.txt
f = open('Receiver/cipherImage', "rb")
encrypted = f.read()
decrypted = aes.AES(key).decrypt_ctr(encrypted, iv)

# Create file receiver.txt
if not os.path.exists('Receiver/Decrypted.png'):
    # Nếu không tồn tại, tạo file mới
    with open('Receiver/Decrypted.png', 'wb') as f:
      f.write(decrypted)
      f.close()