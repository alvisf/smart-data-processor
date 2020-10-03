FROM python:3.6
# ADD requirements.txt /app/requirements.txt
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD [ "python3","app.py" ]
ENTRYPOINT celery -A tasks worker 
