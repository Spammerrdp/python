import folium
import requests
from ip2geotools.databases.noncommercial import DbIpCity
import socket
def printDetails(ip):
    res = DbIpCity.get(ip, api_key="free")
    print(f"IP Address: {res.ip_address}")
    print(f"Location: {res.city}, {res.region}, {res.country}")
    print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")
    lo = folium.Map(location=[res.latitude,res.longitude])
    folium.Marker([res.latitude,res.longitude]).add_to(lo)
    lo.save("location.html")
k = requests.get("https://api.ipify.org").text
#or
# k = socket.gethostbyname("www.google.co.in")
printDetails(k)
