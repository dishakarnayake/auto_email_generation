import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = "dishakarnayake0805@gmail.com"
password = "chickenlover"
subject = "subscription activation"

with open("email.csv","r") as csvfile:
    reader=csv.reader(csvfile)
    for line in reader:
        text=" hello "+ line[1] +" your "+line[2]+" plan has been activated"
        print(text)
        email_send=line[0]
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['subject'] = subject
        msg.attach(MIMEText(text,"plain"))
        text = msg.as_string()

        server=smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login(email_user,password)
        server.sendmail(email_user,email_send,text)
        print("successfully send msg")

        server.quit()


