from fabric import task
from invocations.console import confirm


@task(name="clean")
def clean(c):
    """
    Stops running containers, removes containers, images, network and volumes.
    """
    if confirm("This will remove all containers and volumes. Cannot be undone. Are you sure?", assume_yes=False):
        c.run('docker-compose -f local.yml down --volumes --rmi all')


@task(name='build')
def build(c):
    """
    Builds images.
    """
    c.run('docker-compose -f local.yml build')


@task(name='up')
def up(c):
    """
    Builds images, creates and starts containers.
    """
    c.run('docker-compose -f local.yml up')


@task(name='upd')
def upd(c):
    """
    Builds images, creates and starts containers on the background.
    """
    c.run('docker-compose -f local.yml up -d')


@task(name='makemigrations')
def makemigrations(c):
    """
    Creates new migrations.
    """
    c.run('docker-compose -f local.yml run --rm django python manage.py makemigrations')


@task(name='migrate')
def migrate(c):
    """
    Applies migrations.
    """
    c.run('docker-compose -f local.yml run --rm django python manage.py migrate')


@task(name='createsuperuser')
def createsuperuser(c):
    """
    Creates a superuser.
    """
    c.run('docker-compose -f local.yml run --rm django python manage.py createsuperuser', pty=True)
