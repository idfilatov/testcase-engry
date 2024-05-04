FROM python:3.11.7-slim-bullseye

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app /app
EXPOSE 9009
CMD ["python", "-m", "app.main", "--port", "9009"]
