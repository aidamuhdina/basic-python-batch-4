import smtplib #smtp = simple mail transfer protocol
import os
import imghdr
from email.message import EmailMessage

#user dan password email pengirim
email = os.environ.get('EMAIL_USER')
password = os.environ.get('EMAIL_PASS')

#membaca list penerima dari file
receiver_file = open('receiver_list.txt', 'r')
temp = receiver_file.readlines()
receipent = []

for i in temp:
    receipent.append(i.strip())

receiver_file.close()


#pesan yang akan dikirim
print("\nPlease fill Email detail information below . .\n")
msg = EmailMessage()
msg['Subject'] = input("Insert Mail Subject : ")
msg['From'] = email
msg['To'] = ', '.join(receipent)
msg.set_content(input("Insert Mail Body : "))

#kirim gambar
images = ['love.jpg', 'merida.jpg']
for image in images:
    with open(image, 'rb') as im: #rb = read file in the binary mode
        data_im = im.read()
        type_im = imghdr.what(im.name)
        name_im = im.name

    msg.add_attachment(data_im, maintype='image', subtype=type_im, filename=name_im)

#kirim file
with open('laravel.pdf', 'rb') as f:
    file_data = f.read()
    file_name = f.name
msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

#465 = port sls. Bagian untuk enkripsi server
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email, password)
    smtp.send_message(msg)

print("\nEmail Sent. . .\n")