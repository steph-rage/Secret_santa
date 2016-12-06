from random import randint
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Santa_Values import participants


'''In order to use this tool, please fist create a spreadsheet in google drive. The spreadshet will need to have three columns: Name, Email or Phone Number, and Restrictions. Please choose if you would like to contact your participants by sending a personal email or a text message, and title your column accordingly. Once your participants have all filled out their information in your spreadsheet, you are ready to run the code!'''

restrictions = []
for person in participants:
	restrictions.append(person)
worked = False

def send_email():
	fromaddr = "me@example.com"
	gmail_password = "password"

	for email, giftee in santa_matches.items():
		toaddr = email
		msg = MIMEMultipart()
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = "Secret Santa"
		 
		body = "Personal message: Here's your person to buy for: {}".format(giftee)
		msg.attach(MIMEText(body, 'plain'))

		message = msg.as_string()

		
		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.ehlo()
		s.starttls()
		s.ehlo()
		s.login(fromaddr, gmail_password)
		s.sendmail(fromaddr, toaddr, message)
		s.close()
		print('email sent to {}'.format(email))
		
#def send_text():



while worked == False:
	santa_matches = {}
	choose_from = []
	for person in participants:
		choose_from.append(person)
	for person, email in participants.items():
		person_choices = choose_from.copy()
		for pair in restrictions:
			if person in pair:
				for i in range(2):
					try:
						person_choices.remove(pair[i])
					except ValueError:
						pass
		choices = len(person_choices)
		try:
			give_to = person_choices[randint(0, choices - 1)]
			santa_matches[email] = give_to
			choose_from.remove(give_to)
		except ValueError:
			pass
	if len(santa_matches) == len(participants):
		worked = True

print(santa_matches)