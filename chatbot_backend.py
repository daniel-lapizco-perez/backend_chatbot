import os
import openai

openai.api_key = "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"

def chatbot(): 

    ticket = {"description": [], "area": []}
    messages = [
        {"role": "system", "content": "Crea tus tickets de manera rápida con IA"},
    ]

    input("Usuario: ")
    input_description = input("¿Cuál es el problema que está presentando?: ")
    ticket["description"].append(input_description)
    print("1. Hardware \n2. Software \n3. Periféricos")
    input_area = input("Seleccione una área especifica donde esté pasando su problema de la lista de arriba: ")
    ticket["area"].append(input_area)
    #print(ticket)
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

if __name__ == "__main__":
    print ("Crea un ticket con IA")
    chatbot()