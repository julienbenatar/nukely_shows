from requests import session
import json
import credentials

# username and password should be stored in credentials.py as:
# username ='something@somewhere.com'
# password = 'password'

username = credentials.username
password = credentials.password

class Jukely():
	def get_shows(self):
		with session() as c:
			y = c.get('https://jukely.com/log_in')
			auth_text = '"authenticity_token" type="hidden" value="'
			s = y.text.find(auth_text)+len(auth_text)
			f = y.text[s:].find('" />')
			auth_token = y.text[s:(s+f)]
			payload = {'authenticity_token': auth_token, 
						'username': username,
						'password': password}
			
			c.post('https://jukely.com/sessions',data=payload, auth=(username, password))
			try:
				request = c.get('https://unlimited.jukely.com/shows', auth=(username, password))
			except:
				print "error"

		response = request.text
		event_tag = 'window.events = '
		s = response.find(event_tag)+len(event_tag)
		f = response[s:].find(";\n")
		shows = json.loads(response[s:(s+f)])
		return shows
