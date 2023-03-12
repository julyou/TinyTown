from PIL import Image

class MaskLoader:
    def __init__(self, path):
        img = Image.open(path)
        self.pix = img.load()
    