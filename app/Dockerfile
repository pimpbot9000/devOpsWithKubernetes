FROM python:latest
RUN pip install flask && pip install waitress
WORKDIR /usr/app
COPY app.py .
EXPOSE 8080
CMD ["python3", "app.py"]
