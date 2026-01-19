FROM python:3.12
WORKDIR /app
COPY grade.py .
CMD ["python", "grade.py"]