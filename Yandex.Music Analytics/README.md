### Python classes for analysis of your favorite songs from Yandex.Music
1. Create `txt file` with your credentials and place them in folder with scripts or directly in `YandexMusicFavoritesToCSV` class to the fields `self.username` and `self.password`
2. `YandexMusicFavoritesToCSV.py`<br />
`YandexMusicFavoritesToCSV('yandex_credentials.txt').number_of_liked_songs` - return number of liked songs
3. `PySparkCSVtoPlots.py`<br />
`YandexMusicFavoritesToCSV('yandex_credentials.txt').basic_info_to_CSV('YndxMscFavTracks_Data.csv')` - creates `csv file` with basic info of your liked songs
