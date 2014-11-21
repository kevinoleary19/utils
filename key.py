#!/usr/bin/env python
import requests
import json

api_key = ''

artist = raw_input('Artist: ')
song = raw_input('Song: ')

# first request gets the list of possible songs
query_args = {'api_key':api_key, 'artist':artist, 'title':song}
r = requests.get("http://developer.echonest.com/api/v4/song/search", params=query_args)
data  = json.loads(r.content)
# checks if songs were returned
if data['response']['songs']:
  song_id = data['response']['songs'][0]['id'] # gets the first song in the list
else:
  print 'No matching song found :('
  raise SystemExit

# second request gets the data for the individual song
query_args = {'api_key':api_key, 'id':song_id, 'bucket':'audio_summary'}
r = requests.get("http://developer.echonest.com/api/v4/song/profile", params=query_args)
data = json.loads(r.content)
song_artist = data['response']['songs'][0]['artist_name']
song_title = data['response']['songs'][0]['title']
# gets url of full analysis
url = data['response']['songs'][0]['audio_summary']['analysis_url']
# gets full analysis
full = requests.get(url)
full_data = json.loads(full.content)
track_data = full_data['track']

key_signature_id = track_data['key']
key_signature_confidence = str(int(100 * track_data['key_confidence'])) + ' %'
mode_id = track_data['mode']
mode_confidence = str(int(100 * track_data['mode_confidence'])) + ' %'

# converts key and mode data into key signature
chromatic_scale = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
interval = ['minor','major']
key = chromatic_scale[key_signature_id] + ' ' + interval[mode_id]

print '\n{st} by {sa} \nKey Signature  : {ks} \nKey Confidence : {kc} \nMode Confidence: {mc}\n'.format(st=song_title, sa=song_artist, ks=key,kc=key_signature_confidence, mc=mode_confidence) 

