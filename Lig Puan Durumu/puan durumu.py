from bs4 import BeautifulSoup
import requests
html_text=requests.get("https://www.tff.org/default.aspx?pageID=198").text
soup=BeautifulSoup(html_text,'lxml')
sıralama=soup.find_all('table', attrs={"width":"100%", "border":"0", "cellpadding":"1" ,"cellspacing":"1"})
sıralama2=BeautifulSoup(str(sıralama),'lxml')
sıralama3=sıralama2.find_all('b')
sıralama4=BeautifulSoup(str(sıralama3),'lxml')
sıralama5=sıralama4.find_all('a')
for ch in sıralama5:
    print(ch.text)
input()