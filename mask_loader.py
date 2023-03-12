from PIL import Image

class MaskLoader:
    def __init__(self, path):
        self.img = Image.open(path)
        self.pix = self.img.load()
<<<<<<< HEAD
        img = Image.open(path)
        self.pix = img.load()
=======
>>>>>>> 788d9fc96d6071525376090cf1d1db55f9502b80
