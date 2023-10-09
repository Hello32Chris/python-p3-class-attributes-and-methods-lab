class Song:

    all = []

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artist(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

        Song.all.append(self)


    # HERE IM TELLING IT TO COUNT HOW MANY SONGS ARE ADDED UPON __init__ **constructor method** VVVV

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1


    # HERE IM CREATING A LIST OF ALL THE GENRES AND RUNNING A CHECK TO KEEP DUPLICATES OUT VVVV

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artist(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    # HERE IM COUNTING THE NUMBER OF UNIQUE GENRES IGNORING ANY REPEATS VVVV

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1


    # HERE I CHECK FOR EVERYTIME A SONG IS SUBMITTED, IF THE ARTIST ALREADY EXISTS IN THE LIST -- IF SO I ADD 1 TO THE COUNT in the class attribute I created above called  artist_count = {}

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

