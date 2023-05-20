from flask import Flask, jsonify, request
from flask_cors import CORS
import openai
import json
import re
import requests

key = "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"



app = Flask(__name__)
CORS(app)

app.route("/")
def home():
    return jsonify({"hello": "welcome to the api"})

@app.route("/essay", methods=['POST'])
#json form = {"essay":___essay____}
def essay():
    content_type = request.headers.get('Content-Type')
    print(content_type)
    if(content_type == "application/json"):

        jso = request.get_json()
        print(jso)

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + key,
            }

        json_data = {
            'model': 'gpt-3.5-turbo',
            'messages': [
                {
                    'role': 'user',
                    'content': "give me feedback on this essay. what can I change in my overallm essage, and can you address grammatical errors and how to fix them. /n " + jso.get("essay"),
                },
            ],
            'temperature': 0.7,
        }
        response = requests.post('https://api.openai.com/v1/chat/completions',headers=headers,json=json_data)
        response = json.loads(response.text)

        t = response.get("choices")[0].get("message").get("content")
        return t
        
    else:
        return "error"

@app.route("/flashcard", methods=['POST'])
def flashcard():
    content_type = request.headers.get('Content-Type')
    if(content_type == "application/json"):

        jso = request.get_json()
        print(jso)

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + key,
            }

        json_data = {
            'model': 'gpt-3.5-turbo',
            'messages': [
                {
                    'role': 'user',
                    'content': "Based on this topic, make flashcards in the form of json code, using front and back as the two labels of the json card, something that I could create an in depth quizlet set on. Include the major subtopics, as well as smaller ones. For the flashcards, add terms and definitions. /n " + jso.get("topic"),
                },
            ],
            'temperature': 0.7,
        }
        response = requests.post('https://api.openai.com/v1/chat/completions',headers=headers,json=json_data)
        response = json.loads(response.text)

        t = response.get("choices")[0].get("message").get("content")
        return t
    else:
        return "error"

@app.route("/notes", methods=['POST'])
def note():
    content_type = request.headers.get('Content-Type')
    if(content_type == 'application/json'):
        json = request.json
        
    else:
        return "error"








if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=False)