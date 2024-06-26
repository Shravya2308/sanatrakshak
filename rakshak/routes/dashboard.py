# from flask import Flask, render_template, request, session,jsonify
# from rakshak import app,sock
# import os
# import time
# from rakshak.nlppipeline.ner import get_person_name_and_location
# from rakshak.nlppipeline.zeroshot import give_type_of_emergency,give_priority
# from rakshak.dbcalls.fetchall import fetchall


# @app.route("/dashboard",methods=['POST','GET'])
# def dash():


#     return render_template("dash.html",data=fetchall())
from flask import Flask, render_template, request, session,jsonify
from rakshak import app,sock
import os
import time
from rakshak.nlppipeline.ner import get_person_name_and_location
from rakshak.nlppipeline.zeroshot import give_type_of_emergency,give_priority
from rakshak.dbcalls.fetchall import fetchall
from geopy.geocoders import Bing


@app.route("/dashboard",methods=['POST','GET'])
def dash():

    place_cordinates = []
    data_from_db = fetchall()
    print(data_from_db)
    for i in range(0,len(data_from_db)):
        data_from_db[i]["coordinates"] = get_cordinates_for_map(data_from_db[i]['location'])

    return render_template("dash.html",data=data_from_db)


def get_cordinates_for_map(name):
    print("My nanme is ",name)
    apikey = 'Ao4XIvVIe-m8C-gY4TKD7V0FhTxzf82nIhO6gtSuI8M9kyC3cWypeqdRSG7pY851'
    geolocator = Bing(api_key=apikey, timeout=10)
    geocoded_adr = geolocator.geocode(name)
    print(geocoded_adr.raw['point']['coordinates'])
    return geocoded_adr.raw['point']['coordinates']
    
