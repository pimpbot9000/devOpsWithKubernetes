FROM ubuntu:latest
WORKDIR /usr/src/app
RUN apt-get update && apt-get install -y python3 && apt-get install -y curl
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-psycopg2
RUN mkdir static
RUN mkdir templates
COPY app.py .
COPY requirements.txt .
COPY templates/index.html /usr/src/app/templates/index.html
RUN pip3 install -r requirements.txt
EXPOSE 7070
ENTRYPOINT [ "python3", "-u", "app.py" ]
CMD ["static"]

# in parent dir: docker build -t pimpbot9000/app2-07:latest -f app/Dockerfile app