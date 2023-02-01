import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium. common. exceptions import TimeoutException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

listemm = []
for sayfa in range(1,2):
    response = "https://www.trendyol.com/laptop-x-c103108?pi={}".format(sayfa)
    soup = BeautifulSoup(requests.get(response).content, "lxml")
    bir = soup.find_all("div", attrs={"class ", "p-card-chldrn-cntnr"})
    time.sleep(0.01)
    for st in bir:
        link = ("https://www.trendyol.com" + st.find_all('a')[0].get("href"))
        #browser = webdriver.Chrome("/Users/canoncu/Documents/chromeWeb/chromedriver")
        respond1 = requests.get(link)
        soup1 = BeautifulSoup(respond1.content, "lxml")
        try:
            Marka = soup1.find_element_by_xpath(
                "//*[@id='product-detail-app']/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/h1/a").text
        except:
            Marka = "Markası Belirtilmemiş"
        try:
            Telefon_İsmi = soup1.find_element_by_xpath(
                "//*[@id='product-detail-app']/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/h1/span").text
        except:
            Telefon_İsmiİsmi = "İsim Belirtilmemiş"
        try:
            değerlendirme = soup1.find_element_by_xpath(
                "//*[@id='product-detail-app']/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div/a").text
        except:
            değerlendirme = "Henüz Değerlendirilmemiş"
        try:
            kargo = soup1.find_element_by_xpath(
                "//*[@id='product-detail-app']/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]").text
        except:
            kargo = "KARGO YOK"
        try:
            indirim_oranı = soup1.find_element_by_xpath(
                "//*[@id='product-detail-app']/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]").text
        except:
            indirim_oranı = "İndirimsiz"

        try:
            Fiyat = soup1.find_element_by_xpath(
                "//*[@id='product-detail-app']/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[3]/div/div/div[3]/div[2]/span").text
        except:
            Fiyat = "Fiyatı Belirtilmemiş"
        try:
            Satıcı_Puanı = soup1.find_element_by_xpath(
                "//*[@id='product-detail-app']/div/div[2]/div[2]/div[2]/div[2]/div/a/div").text
        except:
            Satıcı_Puanı = "Puan Yok"
        try:
            Müşteri_Puanı = soup1.find_element_by_xpath(
                "//*[@id='product-detail-app']/div/div[7]/div[2]/div[1]/div/div[1]/span").text
        except:
            Müşteri_Puanı = "Müşteri Puanı Yok"
        try:
            c = 2
            telefonn_özellikleri = []
            while c < 90:
                telefonun_özellikleri = soup1.find_element_by_xpath(
                    "//*[@id='urun-ozellikleri']/div[2]/div[" + str(c) + "]/div[2]").text
                telefonn_özellikleri.append(telefonun_özellikleri)
                c += 2
        except:
            pass
        time.sleep(2)
        try:
            element = soup1.find_element_by_css_selector(
                '#product-detail-app > div > div.pr-rnr-w > div.pr-rnr-cn.gnr-cnt-br > div.pr-rnr-com-w > a')
            soup1.execute_script("arguments[0].click();", element)
        except:
            pass
        try:
            q = 1
            yorumlarr = []
            while q < 60:
                kullanıcı_yorumları = soup1.find_element_by_xpath(
                    "//*[@id='rating-and-review-app']/div/div[2]/div/div[2]/div[3]/div[2]/div[" + str(
                        q) + "]/div[1]/div").text
                kullanıcı_yorumlarım = kullanıcı_yorumları + "//"
                yorumlarr.append(kullanıcı_yorumlarım)
                q += 2

            soup1.quit()
        except:
            pass
        listemm.append(
            [link, Marka, Telefon_İsmi, değerlendirme, kargo, indirim_oranı, Fiyat, telefonn_özellikleri, Satıcı_Puanı,
             Müşteri_Puanı, yorumlarr])

   # sy += 2
#pd.DataFrame(listemm,columns=["link","marka","model","değerlendirme","kargo","indirim","fiyat","telefonn_özellikleri","satıcı_puanı",
                              #"müşteri_puanı","yorumlarr"])