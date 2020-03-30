from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon= "F:\\udemy\\python\\desktop-notification\\icon1.ico",
        timeout=6
    )
def getData(url):
    r=requests.get(url)
    return r.text

if __name__== "__main__":
    # notifyMe("Neetesh", "Lets stop the spread of this virus together")
    while True:
        myHtmlData=getData("https://www.mohfw.gov.in/")
        # print(myHtmlData)

        soup= BeautifulSoup(myHtmlData,'html.parser')
       # print(soup.prettify())
        myDtaStr=""
        for tr in soup.find_all('tbody')[1].find_all('tr'):
            # print(soup.get_text())
            myDtaStr += tr.get_text()
        myDtaStr =myDtaStr[1:]
        itemList=myDtaStr.split("\n\n")
        
        # states = ['Uttar Pradesh','Karnataka']
        
        for item in itemList[0:23]:
            dataList=item.split('\n')
            print(dataList[1])
            if dataList[1] in dataList[1]:
                # print(dataList)
                nTitle='Cases of covid-19' 
                nText =f"State  {dataList[1]}\n Indian: {dataList[2]}\n Forein:{dataList[3]}\n  Cured: {dataList[4]}  Death: {dataList[5]}"
                notifyMe(nTitle,nText)
                time.sleep(2)
        time.sleep(3600)