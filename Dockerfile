FROM python:3.6.5-slim

WORKDIR /app


ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["hello.py"]