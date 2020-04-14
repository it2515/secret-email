'''
Just  wiped this one together today. This program can send an encrypted message throgh gmail 
This was just a fun little project I came up with. Make sure you remember your key.  
@author: Chris Thummel 
'''
import smtplib
import onetimepad
import os

os.system('color 3f')



From = input('Your email')
password =input("your password")
to = input("recipient")
subject = input('enter your subject')
body = input("enter your message")
message = "Subject:{}\n\n{}".format(subject, body)
  
key = ''
cipher =''

Brovo = input('Do you want to cipher your message \n yes \n no \n') 
# this is asking if you want too cipher
if Brovo == 'yes':
   key = input('please enter your key.')
   cipher = onetimepad.encrypt(message, key)
   Brovo = cipher
elif Brovo == 'no':
	Brovo = message
# This dictats the response.	


try:
	Alpha = smtplib.SMTP('smtp.gmail.com', 587)
# Opening 
	Alpha.starttls()
#Secure TLS
	Alpha.login(From, password)
#login
	Alpha.sendmail(From, to, Brovo)
#Sending 
	Alpha.quit()
#Logout
	print ("message sent")
	print (cipher)

except Exception as E:
	print(E)




