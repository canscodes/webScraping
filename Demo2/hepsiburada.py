#HEPSIBURADA
import selenium
from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
import pymongo
from pymongo import mongo_client
import os
import sqlite3
import datetime
conn = sqlite3.connect("son4.db")
c = conn.cursor()
#c.execute("""CREATE TABLE c(marka TEXT,urun_adi TEXT,model_no TEXT,isletim_sistemi TEXT,islemci_tipi TEXT,islemci_nesli TEXT,ram TEXT,disk TEXT,ekran_boyutu TEXT,puani TEXT,urun_fiyati TEXT,site_ismi TEXT,link TEXT)""")
for sayfa in range(3,5):
    headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15"}
    response = requests.get(f"https://www.hepsiburada.com/laptop-notebook-dizustu-bilgisayarlar-c-98?sayfa={sayfa}",headers=headers)
    soup = BeautifulSoup(response.content, "lxml")
    st1 = soup.find("div", attrs={"class":"productListContent-tEA_8hfkPU5pDSjuFdKG"}).find("div", attrs={"class":"productListContent-pXUkO4iHa51o_17CBibU"})\
        .find_all("li",attrs={"class":"productListContent-zAP0Y5msy8OHn5z7T_K_"})
    list=[]
    site_ismi = "HEPSIBURADA"
    for i in st1:
        linksonu=i.a.get("href")
        linkbasi="https://www.hepsiburada.com"
        link=linkbasi+linksonu
        print(link)
        respond1 = requests.get(link,headers=headers)
        soup1 = BeautifulSoup(respond1.content, "lxml")
        try:
            urun_adi=soup1.find("h1",attrs={"id":"product-name"}).text.strip().replace("\n","")
        except:
            urun_adi="none"
        print(urun_adi)
        try:
            product_price_first = soup1.find("span", attrs={"data-bind": "markupText:'currentPriceBeforePoint'"}).text
            product_price_last = soup1.find("span", attrs={"data-bind": "markupText:'currentPriceAfterPoint'"}).text
            urun_fiyati=product_price_first+","+product_price_last
        except:
            urun_fiyati="none"
        print(urun_fiyati)
        try:
            marka = soup1.find("span", attrs={"class": "brand-name"}).text
        except:
            marka="none"
        print(marka)

        try:
            puani =soup1.find("span", attrs={"class":"hermes-AverageRateBox-module-g3di4HmmxfHjT7Q81WvH"}).text
        except:
            puani= "puanlanmamıs icerik"
        print(puani)
        #product_features = soup1.find("div", attrs={"id":"productTechSpecContainer"})#.text.strip().replace("\n","")
        for g in range(1,3):
            product_features = soup1.find("div", attrs={"id":"productTechSpecContainer"}) \
                .findAll('table')[g]
            tableValues = []
            for x in product_features.findAll("tr")[1:]:
                td_tags = x.find_all("th")
                td_sec =x.find_all("td")
                td_val = [y.text.strip().replace("\n","") for y in td_tags]
                td_val2 = [y.text.strip().replace("\n", "") for y in td_sec]
                if (td_val[0] == "İşlemci Tipi"):
                    try:
                        islemci_tipi = td_val2[0]
                    except:
                        islemci_tipi = "none"
                    print(islemci_tipi)
                elif (td_val[0] == "İşletim Sistemi"):
                    try:
                        isletim_sistemi = td_val2[0]
                    except:
                        isletim_sistemi = "none"
                    print(isletim_sistemi)
                elif (td_val[0] == "Ram (Sistem Belleği)"):
                    try:
                        ram = td_val2[0]
                    except:
                        ram ="none"
                    print(ram)
                elif (td_val[0] == "İşlemci Nesli"):
                    try:
                        islemci_nesli = td_val2[0]
                    except:
                        islemci_nesli ="none"
                    print(islemci_nesli)
                elif (td_val[0] == "Ekran Boyutu"):
                    try:
                        ekran_boyutu = td_val2[0]
                    except:
                        ekran_boyutu ="none"
                    print(ekran_boyutu)
                elif (td_val[0] == "SSD Kapasitesi"):
                    try:
                        disk = td_val2[0]
                    except:
                        disk="none"
                    print(disk)
                elif (td_val[0] == "İşlemci"):
                    try:
                        model_no = td_val2[0]
                    except:
                        model_no ="none"
                    print(model_no)
                else:
                    continue

                #tableValues.append(td_val)
                #res = {td_val[i]: td_val2[i] for i in range(len(td_val))}
                # Printing resultant dictionary

                #print(str(res))
                #a = str(res)
            #print(deneme)
        #print(product_features)
        #list.append([product_name,product_price,product_rate,a])
        #print(list)
#pd.DataFrame(list)
#df=pd.DataFrame(list)
#df.columns={"product_name","product_price","product_rate"}
#df.to_excel("hepsi_laptop.xlsx")

        c.execute("""INSERT INTO c VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""", (marka,urun_adi,model_no,isletim_sistemi,islemci_tipi,islemci_nesli,ram,disk,ekran_boyutu,puani,urun_fiyati,site_ismi,link))
        conn.commit()
        c.execute("""SELECT * FROM c""")
        results = c.fetchall()
        print(results)