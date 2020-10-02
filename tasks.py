from celery import Celery

app = Celery('tasks', backend='rpc://', broker='pyamqp://')

@app.task
def sentence_length(sentence):
    print("hello")
    return len(sentence)
