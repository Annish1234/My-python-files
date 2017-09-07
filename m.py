#!/usr/bin/python3
import smtplib
 
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login("annishjk01@gmail.com", "krishna@123")
 
# message to be sent
message = "hi how do doing"
 
# sending the mail
s.sendmail("annishjk01@gmail.com", "annishjk01@gmail.com", message)
 
# terminating the session
s.quit()
