from fabric import task
from invocations.console import confirm


@task(name="clean")
def clean(c):
    """
    Stops running containers, removes containers, images, network and volumes.
    """
    if confirm("This will remove all containers and volumes. Cannot be undone. Are you sure?", assume_yes=False):
        c.run('docker-compose -f local.yml down --volumes --rmi all', replace_env=False)


@task(name='build')
def build(c):
    """
    Builds images.
    """
    c.run('docker-compose -f local.yml build', replace_env=False)


@task(name='up')
def up(c):
    """
    Builds images, creates and starts containers.
    """
    c.run('docker-compose -f local.yml up', replace_env=False)


@task(name='upd')
def upd(c):
    """
    Builds images, creates and starts containers on the background.
    """
    c.run('docker-compose -f local.yml up -d', replace_env=False)


@task(name='makemigrations')
def makemigrations(c):
    """
    Creates new migrations.
    """
    c.run('docker-compose -f local.yml run --rm django python manage.py makemigrations', replace_env=False)


@task(name='migrate')
def migrate(c):
    """
    Applies migrations.
    """
    c.run('docker-compose -f local.yml run --rm django python manage.py migrate', replace_env=False)


@task(name='createsuperuser')
def createsuperuser(c):
    """
    Creates a superuser.
    """
    c.run('docker-compose -f local.yml run --rm django python manage.py createsuperuser', pty=True, replace_env=False)
