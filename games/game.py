from django.urls import reverse


class ScratchGame:

    def __init__(self,index,id, title, img, description):
        self.id = id
        self.index = index
        self.title = title
        self.img = img
        self.description = description

    def get_url(self):
        return reverse('games:play_game', args=[self.id, self.title])
