
FROM python:alpine

WORKDIR /app


RUN pip install pymongo

COPY models.py .
COPY seeder.py .

CMD ["python", "seeder.py"]