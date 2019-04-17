#Eğitim Amaçlı Onedio Haber Bülteni (Requests ve BeatifulSoup4)

import requests
from bs4 import BeautifulSoup
import time

while True:
    print("Onedio Haber Bülteni İçin Lütfen Bekleyin..")
    time.sleep(1)
    istek = requests.get("https://onedio.com/")

    icerik = istek.content

    soup = BeautifulSoup(icerik,"html.parser")
    time.sleep(1)
    sayı=1
    haberler = soup.find_all("h3")

    baslık=[]
    link=[]
    link1=[]

    # Göz Göz Göztepe!

    for i in haberler:
        b=i.text
        if (soup.find("a", {"title":b})) != None:
            baslık.append(i.text)
            link.append((soup.find("a", {"title":b})).get("href"))
        else:
            continue

    for i in link:
        a = "https://onedio.com/"
        link1.append(a+i)

    for i,j in zip(baslık,link):
        a="https://onedio.com/"
        print(sayı,"-",i)
        print(sayı,"-",a+j)
        sayı +=1
        print("*******")

    oku = int(input("\nOkumak istediğiniz haber numarasını girin: \n"))
    okulink = link1[oku-1]
    istekhaber = requests.get(okulink)

    souphaber = BeautifulSoup(istekhaber.content, "html.parser")

    for i in (souphaber.find_all("p")):
        print(i.text)

    geri=input("\nÇıkmak için q'ya basın. Geri Dönmek için Enter'a Basın..\n")


    if geri=="q" or geri=="Q":
        print("Onedio Haber Uygulaması Kapatılıyor!")
        time.sleep(1)
        break
    else:
        continue