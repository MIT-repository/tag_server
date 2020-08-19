FROM python:3.7
RUN apt-get update
RUN apt install sox -y
RUN apt-get install libsox-fmt-mp3 -y

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . ./
RUN chmod 755 ./run.sh
RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ./run.sh
