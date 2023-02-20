class Guitar:
    def play(self):
        return "Playing the guitar"


class Children:
    def play(self):
        return "Children are playing"


def start_playing(song):
    return song.play()


guitar = Guitar()
print(start_playing(guitar))

children = Children()
print(start_playing(children))
