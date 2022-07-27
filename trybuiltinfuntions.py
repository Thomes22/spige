import smtplib

server = smtplib.SMTP_SSL("smtp.gamil.com", 587)

server.starttls()

server.login("thomeswake@gmail.com", "Xpress@24/7")
server.sendmail(from_addr="thomeswake@gmail.com",msg="Hi this is thomes " ,
                to_addrs="cspige@gmail.com " )

print("Mail sent")

