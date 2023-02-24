import requests
import json
from bs4 import BeautifulSoup

URL = "https://www.thejakartapost.com/"
page = requests.get(URL) #mengunduh halaman

soup = BeautifulSoup(page.content, "html.parser") #ekstraksi kode html
latest = soup.find(class_="theLatest") #mengambil theLatest

title = latest.find_all("h2", class_="titleNews") #mengambil tag h2 dengan kelas titleNews
category = latest.find_all("span", class_="dt-news") #mengambil tag span dengan kelas dt-news

result = []
for i in range(len(title)):
    result.append({"id":i+1, "judul": title[i].text.strip(), "kategori":category[i].text.strip()})

hasilJSON = json.dumps(result)
JSONFile = open("BeritaTerkini.json", "w")
JSONFile.write(hasilJSON)
JSONFile.close()

