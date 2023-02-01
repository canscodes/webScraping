#N11
from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
import sqlite3
import datetime

conn = sqlite3.connect("son4.db")
c = conn.cursor()
#c.execute("""CREATE TABLE c(marka TEXT,urun_adi TEXT,model_no TEXT,isletim_sistemi TEXT,islemci_tipi TEXT,islemci_nesli TEXT,ram TEXT,disk TEXT,ekran_boyutu TEXT,puani TEXT,urun_fiyati TEXT,site_ismi TEXT,link TEXT)""")
for sayfa in range(1,2):
    response = "https://www.n11.com/bilgisayar/dizustu-bilgisayar?ipg={}".format(sayfa)
    soup = BeautifulSoup(requests.get(response).content, "lxml")
    veri = soup.find("div", attrs={"class": "productArea"}) \
        .find_all("li",attrs={"class":"column"})
    for urun in veri:
        link = urun.a.get("href")
        #print(link)
        respond1 = requests.get(link)
        soup1 = BeautifulSoup(respond1.content, "lxml")
        urun_adi = soup1.find("div", attrs={"class": "nameHolder"}).text.strip().replace("\n", "")
        urun_fiyati = soup1.find("div", attrs={"class": "unf-p-summary-price"}).text.strip().replace("\n", "")
        try:
            puani = soup1.find("div", attrs={"class": "avarageText"}).text
        except:
            puani = "0"
        #print(urun_adi)
        #print(puani)
        #print(urun_fiyati)
        ozellikler = soup1.find_all("li", attrs={"unf-prop-list-item"})
        for ozellik in ozellikler:
            #print(ozellik.find("p", attrs={"class": "unf-prop-list-title"}).text)
            #print(ozellik.find("p", attrs={"class": "unf-prop-list-prop"}).text)
            urun_label = ozellik.find("p", attrs={"class": "unf-prop-list-title"}).text
            urun_data = ozellik.find("p", attrs={"class": "unf-prop-list-prop"}).text
            if (urun_label == "İşlemci"):
                islemci_tipi = urun_data
                # print(urun_data)
            elif (urun_label == "İşletim Sistemi"):
                isletim_sistemi = urun_data
                # print(urun_data)
            elif (urun_label == "Bellek Kapasitesi"):
                ram = urun_data
                # print(urun_data)
            elif (urun_label == "İşlemci Modeli"):
                islemci_nesli = urun_data
                #print(islemci_nesli)
            elif (urun_label == "Ekran Boyutu"):
                ekran_boyutu = urun_data
                #print(ekran_boyutu)
            elif (urun_label == "Model"):
                model_no = urun_data
                # print(urun_data)
            elif (urun_label == "Disk Kapasitesi"):
                disk = urun_data
                # print(urun_data)
            elif (urun_label == "Marka"):
                marka = urun_data
                print(marka)
            else:
                continue
            site_ismi = "N11"


            #print("{} : {}".format(urun_label,urun_data))

        c.execute("""INSERT INTO c VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""", (marka,urun_adi,model_no,isletim_sistemi,islemci_tipi,islemci_nesli,ram,disk,ekran_boyutu,puani,urun_fiyati,site_ismi,link))
        conn.commit()
        c.execute("""SELECT * FROM c""")
        results = c.fetchall()
        print(results)