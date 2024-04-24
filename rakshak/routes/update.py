from flask import Flask, render_template, request, session,jsonify
from rakshak import app,sock
import os
import time
from rakshak.nlppipeline.ner import get_person_name_and_location,old_ner
from rakshak.nlppipeline.zeroshot import give_type_of_emergency,give_priority
from rakshak.dbcalls.update import updates_one
from bson import ObjectId

@app.route('/update', methods=['POST'])
def update():
    data = request.get_json()
    filter_query = {"_id": ObjectId(data["data-id"])}
    status_query = {"call_priority": data["call_priority"]}
    print(updates_one(filter_query,status_query))

    return "hello"