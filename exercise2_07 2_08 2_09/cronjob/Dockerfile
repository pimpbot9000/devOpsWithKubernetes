FROM python:latest
WORKDIR /usr/src/app
RUN pip install requests
COPY job.py .
ENTRYPOINT [ "python3", "-u", "job.py" ]
