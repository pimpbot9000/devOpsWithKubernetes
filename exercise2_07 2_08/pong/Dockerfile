FROM python:latest
WORKDIR /usr/src/app
RUN mkdir static
COPY pong.py .
COPY models.py .
COPY manage.py .
COPY app.py .
#RUN apt-get install -y python3-psycopg2
COPY requirements.txt .
RUN pip install -r requirements.txt
#RUN pip install Flask-Script
EXPOSE 6060
ENTRYPOINT [ "python3", "-u", "pong.py" ]
CMD ["file.txt"]


# docker build -t pimpbot9000/pong2-01:latest -f Dockerfile.pong2 .