#**FASILITE JPG_TO_PNG**
def jpg_to_png (infile, outfile) :
    try:
        with open(infile,'rb') as jpgf:
            jpgd = jpgf.read()
    except FileNotFoundError:
        print(f"Fichier non trouve", {infile})
        return
    except IOError as e:
        print(e)
        return

    pngd = b'\x89PNG\r\n\x1a\n' + jpgd[2:]
    try :
        with open (outfile, 'wb') as pngf:
            pngf.write(pngd)
    except IOError as e:
        print(e)
    
infile = "C:\\Users\\Thamie\\Pictures\\Saved Pictures\\IMG-20220911-WA0032.jpg"
outfile="C:\\Users\\Thamie\\Pictures\\Saved Pictures\\IMG-20220911-WA0032.png"
jpg_to_png(infile,outfile)