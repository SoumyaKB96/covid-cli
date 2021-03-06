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
            break    
              
    
data_int = requests.get("https://api.covid19api.com/summary")


    
def case2():
 dat = data_int.json()["Global"]
 for i in dat:
    print(i,"\t", dat[i])

  
def cont_case(key):
    dat = data_int.json()["Countries"]

    for i in dat:
        if(key == i["Country"]):
            for x in i:
                print(x, "\t", i[x])
            break    

def help():
    print("Usage:")
    print("---------")
    print(" -t  \t \t displays data for India")
    print(" -s [State] \t displays data for the states of India")
    print(" -i  \t \t displays data for world total")
    print(" -i [Country] \t displays data for entered country")
    print(" -h  \t \t help")

help()