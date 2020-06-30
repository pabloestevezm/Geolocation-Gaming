import re
import requests
import numpy as np



def total_funds(x):
    crry = {'CAD': 0.73, '€': 1.13, '£': 1.23}
    abrv = {'K': 1000, 'M': 1000000, 'B': 100000000000}
    val = float(re.search('[+-]?([0-9]*[.])?[0-9]+', x)[0])
    if x.endswith('B'):
        total = val*(abrv['B'])
    elif x.endswith('K'):
        total = val*(abrv['K'])
    elif x.endswith('M'):
        total = val*(abrv['M'])
    elif x.startswith("C"):
        total = val*(crry['CAD'])
    elif x.startswith("€"):
        total = val*(crry['€'])
    elif x.startswith("£"):
        total = val*(crry['£'])
    else:
        total = val
    return int(total)


def transformToGeoPoint(s):
    if np.isnan(s.latitude) or np.isnan(s.longitude):
        return np.nan
    return {
        "type":"Point",
        "coordinates":[s.longitude, s.latitude]
    }



def geocode(address):
    try:
        res = requests.get(f"https://geocode.xyz/{address}", params={"json":1})
        data = res.json()
        data
        return {
            "type":"Point",
            "coordinates":[float(data["longt"]),float(data["latt"])]
        }
    except Exception:
        raise ValueError("error")
        return None


def getLoc(long, lat):
    loc = {
        'type': 'Point',
        'coordinates': [long, lat]
    }
    return loc

def f_address(x):
    full_address = x['Street Address']+" "+x['City']
    return full_address




def geoQueryNear(point,radius=10000):
    return {
        "geopoint":{
            "$near": {
                "$geometry": point,
                "$maxDistance": radius,
                "$minDistance": 0
            }
        }
    }

