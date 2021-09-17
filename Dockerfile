FROM python:3.9.7-bullseye

WORKDIR /backend
COPY requirements.txt /backend/
RUN pip install -r requirements.txt && rm requirements.txt

COPY . /backend/

ENTRYPOINT ["bash", "run.sh"]