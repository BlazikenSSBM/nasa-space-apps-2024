import requests
import hidden_vars


def send_simple_message(recepient, subject, content):
  	return requests.post(
  		hidden_vars.MAILURL,
  		auth=("api", hidden_vars.MAILKEY),
  		data={"from": hidden_vars.MAILEMAIL,
  			"to": [recepient, recepient],
  			"subject": subject,
  			"text": content})

#send_simple_message("test@gmail.com", "Test Email", "This is a test email from the NerdsFromSpace Landsat API")