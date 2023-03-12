from PIL import Image

class MaskLoader:
    def __init__(self, path):
        self.img = Image.open(path)
        self.pix = self.img.load()

