import requests


def send_simple_message(recepient, subject, content):
  	return requests.post(
  		"https://api.mailgun.net/v3/mg.nerdsfromspace.tech/messages",
  		auth=("api", "ce1edbd46a0e06f5fff2006219d76474-3724298e-3d3e441a"),
  		data={"from": "NerdsFromSpace Landstat <landsat@mg.nerdsfromspace.tech>",
  			"to": [recepient, recepient],
  			"subject": subject,
  			"text": content})

#send_simple_message("test@gmail.com", "Test Email", "This is a test email from the NerdsFromSpace Landsat API")