import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 535 #for starttls
sender_emails = "jennyfergoj1571999@gmail.com"
password = "Suryal143"

# create a secure ssl context
context = ssl.create_default_context()

try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_emails,password)

except Exception as e:
    print(e)
finally:
    server.quit()