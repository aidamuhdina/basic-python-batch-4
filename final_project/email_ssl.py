import smtplib #smtp = simple mail transfer protocol
import os
import imghdr
from email.message import EmailMessage

email = os.environ.get('EMAIL_USER')
password = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = "image and file attachment"
msg['From'] = email
msg['To'] = "aidamuhdina@gmail.com"
msg.set_content("image and file attached . . . check it out!")

#kirim gambar
images = ['love.jpg', 'merida.jpg']
for image in images:
    with open(image, 'rb') as im: #rb = read by
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

print("Email Terkirim. . .")