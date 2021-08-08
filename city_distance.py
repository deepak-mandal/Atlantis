# -*- coding: utf-8 -*-
"""
Assignment 3:
Write a python class that is able to return the flight distance between two cities given their
latitude and longitude coordinates.
Expected output:
$ python city_distance.py
> City 1: 51.5074 N, 0.1278 W
> City 2: 48.8566 N, 2.3522 E
> Output: City 1 and City 2 are 342.87 km apart
"""
from math import sin, cos, sqrt, atan2, radians


class Distance:
    def __init__(self, lat_1, lon_1, lat_2, lon_2):
        self.lat1=lat_1
        self.lon1=lon_1
        self.lat2=lat_2
        self.lon2=lon_2
        
    def flightDistance(self):
        R=6371      #Radius of earth in km 
        
        self.lat1 = radians(self.lat1)
        self.lon1 = radians(self.lon1)
        self.lat2 = radians(self.lat2)
        self.lon2 = radians(self.lon2)
        
        #Haversine Formula that will calculate the flight distance between two cities given their latitude and longitude coordinates. 
        dLon=self.lon2 - self.lon1
        dLat=self.lat2 - self.lat1
        
        a = sin(dLat / 2)**2 + cos(self.lat1) * cos(self.lat2) * sin(dLon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c
        
        return distance
    


if __name__=="__main__":
    city1=input("(eg. City 1: 51.5074 N, 0.1278 W) Enter City 1: ")
    city2=input("(eg. City 2: 48.8566 N, 2.3522 E) Enter City 2: ")
    City1= city1.strip().split()
    City2=city2.strip().split()
    #print(City1)
    #print(City2)
    """
    Implementing convention:
        W(-)
        E(+)
        S(-)
        N(+)
        """
        
    if City1[1]=="W," or City1[1]=="W" or City1[1]=="S," or City1[1]=="S":
        City1[0]= -float(City1[0])
    elif City1[3]=="W," or City1[3]=="W" or City1[3]=="S," or City1[3]=="S":
        City1[2]= -float(City1[2])
    elif City2[1]=="W," or City2[1]=="W" or City2[1]=="S," or City2[1]=="S":
        City2[0] = -float(City2[0])
    elif City2[3]=="W," or City2[3]=="W" or City2[3]=="S," or City2[3]=="S":
        City2[2] = -float(City2[2])
        
    lat_1=float(City1[0])
    lon_1=float(City1[2])
    lat_2=float(City2[0])
    lon_2=float(City2[2])
    
    result=Distance(lat_1, lon_1, lat_2, lon_2).flightDistance()
    print("City 1 and City 2 are {:.2f} km apart".format(result))







