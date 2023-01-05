FROM ubuntu:22.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

WORKDIR /app

RUN pip install flask logging datetime

COPY . /app

RUN chmod 555 /app

USER 1000:1000

ENTRYPOINT [ "python3" ]

EXPOSE 5000
CMD [ "app.py" ]