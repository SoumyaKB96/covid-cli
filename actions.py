import requests
import json

data = requests.get("https://api.covid19india.org/data.json")



def cases():
 dat=data.json()["cases_time_series"][-1]
 for i in dat:
    if(i=="date"):
        continue 
    print(i,"\t", dat[i])

def state_case(key):
    dat = data.json()["statewise"]

    for i in dat:
        if(key==i["state"]):
            for x in i:
                print(x,"\t", i[x])
              
    
        
    
    



