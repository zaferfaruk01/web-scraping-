# Web Scraping Nedir?

Web scraping yani veri kazıma işlemi Web sitelerinden veri çıkarma işlemidir.
Web scraping ile web üzerinde bulunan birçok veriyi toplama işlemini otomatikleştirir.İnternet'ten kazınan verilerle birçok işlem yapabiliriz.

Web sayfalarının yapısı biçimlendirme dilleri ile oluşturulmuştur, bunların en popüleri HTML dir.
HTML ile ayrıştırma yaparak web scraping aşamasına başlıyabiliriz.

# Beautiful Soup Kütüphanesi
Web sayfalarından bilgi kazımayı kolaylaştıran kütüphanedir. 
Bu kütüphane sayesinde web sitesindeki HTML kodlarını ayrıştırıp sadece istediğimiz alanları elde etmemizi sağlar.

## Kurulum
pip3 python3 için paket yöneticisi.

pip3 ile yüklemek için ilk olarak pip3 e sahip olmanız gerekir.
###### sudo apt-get install python3-pip

Beautiful Soup indirmek için:
###### pip3 install beautifulsoup4

projemize dahil etmek için:
###### from bs4 import BeautifulSoup

Websitesinin HTML kodlarını almak için:
###### import requests


