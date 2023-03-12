from PIL import Image

class MaskLoader:
    def __init__(self, path):
<<<<<<< HEAD
        self.img = Image.open(path)
        self.pix = self.img.load()

=======
        img = Image.open(path)
        self.pix = img.load()
>>>>>>> acb3ca3319d933a5b5da7b143e714dd697575262
