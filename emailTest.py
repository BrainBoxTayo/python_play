import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib, ssl
password = input("Please enter your password")
address_book = ['temitayo.akanbi-bello@ndwestern.com', 'teetayotemi23@gmail.com', 'group3@company.com']
msg = MIMEMultipart()    
sender = 'temitayo.akanbi-bello@ndwestern.com'
subject = "My subject"
body = "This is my email body"

msg['From'] = sender
msg['To'] = ','.join(address_book)
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))
text=msg.as_string()
# Create a secure SSL context
context = ssl.create_default_context()
# Send the message via our SMTP server
s = smtplib.SMTP('smtp.office365.com')
try:
    s.starttls(context=context)
    s.login(sender, password)
    s.sendmail(sender,address_book, text)
except Exception as e:
    print(e)
finally:
    s.quit()
