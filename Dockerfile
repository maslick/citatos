FROM python:3

WORKDIR /app
EXPOSE 5000
COPY . /app

RUN pip install -U pip
RUN pip install -r /app/requirements.txt

CMD ["gunicorn", "run:app", "-c", "gunicorn.config.py"]
