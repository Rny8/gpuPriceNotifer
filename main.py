from bs4 import BeautifulSoup
import requests
import time
import smtplib
import os
import json


if os.path.exists(os.getcwd() + "/key.json"):
    with open("./key.json") as f:
        configData = json.load(f)
else:
    configTemplate = {"Password": ""}

    with open(os.getcwd() + "/key.json", "w") as f:
        json.dump(configTemplate, f)


senderEmail = "botneticbots.xyz@gmail.com"
rec_email = "liljedi06@gmail.com"
password = configData["Password"]
message = "Test"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(senderEmail, password)
print("Login worked")





requestS = []
gpuDic = {
    "https://www.newegg.com/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Item=N82E16814932436&cm_sp=Homepage_SS-_-P4_14-932-436-_-08102022": -1,
    "https://www.newegg.com/core-black-msi-gp-series-gp66-leopard-11uh-032-gaming-entertainment/p/N82E16834155852?Item=N82E16834155852&cm_sp=Homepage_SS-_-P2_34-155-852-_-08102022": -1
    
    }

while True:
    for gpu in gpuDic.keys():
        request = requests.get(gpu)
        doc = BeautifulSoup(request.text, "html.parser")
        prices = doc.find_all(text="$")
        parent = prices[0].parent
        strong = parent.find("strong")
        currentPrice = strong.text
        if "," in currentPrice:
            currentPrice = currentPrice.replace(",", "")
            currentPrice = int(currentPrice)
        else:
            currentPrice = int(currentPrice)
        print(f"Price is: ${currentPrice}")
        if currentPrice == gpuDic[gpu]:
            print("Price hasn't changed")
        else:
            print("Price has changed!")
            server.sendmail(senderEmail, rec_email, message)
        gpuDic[gpu] = currentPrice
        
    time.sleep(250)

