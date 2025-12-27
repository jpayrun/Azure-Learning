FROM python:3.13-slim

WORKDIR /app
COPY ./requirements.txt .
COPY . .

RUN pip install -r  requirements.txt

EXPOSE 8050

CMD ["python", "./app.py"]
# CMD ["gunicorn", "-b", "0.0.0.0:8050", "app:server"]
