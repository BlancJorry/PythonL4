#**FASILITE JPG_TO_PNG**
infile = "C:/Users/Thamie/Pictures/Saved Pictures/IMG-20220911-WA0025.jpg"
outfile = "C:/Users/Thamie/Pictures/Saved Pictures/IMG-20220911-WA0025.png"

extensions_images = ['.jpg']

def jpg_to_png (infile, outfile) :
    if any(infile.lower().endswith(jpg) for jpg in extensions_images):
        try:
            with open(infile,'rb') as jpgf:
                jpgd = jpgf.read()
        except FileNotFoundError:
            print(f"Fichier non trouve", {infile})
            return
        except IOError as e:
            print(e)
            return

        pngd = b'\x89PNG\r\n\x1a\n' + jpgd
        try :
            with open (outfile, 'wb') as pngf:
                pngf.write(pngd)
                print("Conversion reussie!")
        except IOError as e:
            print(e)
    else:
        print("Le fichier n'est pas une image JPG valide")        
    
jpg_to_png(infile,outfile)
