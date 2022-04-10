import requests
import time
from bs4 import BeautifulSoup
import os
clear = lambda: os.system('cls')
def dollar_tl():
    html_text=requests.get('https://www.bloomberght.com/doviz/dolar').text
    soup=BeautifulSoup(html_text,'lxml')
    dolar_txt=soup.find_all("span",attrs={"class":"LastPrice downRed"})
    dolar_txt2=soup.find_all("span",attrs={"class":"LastPrice upGreen"})

    if dolar_txt != []:
        for n in dolar_txt:
            return(n.text)

    elif dolar_txt2 != []:
        for n in dolar_txt2:
            return(n.text)
def euro_tl():
    html_text=requests.get('https://www.bloomberght.com/doviz/euro').text
    soup=BeautifulSoup(html_text,'lxml')
    euro_txt=soup.find_all("span",attrs={"class":"LastPrice downRed"})
    euro_txt2=soup.find_all("span",attrs={"class":"LastPrice upGreen"})
    if euro_txt != []:
        for n in euro_txt:
            return(n.text)

    elif euro_txt2 != []:
        for n in euro_txt2:
            return(n.text)
        
class para_birimi:
    def __init__(self,value):
        self.value=value

while True:
    clear()  
    dollar_to_tl=para_birimi(float(dollar_tl().replace(',','.')))
    euro_to_tl=para_birimi(float(euro_tl().replace(',','.')))
    euro_to_dollar=para_birimi(euro_to_tl.value/dollar_to_tl.value)
    dollar_to_euro=para_birimi(dollar_to_tl.value/euro_to_tl.value)
    tl_to_dollar=para_birimi(float(1/dollar_to_tl.value))
    tl_to_euro=para_birimi(float(1/euro_to_tl.value))
    print("dolar-tl: "+str(dollar_to_tl.value))
    print("euro-tl: "+str(euro_to_tl.value))
    print("euro-dolar: "+str(euro_to_dollar.value))
    print("dolar-euro: "+str(dollar_to_euro.value))
    print("tl-dolar: "+str(tl_to_dollar.value))
    print("tl-euro: "+str(tl_to_euro.value))
    time.sleep(120)
    

    
    
    


        

