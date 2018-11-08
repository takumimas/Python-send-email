def send_email(body,subject,from_add,to_add,password,smtp_add,port):
   import smtplib
    from email.mime.text import MIMEText
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_add
    msg["To"] = to_add
    s = smtplib.SMTP(smtp_add,port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(from_add,password)
    s.send_message(msg)
    s.close()
