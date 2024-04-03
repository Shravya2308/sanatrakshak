import requests
import json
from transformers import AutoTokenizer, AutoModelForTokenClassification
def get_person_name_and_location(text):
    url = "https://ai4bharat-indicner.hf.space/run/predict"

    payload = json.dumps({
    "data": [
        text
    ]
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    ner_predictions = response.json()['data']

    person_name = ""
    location = ""
    print(ner_predictions)
    for sentence in ner_predictions:
        for i,(word, tag) in enumerate(sentence):
            if tag == 'B-PER' or tag == 'I-PER':
                person_name = "caller"
            elif tag == 'B-LOC':
                location = location + word
                if i < len(sentence) - 1:
                    next_tag = sentence[i + 1][1]
                    if next_tag == 'I-LOC' or next_tag == 'O':
                        location = location + " "+ sentence[i+1][0]


    return person_name,location

def old_ner(text):
    
    # old ner may come here
    from transformers import pipeline
    tokenizer = AutoTokenizer.from_pretrained("Davlan/distilbert-base-multilingual-cased-ner-hrl")
    model = AutoModelForTokenClassification.from_pretrained("Davlan/distilbert-base-multilingual-cased-ner-hrl")
    nlp = pipeline("ner", model=model, tokenizer=tokenizer)
    ner_results = nlp(text)
    print(ner_results)

    array = []
    for i in range(0, len(ner_results)):
     if ner_results[i]['entity']=='B-LOC' or ner_results[i]['entity']=='I-LOC':
             array.append((ner_results[i]['word']))
             print(array)

    nlp_string = ""
    for i in range(0,len(array)):
        nlp_string=nlp_string + array[i]
        print(nlp_string)

    nlp_newstr = nlp_string.replace('#','')
    print(nlp_newstr)
    return nlp_newstr
# get_person_name_and_location("My name is Soham. I'm stuck at the thane station.")
