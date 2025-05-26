from robocorp.tasks import task
import requests

@task
def minimal_task():
    message = "Hello"
    message = message + " World!"
