from invoke import task

@task
def run(c):
    c.run("python main.py")

@task
def test(c):
    c.run("python -m unittest discover tests")

@task
def clean(c):
    c.run("find . -type f -name '*.pyc' -delete")
    c.run("find . -type d -name '__pycache__' -delete")