from io import BytesIO
from PIL import Image

def png_to_jpg(infich,outfich):
    try:
        with open(infich,'rb') as pngf:
            pngd = pngf.read()
    except FileNotFoundError:
        print(f" nou pa jwen fichier {infich} la")  
    except IOError as e:
        print(e)          

    jpgd=pngd[33:]    

    with open(outfich,'wb') as jpgf:
        jpgf.write(jpgd)


png_to_jpg()
