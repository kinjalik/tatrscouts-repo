FROM python:3.9.7-bullseye

WORKDIR /backend
COPY requirements.txt /backend/
RUN pip install -r requirements.txt && rm requirements.txt

COPY . /backend/

COPY download_model.py /download_model.py
RUN python3 /download_model.py && rm /download_model.py

ENTRYPOINT ["bash", "run.sh"]