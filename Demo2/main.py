#VATAN
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

for sayfa in range(1,5):
    response = f"https://www.vatanbilgisayar.com/laptop/?page={sayfa}"
    #response = "https://www.vatanbilgisayar.com/laptop/?page={}".format(sayfa)
    #vatan_web_page = response.text
    soup = BeautifulSoup(requests.get(response).content, "lxml")
    veri = soup.find("div", attrs={"class":"wrapper-product wrapper-product--list-page clearfix"})\
        .find_all("div", attrs={"class":"product-list product-list--list-page"})
    isletim_sistemi ="no"
    for i in veri:
        linksonu = i.a.get("href")
        linkbasi = "https://www.vatanbilgisayar.com/laptop/"
        link = linkbasi + linksonu
        ad = i.find("div",attrs={"class":"product-list__content"}).find("a", attrs={"class":"product-list__link"})\
        .find("div",attrs={"class":"product-list__product-name"}).text
        #print(ad)
        print(link)
        respond1 = requests.get(link)
        soup1 = BeautifulSoup(respond1.content, "lxml")
        urun_adi1 = soup1.find("div", attrs={"class": "product-list__content product-detail-big-price"})
        urun_adi = urun_adi1.find("h1", attrs={"class": "product-list__product-name"}).text.strip().replace("\n","")
        urun_fiyati1 = urun_adi1.find("div", attrs={"class": "product-list__cost product-list__description"})
        urun_fiyati = urun_fiyati1.find("span", attrs={"class": "product-list__price"}).text
        puani = soup1.find("strong", attrs={"id": "averageRankNum"}).text
        site_ismi = "VATAN"
        try:
            model_no1 = soup1.find("div",attrs={"class":"product-list__product-code pull-left product-id"})
            model_no = model_no1.text.strip().replace("\n","")
        except:
            model_no = "36A75-41G-R0162"

            #.find("div", attrs={"class": "col-lg-6 col-md-6 col-sm-12 col-xs-12 property-tab-item masonry-brick"})#\
        #.find("div", attrs ={"product-feature"})#.find("table", attrs={"product-table"})#.find("tr", attrs={"data-count":"0"})

        try:
            marka = soup1.find("a",attrs={"class":"bradcrumb-item"}).text
        except:
            marka = "36A75-41G-R0162"
        print(marka)

        #print(urun_adi)
        #print(urun_fiyati)
        #print(urun_puani)
        #print(model_no)

        #monitor_boyutu = soup1.find("div", attrs={"id": "urun-ozellikleri"}) \
        #.find("table", attrs={"class":"product-table"})
        #tableValues=[]
        #for x in monitor_boyutu.findAll("tr")[1:]:
            #td_tags = x.find_all("td")
            #td_val = [y.text for y in td_tags]
            #tableValues.append(td_val)
            #print(tableValues)
            #for y in x.findAll("td"):
                #print(y.text)
        for z in range(0,14):
            monitor_boyutu = soup1.find("div", attrs={"id": "urun-ozellikleri"}) \
                .findAll('table')[z]
            tableValues = []
            for x in monitor_boyutu.findAll("tr")[1:]:
                listem = ["Windows", "Free Dos", "Windows 11"]
                isletim_sistemi = random.choice(listem)
                td_tags = x.find_all("td")
                td_val = [y.text.strip().replace("\n", "") for y in td_tags]
                # if (td_tags == "Ram (Sistem Belleği)")
                # print("td_val")
                if (td_val[0] == "İşlemci Teknolojisi"):
                    islemci_tipi = td_val[1]
                    print(islemci_tipi)
                    if (islemci_tipi == "M2"):
                        isletim_sistemi = "Mac Os"
                    elif (islemci_tipi == "M1"):
                        isletim_sistemi = "Mac Os"
                    print(isletim_sistemi)
                elif (td_val[0] == "İşletim Sistemi"):
                    isletim_sistemi = td_val[1]
                    print(isletim_sistemi)
                elif (td_val[0] == "İşlemci Nesli"):
                    islemci_nesli = td_val[1]
                    print(islemci_nesli)
                elif (td_val[0] == "Ram (Sistem Belleği)"):
                    ram = td_val[1]
                    print(ram)
                elif (td_val[0] == "Ekran Boyutu"):
                    ekran_boyutu = td_val[1]
                    print(ekran_boyutu)
                # elif (td_val[0] == ""):
                # model_no = td_val[1]
                elif (td_val[0] == "Disk Kapasitesi"):
                    disk = td_val[1]
                    print(disk)
                else:
                    continue


                #tableValues.append(td_val)
            #print(tableValues)
             #print(monitor_boyutu)
        #c.execute("""INSERT INTO c VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""", (marka,urun_adi,model_no,isletim_sistemi,islemci_tipi,islemci_nesli,ram,disk,ekran_boyutu,puani,urun_fiyati,site_ismi,link))
        c.execute("""INSERT INTO c VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""", (marka,urun_adi,model_no,isletim_sistemi,islemci_tipi,islemci_nesli,ram,disk,ekran_boyutu,puani,urun_fiyati,site_ismi,link))
        conn.commit()
        c.execute("""SELECT * FROM c""")
        results = c.fetchall()
        print(results)


