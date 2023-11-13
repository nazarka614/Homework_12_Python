class Player:
    def __init__(self, name, video_link, duration):
        self.name = name
        self.video_link = video_link
        self.duration = duration
        self.playing = True
        self.quality = "HD"

    def play(self, new_video_link):
        self.playing = self.video_link == new_video_link
        return self.playing

    def pause(self):
        self.playing = not self.playing

    def change_quality(self, new_quality):
        self.quality = new_quality
