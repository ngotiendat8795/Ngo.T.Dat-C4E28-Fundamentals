import smtplib


server = smtplib.SMTP('smtp.gmail.com',587)

server.ehlo()
server.starttls()
server.ehlo()

server.login('ngotiendat8795@gmail.com','lifeisbeautiful8795')



msg  = "Never been to me"
server.sendmail("ngotiendat8795@gmail.com","diemquynhhoang21@gmail.com",msg)



