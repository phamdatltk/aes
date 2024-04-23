# Mô phỏng AES với text file
Project này mô phỏng quá trình mã hóa bằng thuật toán AES.

Input:
- File text: `Sender/send.txt`

Output: 
- File encrypted: `Receiver/cipher.txt`
- File text: `Receiver/receiver.txt`

## Hướng dẫn sử dụng (File text)
- Vào trong file send.txt, nhập nội dung muốn truyền tải, sau đó nhấn save
- Chạy file main.py
- Kết quả: 
  - File mã hóa: đoạn văn bản được mã hóa
  - File giải mã: đoạn văn bản sau giải mã

# Mô phỏng AES với file png
Project này mô phỏng quá trình mã hóa bằng thuật toán AES.

Input:
- File text: `Sender/Group4.png`

Output: 
- File encrypted: `Receiver/cipherImage`
- File text: `Receiver/Decrypted.png`

## Hướng dẫn sử dụng (File image)
- Copy ảnh vào trong thư mục sender
- Sửa đường dẫn vào biến `path_sender_image` trong file image.py, sau đó nhấn chạy file này
- Kết quả: 
  - File mã hóa: file mã hóa ảnh
  - File ảnh giải mã: ảnh sau giải mã