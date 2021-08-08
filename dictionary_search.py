# -*- coding: utf-8 -*-
"""
Assignment 2:
Write a python class that is able to return the meaning of an English language word provided to
it in the terminal. (Use https://dictionaryapi.dev/)
Expected output:
$ python dictionary_search.py
> Word? <user inputs the word “House”>
> Output: House. Noun. A building for human habitation, especially one
that is lived in by a family or small group of people.
"""
#url="https://api.dictionaryapi.dev/api/v2/entries/en_US/hello"

import requests
import bs4
import json


class Dictionary:
    def __init__(self, word):
        self.word=word
        
    def search(self):
        #https://api.dictionaryapi.dev/api/v2/entries/<language_code>/<word>
        url="https://api.dictionaryapi.dev/api/v2/entries/en_US/"
        
        url+=word
        data = requests.get(url)
        #creating soup object
        soup = bs4.BeautifulSoup(data.text, 'html.parser')
        #print(soup.prettify())        
        
        jsonStr = soup.text        
        aList = json.loads(jsonStr)
        
        for x in aList:
            #print(x["word"])
            #print(type(x["meanings"]))
            i=1
            print("Output: the meaning of an English language word is as following:- ")
            for arrEle in x["meanings"]:
                #print(arrEle["definitions"])
                #print(arrEle)
                #print(type(arrEle["definitions"]))
                #print(arrEle["definitions"][0])
                #print(type(arrEle["definitions"][0]))
                finalOut=arrEle["definitions"][0]
                print("[{}]. {} ".format(i, finalOut["definition"]))
                i+=1
        
            

if __name__=="__main__":
    word=input("Word?: ").strip()
    try:
        Dictionary(word).search()
    except Exception:
        print("Not Found!")
    





