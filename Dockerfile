FROM python:3-alpine3.6

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apk add --no-cache python3-dev gcc
RUN apk add --no-cache libxml2-dev
RUN apk add --no-cache musl-dev
RUN apk add --no-cache libxslt-dev
RUN apk add --no-cache libffi-dev
RUN apk add --no-cache libressl-dev

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "./Cr3d0v3r.py" ]