FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD [ "python", "main.py" ]
#CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]
