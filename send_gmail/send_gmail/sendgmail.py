from smtplib import SMTP
msg=input()
subject = " test "
message = msg
content ="subject : {} \n\n".format(subject,message)

mymail="orcun8522@gmail.com"
password="dwdmqcupilymnfls"

sendto="orcun8522@gmail.com"

mail = SMTP("SMTP.gmail.com",587)
mail.ehlo()
mail.starttls()
mail.login(mymail,password)
mail.sendmail(mymail,sendto,message.encode("utf-8"))
print("succesful")

