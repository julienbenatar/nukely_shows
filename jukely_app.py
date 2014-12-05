from spyre import server

import pandas as pd
import time
from sets import Set
from jukely import *


class JukelyApp(server.App):

	def __init__(self):
		self.j = Jukely()
		self.shows = self.j.get_shows()


	title = "Free Jukely Shows"
	
	inputs =  [{"input_type":"checkboxgroup",
				"label": "Genres to include",
				'options': [
					{"label":"all", 'value':"all", "checked":True},
					{"label":"indie", 'value':"indi"},
					{"label":"rock", 'value':"rock"},
					{"label":"alternative", 'value':"alt"},
					{"label":"punk", 'value':"punk"},
					{"label":"electronic", 'value':"elec"},
					{"label":"folk", 'value':"folk"},
					{"label":"reggae", 'value':"reggae"},
					{"label":"metal", 'value':"metal"},
					{"label":"rap", 'value':"rap"},
					],
				"variable_name":"genres",
				"action_id":"html_id"
				},
				{"input_type":"checkboxgroup",
				'options': [{"label":"show videos", 'value':True}],
				"variable_name":"show_videos",
				"action_id":"html_id"
				}]

	controls = [{	"control_type" : "button",
					"control_id" : "button1",
					"label" : "refresh",
				}]

	outputs = [{	"output_type" : "html",
					"output_id" : "html_id",
					"on_page_load" : True,
				},
				{	"output_type" : "no_output",
					"output_id" : "refresh",
					"control_id" : "button1",
					"alert_message" : "Refresh Page to see new concerts"
				}]

	def noOutput(self,params):
		self.shows = self.j.get_shows()
		print "done"

	def getHTML(self,params):
		show_videos = params['show_videos']
		genres_to_include = params['genres']

		shows = self.shows
		html = ""
		for show in shows['events']:
			genres = show['headliner']['genres']
			genre_list = ", ".join(genres)
			display=0
			if 'all' not in genres_to_include:
				for g in genres_to_include:
					if genre_list.find(g)>=0:
						display += 1
				if display==0:
					continue
			if len(show_videos)>0 and show['headliner'].has_key('video_url'):
				url = show['headliner']['video_url']
				video_id = url.split("?v=")[1]
				video_embed = '<embed width="420" height="315" src="{}"><br>'.format("http://www.youtube.com/v/"+video_id)
			else:
				video_embed = ""
			html += """<div>
						<b>Headliner: {}</b><br>
						{}
						date: {}<br>
						genres: {}<br>
						also playing: {}<br>
						</div></br></br>""".format(
							show['headliner']['name'], 
							# show['image_url'], 
							video_embed,
							show['starts_at'][:10],
							genre_list,
							", ".join(show['other_artist_names'])
							)
		return html

app = JukelyApp()
app.launch(host='0.0.0.0', port=9876)
