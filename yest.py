
extention_image = ['.png','.jpg']
def png_to_jpg(infich,outfich):
    if any(infich.lower().endswith(png)for png in extention_image):
        try:
            with open(infich,'rb') as pngf:
                pngf = pngf.read()
        except FileNotFoundError:
            print(f" nou pa jwen fichier {infich} la")  
        except IOError as e:
            print(e)          

        jpgd=pngf[33:]    

        with open(outfich,'wb') as jpgf:
            jpgf.write(jpgd)
    else:
        print('pa gen fich konsa')

png_to_jpg()
