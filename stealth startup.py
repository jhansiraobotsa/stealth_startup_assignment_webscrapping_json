import requests
from bs4 import BeautifulSoup
import json
url=input("enter your url :")
r=requests.get(url)
soup=BeautifulSoup(r.text,'lxml')
#print(soup)
divs=soup.find_all("div")
text=[]
result=[]
for i in divs:
    text.extend(i.text.split())
for i in text:
    if i not in result:
        result+=[(i,text.count(i))]
output=dict(result)
#print(len(output))
#def main():
#   url=input('enter the url of a static website: ')
file=input("enter file name with extension : ")
with open(file,'w') as f:
    json.dump(output,f)
print('successfully added data to your file.......')


