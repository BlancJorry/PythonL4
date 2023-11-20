#kreye klas poum fe konvesyon de JPG_TO_PNG**
class PngClass :

    def jpg_to_png(infile, outfile) :
        extensions_images = ['.jpg']
        if any(infile.lower().endswith(jpg) for jpg in extensions_images) :
            try:
                with open(infile, 'rb') as jpgf:
                    jpgd = jpgf.read()
            except FileNotFoundError :
                print(f"fichier non trouve",{infile})
                return
            except IOError as e :
                print(e)
        
        pngd = b'\x89JPG\r\n\x1a\n' + jpgd
        try :
            with open (outfile, 'wb') as pngf :
                 pngf.write(pngd)
                 print("conversion reussie**")
        except IOError :
            print("Le fichier n'est pas une image valide")

infile = "C:/Users/Thamie/Desktop/Pict/Pict1.jpg"
outfile = "C:/Users/Thamie/Desktop/Pict/Pict1.png"
PngClass.jpg_to_png(infile,outfile)

    