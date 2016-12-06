from random import randint
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


participants = {"Person": "email"}
couples = []
worked = False


while worked == False:
	santa_matches = {}
	choose_from = []
	for person in participants:
		choose_from.append(person)
	for person, email in participants.items():
		person_choices = choose_from.copy()
		for pair in couples:
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

fromaddr = "me@example.com"
gmail_password = "password"

for email, giftee in santa_matches.items():
	toaddr = email
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Mansion on Mansion Secret Santa"
	 
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
	