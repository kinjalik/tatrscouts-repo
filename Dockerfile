FROM python:3.9.7-bullseye

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

WORKDIR /backend
COPY requirements.txt /backend/
RUN pip install -r requirements.txt && rm requirements.txt

COPY . /backend/

ENTRYPOINT ["bash", "run.sh"]