FROM python:3.8

VOLUME ["/code"]
ADD . /code
WORKDIR /code

RUN pip install -r requirements.txt

EXPOSE 3000

CMD ["python", "camera_client.py"]