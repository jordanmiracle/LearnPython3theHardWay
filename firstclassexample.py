
class Song(object):

    def __init__(self,lyrics):
        self.lyrics = lyrics



    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def artist(self):
        self.artist = artist





happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there",])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

all_thats_left_is_love = Song(["The world is different now, We feel more of us.",
                                "This place is such a mess, but we always pass the test.",
                                "When you feel like looking up, when the days are getting tough.",
                                "We're gettin' us that drug, A little bits enough.",
                                "When all that's left is love."])

tunnels = Song(["I am still without devotion, cause we\'re all asleep at the wheel."
                "Asleep and so surrounded by what we feel"])

AVA = Song.artist(["Angels&Airwaves"])


happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

all_thats_left_is_love.sing_me_a_song()


tunnels.sing_me_a_song()

MyStuff = {'apples': "I am apples!"}


