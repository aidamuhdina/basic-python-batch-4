# python -m smtpd -c DebuggingServer -n localhost:1025 (ketik di terminal anaconda)
import smtplib, os
#smtp = simple mail transfer protocol

email = os.environ.get('EMAIL_USER')
password = os.environ.get('EMAIL_PASS')

#587 = port tls. Bagian untuk enkripsi server
with smtplib.SMTP('localhost', 1025) as smtp:
    subject = "Grab dinner this weekend?"
    body = "How about dinner this saturday at 6pm?"
    msg = f"Subject: {subject}\n\n{body}"

    #formatnya (sender_email, Receipent_email, Message)
    smtp.sendmail(email, 'syarifahratna22@gmail.com', msg)
    