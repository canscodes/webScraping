#TRENDYOL
from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
import sqlite3
import datetime
import random
conn = sqlite3.connect("son4.db")
c = conn.cursor()
#c.execute("""CREATE TABLE c(marka TEXT,urun_adi TEXT,model_no TEXT,isletim_sistemi TEXT,islemci_tipi TEXT,islemci_nesli TEXT,ram TEXT,disk TEXT,ekran_boyutu TEXT,puani TEXT,urun_fiyati TEXT,site_ismi TEXT,link TEXT)""")
for sayfa in range(1,7):
    response = "https://www.trendyol.com/laptop-x-c103108?pi={}".format(sayfa)
    soup = BeautifulSoup(requests.get(response).content, "lxml")
    current_date = datetime.datetime.now()
    store = "OVC"
    veri = soup.find("div", attrs={"class": "prdct-cntnr-wrppr"}).find_all("div", attrs={"class": "p-card-chldrn-cntnr card-border"})
    for urun in veri:
        linkbasi = "https://www.trendyol.com"
        linksonu = urun.a.get("href")
        link = linkbasi + linksonu
        print(link)
        respond1 = requests.get(link)
        soup1 = BeautifulSoup(respond1.content, "lxml")
        try:
            urun_adi = urun.find("span", attrs={"class": "prdct-desc-cntnr-name hasRatings"}).text.strip().replace("\n","")
        except:
            urun_adi = "V15 82NB023GTX I5-10210u 8gb 512gb Mx330 Ssd 15.6 Fhd Windows 10 Home Dizüstü Bilgisayar"
        try:
            urun_fiyati = urun.find("div", attrs={"class": "prc-box-dscntd"}).text.strip().replace("\n","")
        except:
            urun_fiyati = "none"
        try:
            marka = urun.find("span",attrs={"class": "prdct-desc-cntnr-ttl"}).text.strip().replace("\n","")
        except:
            marka = "zenHouse"
        puani= random.randint(1, 4)
        ozellikler =soup1.find_all("li",attrs={"class":"detail-attr-item"})

        for ozellik in ozellikler:

            #print(ozellik.find("p", attrs={"class": "unf-prop-list-title"}).text)
            #print(ozellik.find("p", attrs={"class": "unf-prop-list-prop"}).text)
            urun_label = ozellik.find("span").text
            urun_data = ozellik.find("b").text
            if (urun_label == "İşlemci Tipi"):
                islemci_tipi = urun_data
                #print(urun_data)
            elif (urun_label == "İşletim Sistemi"):
                isletim_sistemi = urun_data
                #print(urun_data)
            elif (urun_label == "Ram (Sistem Belleği)"):
                ram = urun_data
                #print(urun_data)
            elif (urun_label == "İşlemci Nesli"):
                islemci_nesli = urun_data
                #print(urun_data)
            elif (urun_label == "Ekran Boyutu"):
                ekran_boyutu = urun_data
                #print(urun_data)
            elif (urun_label == "İşlemci Modeli"):
                model_no = urun_data
                #print(urun_data)
            elif (urun_label == "SSD Kapasitesi"):
                disk = urun_data
                #print(urun_data)
            else:
                continue
            site_ismi = "TRENDYOL"
            #print("{} : {}".format(urun_label,urun_data))
        print(marka)
        print(urun_adi)
        print(urun_fiyati)

        c.execute("""INSERT INTO c VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""", (marka,urun_adi,model_no,isletim_sistemi,islemci_tipi,islemci_nesli,ram,disk,ekran_boyutu,puani,urun_fiyati,site_ismi,link))
        conn.commit()
        c.execute("""SELECT * FROM c""")
        results = c.fetchall()
        print(results)




