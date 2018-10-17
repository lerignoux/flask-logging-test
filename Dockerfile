from python:3.7-alpine

RUN pip install flask

CMD ["python", "/app/app.py"]
