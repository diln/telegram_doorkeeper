FROM python:3.10

ENV TZ=Europe/Moscow

WORKDIR /opt/doorkeeper_bot

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY doorkeeper.py ./

ENTRYPOINT ["python", "doorkeeper.py"]