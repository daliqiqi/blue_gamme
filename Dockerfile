FROM tensorflow/tensorflow:2.5.1

COPY requirements.txt /
RUN  pip3 install -r /requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 5000
CMD [ "python" , "app.py"]
