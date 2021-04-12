from yandex_music import Client
import csv


class YandexMusicFavoritesToCSV():
	'''Class getting basic info about favorite tracks from your account'''
	
	def __init__(self, credentials):
		# initializing
		self.client = Client()

		# data for authorization
		self.credentials = credentials
		self.file = open(self.credentials, 'r').readlines()

		# strip symbols of new line
		self.username = self.file[0].rstrip('\n')
		self.password = self.file[1]

		# authorization
		self.client = Client.from_credentials(self.username, self.password)
		
	
	def number_of_liked_songs(self):
		'''count and return number of liked tracks'''

		counter = 0
		for i in self.client.users_likes_tracks():
			counter += 1
		return counter


	def basic_info_to_CSV(self, csv_name):
		'''get basic info, load it to CSV'''
			
		# load to CSV
		with open(csv_name, 'w', newline='') as csvfile:
			writer = csv.writer(csvfile, delimiter=',')

			# header
			writer.writerow(['song_id', 'artist', 'title', 'album', 'major',
							 'label', 'genre', 'release_date', 'year',
							 'duration', 'content_warning', 'explicit',
							 'song_type', 'file_size', 'regions',
							 'is_suitable_for_children'])

			favorites = self.client.users_likes_tracks()

			
			for i in range(len(favorites)):
				song_id = favorites[i].fetch_track().id
				title = favorites[i].fetch_track().title
				
				try:
					artist = favorites[i].fetch_track()['artists'][0]['name']
				except IndexError:
					print(f'Artist name not found, Nan value inserted!')
					artist = ''
				except TypeError:
					print(f'Artist name not found, Nan value inserted!')
					artist = ''

				try:
					album = favorites[i].fetch_track()['albums'][0]['title']
					
				except IndexError:
					print(f'Album name not found, Nan value inserted!')
					album = ''
				except TypeError:
					print(f'Album name not found, Nan value inserted!')
					album = ''
				
				try:
					genre = favorites[i].fetch_track()['albums'][0]['genre']
				except IndexError:
					print(f'Genre not found, Nan value inserted!')
					genre = ''
				except TypeError:
					print(f'Genre name not found, Nan value inserted!')
					genre = ''

				try:
					year = favorites[i].fetch_track()['albums'][0]['year']
				except IndexError:
					print(f'Year not found, Nan value inserted!')
					year = ''
				except TypeError:
					print(f'Year name not found, Nan value inserted!')
					year = ''

				try:
					major = favorites[i].fetch_track().major['name']
				except IndexError:
					print(f'Major name not found, Nan value inserted!')
					major = ''
				except TypeError:
					print(f'Major name not found, Nan value inserted!')
					major = ''

				try:
					label = favorites[i].fetch_track()\
										['albums'][0]['labels'][0]['name']
				except IndexError:
					print(f'Label name not found, Nan value inserted!')
					label = ''
				except TypeError:
					print(f'Label name not found, Nan value inserted!')
					label = ''
						
				try:
					release_date = favorites[i].fetch_track()\
										['albums'][0]['release_date']
				except IndexError:
					print(f'Release Date not found, Nan value inserted!')
					release_date = ''
				except TypeError:
					print(f'Release Date not found, Nan value inserted!')
					release_date = ''

				# to minutes
				try:
					duration = favorites[i].fetch_track().duration_ms / 60000   
				except TypeError:
					print(f'Duration not found, Nan value inserted!')
					duration = ''

				content_warning = favorites[i].fetch_track().content_warning
				explicit = favorites[i].fetch_track().explicit
				song_type = favorites[i].fetch_track().type
				file_size = favorites[i].fetch_track().file_size
				regions = favorites[i].fetch_track().regions
				
				is_suitable_for_children = \
						favorites[i].fetch_track().is_suitable_for_children	

				writer.writerow([song_id, artist, title, album, major, label,
								genre, release_date, year, duration,
								content_warning, explicit, song_type, file_size,
								regions, is_suitable_for_children])
				print(f'Row {i} successfuly loaded to CSV!')
				

		print('-----------------------------------------------')
		print(f'Music data successfuly uploaded to {csv_name}!')


						
# YandexMusicFavoritesToCSV('yandex_credentials.txt').number_of_liked_songs
# 2945

YandexMusicFavoritesToCSV('yandex_credentials.txt').basic_info_to_CSV('YndxMscFavTracks_Data.csv')