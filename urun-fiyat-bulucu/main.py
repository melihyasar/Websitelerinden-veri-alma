from bs4 import BeautifulSoup
import requests
class urun_b:
  def __init__(self,urun_bilgileri):
      self.urun_adi=urun_bilgileri[0]
      self.urun_fiyatı=urun_bilgileri[1]
      self.para_birimi=urun_bilgileri[2]
      self.urun_detay=urun_bilgileri[3]
def urun_bul(urun):
    m=0
    d={}
    html_text=requests.get("https://www.n11.com/arama?q="+urun).text
    soup=BeautifulSoup(html_text,'lxml')
    content=soup.find_all('div',attrs={'class':'productArea'})
    if content == []:
        return "ürün bulunamadı"
    soup=BeautifulSoup(str(content),'lxml')
    content=soup.find_all('div',attrs={'id':'view'})
    soup=BeautifulSoup(str(content),'lxml')
    content=soup.find_all('ul',attrs={'class':'clearfix'})
    soup=BeautifulSoup(str(content),'lxml')
    content=soup.find_all('li',attrs={'class':'column'})
    for i in content:
        m=m+1
        #////////////////Ürün adı//////////////////////////////
        ad_soup=BeautifulSoup(str(i),'lxml')
        try:
            unwanted = ad_soup.find('span',attrs={'class':"superBadge"})#REKLAM yazısını kaldırmak için
            unwanted.extract()
        except:
            pass    
        urun_adi=ad_soup.find('h3',attrs={'class':'productName'}).text.strip()
        #////////////////Ürün fiyatı//////////////////////////////
        fiyat_soup=BeautifulSoup(str(i),'lxml')
        fiyat_content=fiyat_soup.find('div',attrs={'class':'proDetail'})
        fiyat_soup=BeautifulSoup(str(fiyat_content),'lxml')
        #///////////////
        unwanted2 = fiyat_soup.find('span',content=True)
        para_birimi=unwanted2.text.strip()
        unwanted2.extract()#para birimini 'fiyat_soup'tan çıkarıp ayrıca bir değişkene atıyor///////
        urun_fiyatı=fiyat_soup.find('ins').text.strip()
        #/////ürün detayları için/////////
        detay_soup=BeautifulSoup(str(i),'lxml')
        urun_detay=detay_soup.find('a',attrs={'class':'plink'})['href']
        d["i"+str(m)]=[urun_adi,urun_fiyatı,para_birimi,urun_detay]
    k={}
    for i in d:
        k[i]=urun_b(d[i])
    return k
a=input("ne arıyorsunuz?")
k=urun_bul(a)
if k=="ürün bulunamadı":
  print("ürün bulunamadı")
else: 
  #k["x"].urun_adi/urun_fiyatı/para_birimi/urun_detay | x aranılan ürünün "kodu"(i1,i2 i5 vs.)
  #k'nın anahtarlarının her biri bir ürünün kodu,anahtarın değeri ise o ürüne ait bilgileri içeren obje
  for i in k:
      print(i[1:]+")",k[i].urun_adi,k[i].urun_fiyatı,k[i].para_birimi)
  dty=input('hangi ürünler ilgili detayları istersiniz?')
  print(k["i"+dty].urun_detay)
input()
    





