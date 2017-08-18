#!/usr/bin/env python
# -*- coding: utf-8 -*-

from slackclient import SlackClient
import time
from datetime import datetime
import os
from ConfigParser import SafeConfigParser

import urllib3
urllib3.disable_warnings()


parser = SafeConfigParser()
parser.read('config.ini')

BOT_ID = parser.get('slackbotapp', 'BOT_ID')
BOT_USERNAME = parser.get('slackbotapp', 'BOT_USERNAME')
SLACK_BOT_ID = parser.get('slackbotapp', 'SLACK_BOT_ID')
SLACK_TOKEN = parser.get('slackbotapp', 'SLACK_TOKEN')

sc = SlackClient(SLACK_TOKEN)

def parse_message(slack_rtm_message):
    output_list = slack_rtm_message
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and BOT_ID in output['text'] \
                    and output['user'] is not SLACK_BOT_ID:  # check if bot was called
                return output['text'].encode('utf8'), output['channel'], output['user']
    return None, None, None


def send_response(msg_type, text):
    if msg_type == "message":
        sc.api_call("chat.postMessage", channel=channel,
                    as_user=False,
                    username=BOT_USERNAME,
                    text=text)

    if msg_type == "button":
        sc.api_call("chat.postMessage", channel=channel,
                    as_user=False,
                    username=BOT_USERNAME,
                    text=text,
                    attachments=[
                        {
                            "text": "Elige cuando le vamos a poner...",
                            "fallback": "No se puede enviar",
                            "callback_id": "wopr_game",
                            "color": "#3AA3E3",
                            "attachment_type": "default",
                            "actions": [
                                {
                                    "name": "manana",
                                    "text": "Mañana?",
                                    "type": "button",
                                    "value": "manana"
                                },
                                {
                                    "name":"hoy",
                                    "text":"Hoy?",
                                    "type":"button",
                                    "value":"hoy"
                                }
                            ]
                        }
                    ])


def handle_response(text, channel, user):

    if ("ayudame") in text:
        send_response(msg_type="message", text="¿Aún no conoces los comandos y opciones? No hay problema, aquí están:\n- Crea Evaluación\n- Modifica Evaluación")
        
    if ("a q hora tomamos") in text:
       send_response(msg_type="message", text="A las 22:00hrs en el bunker")

    if ("dime la hora" or "que hora es") in text:
        send_response(msg_type="message",
                      text="Son las {0}".format(str(datetime.now())))

    if ("como estas?" or "como estas" or "como estás?") in text:
        send_response(msg_type="message", text="Estoy super bien")

    if("vamos a tomar?") in text:
        send_response(msg_type="message", text="Vamos a ponerle a cagar")

    if("sus piscolas") in text:
        send_response(msg_type="message", text="vamos perro yo me rajo")

    if("vamos a tomar chela?") in text:
        send_response(msg_type="button", text="Cuando vamos perrin?")
    
    if("testing buttons") in text:
        send_response(msg_type="button", text="mensaje de prueba")

if __name__ == "__main__":

    try:
        sc.rtm_connect()  # connect to a Slack RTM websocket
        while True:
           # read all data from the RTM websocket
            text, channel, user = parse_message(sc.rtm_read())
            if text is not None and channel is not None:
                handle_response(text, channel, user)
                time.sleep(1)
    except Exception as e:
        print e