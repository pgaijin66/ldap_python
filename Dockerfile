FROM python:3.7

ADD src /app
WORKDIR /app
RUN apt-get update && apt-get install -y python-dev libldap2-dev libsasl2-dev libssl-dev
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "main.py" ]