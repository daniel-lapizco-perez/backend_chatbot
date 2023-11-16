#Tu hermana mejor
FROM python:3-alpine

WORKDIR /chatbot

COPY ./app.py /chatbot/app.py
COPY ./Dockerfile /chatbot/Dockerfile
COPY requirements.txt /chatbot/requirements.txt

RUN pip3 install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]