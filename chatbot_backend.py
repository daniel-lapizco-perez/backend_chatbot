import os
import openai

openai.api_key = "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"

def chatbot(): 

    messages = [
        {"role": "system", "content": "Crea tus tickets de manera rápida con IA"},
    ]

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

if __name__ == "__main__":
    print ("Crea un ticket con IA")
    chatbot()