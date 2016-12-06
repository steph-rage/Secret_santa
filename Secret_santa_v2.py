from random import randint
import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from Santa_Values import participants, email_or_text


'''In order to use this tool, please first create a spreadsheet in google drive. The spreadshet will need to have three columns: Name, Email or Phone Number, and Restrictions. Please choose if you would like to contact your participants by sending a personal email or a text message, and title your column accordingly. 
	
	Anything your participants put in the third column will be treated as excpetions. For example, if you would like people to avoid picking their significant other or their immediate family members, they should type that person's (those people's) name(s) in this column. The title of the third column is up to you, and feel free to leave it blank if this does not apply to your group. 

	Once your participants have all filled out their information in your spreadsheet, you are ready to run the code!'''


'''Please note that if you choose the email, you will be prompted to enter your email and password, which will be used to (securely) send emails through your email. If you are using gmail, you will have to turn on the setting to allow less secure apps.'''

restrictions = []
worked = False

max_price = input("Please enter the maximum amount you would like your participants to spend on each other: $")
gift_exchange_date = input("Please enter the date you would like to exchange gifts (in whatever format you choose): " )



def send_email():
	fromaddr = input("------------\nPlease enter the email address you would like to send emails from: ")
	frompassword = getpass.getpass("Please enter the password for the email address you are sending from: ")
	subject = input("What is the title for your emails? ")

	for email, people in santa_matches.items():
		toaddr = email
		msg = MIMEMultipart()
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = subject
		 
		body = "Happy holidays, {}! Your secret santa assignment is to get a present for {}. In order to keep things fair, please spend ${} or less. Secret santa gift exchange will occur on {}.".format(people[0], people[1], max_price, gift_exchange_date)
		msg.attach(MIMEText(body, 'plain'))

		message = msg.as_string()

		try:
			s = smtplib.SMTP('smtp.gmail.com', 587)
			s.ehlo()
			s.starttls()
			s.ehlo()
			s.login(fromaddr, frompassword)
			s.sendmail(fromaddr, toaddr, message)
			s.close()
			print('email sent to {}'.format(email))
		except smtplib.SMTPAuthenticationError:
			print("------------\nUh-oh! It looks like we are having trouble accessing your email. If you have a gmail account, you'll need to go to My Account -> Sign-in and Security, then scroll down and change 'Allow less secure apps' to 'On'. Please do this and try again.\n")
			break
		
#def send_text():


for person in participants:
	restrictions.append([person])
while worked == False:
	santa_matches = {}
	choose_from = []
	for person in participants:
		choose_from.append(person)
	for person, email in participants.items():
		person_choices = choose_from.copy()
		for group in restrictions:
			if person in group:
				for i in range(len(group)):
					try:
						person_choices.remove(group[i])
					except ValueError:
						pass
		choices = len(person_choices)
		try:
			give_to = person_choices[randint(0, choices - 1)]
			santa_matches[email] = [person, give_to]
			choose_from.remove(give_to)
		except ValueError:
			pass
	if len(santa_matches) == len(participants):
		worked = True

print(santa_matches)
send_email()
