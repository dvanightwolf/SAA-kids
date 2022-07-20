from django.urls import reverse


class ScratchGame:
    def __init__(self, id, title, img):
        self.id = id
        self.title = title
        self.img = img

    def get_url(self):
        return reverse('games:play_game',args=[self.id,self.title])


