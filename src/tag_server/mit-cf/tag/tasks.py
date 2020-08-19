from celery import Celery

app = Celery('tasks', broker='pyamqp://mit:mit@101.101.210.48:5672//')

@app.task
def add(x,y):
    return x+y
