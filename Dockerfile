FROM alpine:3.2
MAINTAINER CooK "cook@eth2.com"
RUN apk add --update musl python3 bash py-pip \
    && rm /var/cache/apk/*
COPY files /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install flask
ENTRYPOINT ["python"]
CMD ["app.py"]
