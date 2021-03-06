import smtplib, os
#smtp = simple mail transfer protocol

email = os.environ.get('EMAIL_USER')
password = os.environ.get('EMAIL_PASS')

#587 = port tls. Bagian untuk enkripsi server
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(email, password)
    
    subject = "Grab dinner this weekend?"
    body = "How about dinner this saturday at 6pm?"
    msg = f"Subject: {subject}\n\n{body}"

    #formatnya (sender_email, Receipent_email, Message)
    smtp.sendmail(email, 'tefanzprih@gmail.com', msg)
    
