from random import randint
import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from Santa_Values import participants, email_or_text, restrictions

worked = False

max_price = input("\nPlease enter the maximum amount you would like your participants to spend on each other: $")
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

send_email()
