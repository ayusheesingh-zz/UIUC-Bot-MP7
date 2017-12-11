#!/usr/bin/env python

from pymessenger import Bot
from flask import Flask, request
import json
import os
import sys
import witlib

app = Flask(__name__)
# token for facebook page
bot = Bot("EAAbwYM5CtuwBANUIGgDScEqkJBYgZBd9K2tGqndPRhZAeWZC5jXv7U4FVABxZBGZCfKGmT0HoHUlK2WY0fIpRc4EHCHPuTNrHZA7BkOiegZAqJsrXt7oTLPniWlXoLHARskJGfwjFKPtdZA3REfe5vsvpvK0wm6fehTteBLYdSoPYWsFrD0VZAglK")
# wit access token
wit = witlib.WitAdapter("S5PPAUKICHKPQASRGIJ5BFEYJF7BPXWB")
wit = witlib.WitAdapter("ZGTJG7FCVEHPF6JDPXL222BHQTW6MNAY")

@app.route('/', methods=['GET'])
def authenticate():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if request.args.get("hub.verify_token") != "ayushics125mp7":
            return "authentication failed", 403
        # send back the challenge only if token matches
        return request.args["hub.challenge"], 200
    # if someone goes to the root URL, return this text
    return "Ayushi's Chatbot for MP7", 200

@app.route('/', methods=['POST'])
def respond():
    data = request.get_json()

    if data["object"] == "page":
        for entry in data["entry"]:
            for event in entry["messaging"]:
                if event.get("message") and event["message"].get("text"):
                    print("Got request", json.dumps(data, indent=2))
                    if event["message"].get("is_echo") and event["message"]["is_echo"]:
                        continue
                    message = event["message"]["text"]
                    bot.send_text_message(event["sender"]["id"], wit.response(message))

    return "ok", 200

if __name__ == "__main__":
    app.run(debug=True, port=9191)
