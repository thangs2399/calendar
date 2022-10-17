FROM python:alpine3.16

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

# CMD flask --app capp run --host=0.0.0.0

ENTRYPOINT [ "python3" ]

CMD ["main.py"]