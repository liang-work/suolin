import requests
import readFile

DOMAIN = readFile.LoadJson("config.json").get("APIdomain","https://api.solian.app")

def requests_API(url:str,method:str="GET",params:dict={},data:dict={},headers:dict={}):
    if method == "GET":
        return requests.get(url,params=params,headers=headers)
    elif method == "POST":
        return requests.post(url,params=params,data=data,headers=headers)
    elif method == "PATCH":
        return requests.patch(url,params=params,data=data,headers=headers)
    elif method == "DELETE":
        return requests.delete(url,params=params,headers=headers)
    else:
        return None
    
##login changellenge
def create_challenge(username:str):
    api_url = f"{DOMAIN}/api/v1/auth/challenge/{username}"
    response = requests_API(api_url,method="GET")
    return response

##chat

##realms

##user profile

##solarnetwork drive

