FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
COPY . .

CMD bash -c "while true; do sleep 1; done"