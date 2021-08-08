# -*- coding: utf-8 -*-
"""
Assignment 1:
Write a python program to scrape the list of links available in this Github repository
(https://github.com/vinta/awesome-python) and search them by exact name from the console.
Search result should return the github url of the result repository.
Expected output:
$ python search_repos.py
> Query? graphene
> Output: https://github.com/graphql-python/graphene/
The list should be scraped and kept in a runtime variable as soon as the program is initialized..
Handle the error with a suitable error message in case the exact name is not matched from the
list.
"""

#importing libraries
import bs4    #BeautifulSoup
import requests


def searchRepo(Query):
    url = "https://github.com/vinta/awesome-python"
    response = requests.get(url)    #response after sending the url requests

    bs = bs4.BeautifulSoup(response.text, "html.parser")

    Link_list = bs.find_all("a")
    #print(Link_list)

    tempDict={}
    linkArr = []
    for aTag in Link_list:
        try:
            hrefLink = aTag.get("href")
        
            if hrefLink.startswith("/"):
                hrefLink = url[: url.rindex('/')] + hrefLink
                linkArr.append(hrefLink)
            elif hrefLink.startswith("#"):
                hrefLink=url+hrefLink
            else:
                linkArr.append(hrefLink)
            #print(hrefLink)
            #print(aTag.text)
            searchElement=aTag.text.strip()
            tempDict[searchElement]=hrefLink
        except Exception:
            pass    
  
    #print(tempDict)
    try:
        return print("Output: ", tempDict[Query])
    except Exception:
        return print("NOT FOUND!!")


if __name__=="__main__":
    Query=input("[Enter exact name] Query ?: ").strip()
    searchRepo(Query)
    
    



