FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip uninstall --yes praw

COPY . .

CMD ["python", "src/main.py"]