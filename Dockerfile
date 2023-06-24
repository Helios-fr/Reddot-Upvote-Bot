FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .
COPY accounts.txt .

RUN pip install -r requirements.txt

COPY ./src .

CMD ["python", "main.py"]