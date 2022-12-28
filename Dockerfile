FROM centos:7
version="1.0.0"

ENV LC_ALL "zh_CN.UTF-8"


COPY requirements.txt /
RUN python3 -m pip install -r /requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 5000
CMD [ "python" , "app.py"]
