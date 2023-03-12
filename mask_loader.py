from PIL import Image

class MaskLoader:
    def __init__(self, path):
        img = Image.open(path)
        self.pix = img.load()
        self.width, self.height = img.width, img.height
        self.mat = [[1] * self.width] * self.height

