FROM python:latest
WORKDIR /usr/src/app
RUN mkdir static
COPY memory-backend.py .
COPY app.py .
COPY models.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5050
ENTRYPOINT [ "python3", "-u", "memory-backend.py" ]
CMD ["5050"]