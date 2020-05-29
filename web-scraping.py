import requests
from bs4 import BeautifulSoup

site =requests.get("https://sondakika.haberler.com")

#200 alıyorsak verileri alrıız
#print(site.content)

jobs = site.content

soup = BeautifulSoup(jobs,"html.parser")

#print(soup.title)
#find ile etiketleri alabilirizdatetime A combination of a date and a time. Attributes: ()

#haber = soup.find("h2".text)

"""

din ile tek div etiketi
find_all ile bütün div etiketlerini çağırıırız
soup.find("div"))

soup.find_all("div"))

"""
#p etiketlerini al
#print(soup.find_all("p"))

"""
class lı a etiketi

print(soup.find_all("a"),{"class":"hblnTitle"})
"""
#all_jobs =(soup.find_all("p",))

all_jobs =soup.find_all("div",{"class":"hblnContent"})
all_jobs2 =soup.find_all("a",{"class":"hblnTitle"})
    
#print(all_jobs)

for job in all_jobs:   
    #a etiketinin başlığını almak için.
    print(job.a.text)
    #a etiketinin başlığında yer alan haberin özetini almak için.
    print(job.p.text)
    print("\n***************\n")
    
 






