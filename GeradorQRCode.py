import os
import pyqrcode
from PIL import Image

class QR_Gerador(object):
    def __init__(self, text):
        self.qr_image = self.qr_generator(text)

    @staticmethod
    def qr_generator(text):
        qr_code = pyqrcode.create(text)
        nomeArquivo = "QR gerado"
        save_path = os.path.join(os.path.expanduser('~'),'Desktop')

        name = (f"{save_path}{nomeArquivo}.png")
        qr_code.png(name, scale=10)
        image = Image.open(name)
        image = image.resize((400,400),Image.ANTIALIAS)
        image.show()

if __name__ == "__main__":
    QR_Gerador(input("[QR] Entre com o link: "))