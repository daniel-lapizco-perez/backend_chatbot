import os
import openai
from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)


openai.api_key = "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"

messages = [
        {"role": "user", "content": "¿Puedes responder como si fueras un agente de service desk y estás recopilando información para generar tickets que después va a revisar un técnico?Intenta recopilar la información con pocas preguntas, como si fuera una conversación"},
    ]

def chatbot(): 

    while True:
        message = input("Usuario: ")

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

@app.route("/")
def index():
    return "200"

@socketio.on('message')
def handle_message(message):
    user_message = message['data']

    # Call OpenAI's API to get the chatbot's response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages.append({"role": "user", "content": user_message})
        temperature=0.7,
        max_tokens=100
    )

    bot_reply = response['choices'][0]['message']['content']
    messages.append({"role": "assistant", "content": bot_reply})

    emit('bot_response', {'data': bot_reply})

    # Se terminó de generar el ticket
    # Recopilar los datos: 
    #     title = data.get('title')
    #     description = data.get('description')
    #     author = data.get('author')
    #     assigned = data.get('assigned')
    #     area = data.get('area')
    #     created = data.get('created')
    #     modified = data.get('modified')
    #     status = data.get('status')
    # ejemplo:
    #     {
    #       "title": "Otro gato",
    #       "description": "Una prueba medio corta",
    #       "author": "jGH8r5F6WONvyXW3eagExiSTJJ22",
    #       "assigned": "",
    #       "area": "",
    #       "created": "2023-10-01T22:45:36.303+00:00",
    #       "modified": "2023-10-01T22:45:36.303+00:00",
    #       "status": "open"
    #      }
    # Hacer post request a http://172.174.216.130:5000/ticket_post

if __name__ == '__main__':
    socketio.run(app)