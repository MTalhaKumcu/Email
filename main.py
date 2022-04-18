import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj  = MIMEMultipart()
mesaj ["From"] = "mkumcu151@gmail.com"
mesaj ["To"] = "mkumcu151@gmail.com"
mesaj["subject"] = "Smtp Mail Gonderme"

yazi = """

Smtp ile masil gonderiyorum

-MTK

"""

message_main = MIMEText(yazi,"plain")
mesaj.attach(message_main)


try :
    mail = smtplib.SMTP("smp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("mkumcu151@gmail.com","Password")
    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
    print("Mail success")
    mail.close()
except:
    sys.stderr.write("has Fail")
    sys.stderr.flush()