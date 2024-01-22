import requests
from bs4 import BeautifulSoup
import csv

url = 'https://lenouvelliste.com/'

reponse = requests.get(url)

if reponse.ok:
    soup = BeautifulSoup(reponse.text, "html.parser")
    title = soup.find_all('h1')  
    lyen = soup.find_all('a')
    article = soup.find_all('div', class_='lnv-featured-article-lg')

    imglyen = []

    for div in article:
        imgt = div.find('img')
        if imgt:
            srcvaleur = imgt.get('src')
            imglyen.append(srcvaleur)

    with open('Nouv_donne.csv', mode='w', newline='') as e:
        ekri = csv.writer(e)

        ekri.writerow(['Titres'])  
        for titre in title:
            ekri.writerow([titre.text.strip()])  
            
        ekri.writerow(['Liens'])
        for lien in lyen : 
            ekri.writerow([lien.text.strip()])
    
        ekri.writerow(['Lien Images']) 
        for link in imglyen:
            ekri.writerow([link])
       
                        
                         


                
             
                    
                          
                            
                            