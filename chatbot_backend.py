import os
import openai
from datetime import datetime
from flask import Flask
from flask_socketio import SocketIO
import requests
import json


app = Flask(__name__)
socketio = SocketIO(app)

openai.api_key = "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"
messages = [
    {"role": "system", "content": "Crea tus tickets de manera rápida con IA"},
]

@app.route("/")
def index():
    return "200"

def chatbot(): 
    ticket = {"title": [], "description": [], "author": [""], "assigned":[""], "area": [], "creation": [], "modified": [], "status": ['Abierto']}
   
    #mensaje inicial
    input_title = input("Titulo de ticket: ")
    ticket["title"].append(input_title)

    #Input de descripcion
    input_description = input("¿Cuál es el problema que está presentando?: ")
    ticket["description"].append(input_description)

    #Input de tipos
    print("1. Hardware \n2. Software \n3. Periféricos \n4. Solicitud de equipo(periféricos)")
    input_area = input("Seleccione una área especifica donde esté pasando su problema de la lista de arriba: ")
    ticket["area"].append(input_area)

    #obtener fecha y hora actual
    moded_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ticket["creation"].append(str(moded_time))
    ticket["modified"].append(str(moded_time))
    print(ticket)


    print("¿Qué desea hacer con la información previamente proporcioanda? \nAbrir un ticket o continuar")

    while True:
        
        message =  input("Usuario: ")
        if message.lower() == "quit":
            break

        messages.append({"role": "user", "content": message})

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        chat_message = response.choices[0].message.content
        print(f"Help Desk ChatBot: {chat_message}")
        messages.append({"role": "assistant", "content": chat_message})

    post_ticket(ticket)
    
    return ticket

def post_ticket(ticket):
    url = "http://172.174.216.130:5000/ticket_post"

    headers = {'Content-Type': 'application/json'}

    moded_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = {
        "title" : ticket['title'][0],
        "description": ticket['description'][0],
        "area": ticket['area'][0],
        "status": ticket['status'][0],
        "percentage": "0",
        "created": moded_time,
        "modified": moded_time,
        "author": ticket['author'][0],
        "assigned": ticket['assigned'][0]
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        print(f'Solicitud exitosa: {response.text}')
    except requests.exceptions.RequestException as e:
        print('Error: ', e)

if __name__ == "__main__":
    print ("Crea un ticket con IA")
    chatbot()