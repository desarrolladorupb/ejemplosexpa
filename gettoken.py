'''
Created on 9 mar. 2017

@author: julian
'''
import re, requests


def GET_TOKEN( email=None, password=None ):
    if email and password:
        AUTH = {
            "user[email]":email,
            "user[password]":password
        }
        r = requests.post("https://auth.aiesec.org/users/sign_in", data=AUTH, verify=False)
        return r.history[-1].cookies["expa_token"]
    else:
        r = requests.get("https://opportunities.aiesec.org/js/1.0.0.op.js", verify=False).text
        return re.search(r'["\']?access_token["\']?:"(.*?)"', r).group(1)

if __name__=="__main__":
    print ("PUBLIC TOKEN ", GET_TOKEN("julian.estrada2@aiesec.com","Jupiter1026"))