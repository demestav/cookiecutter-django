from fabric import task
from invoke import Collection
import fabfile.local
import fabfile.production

ns = Collection()
ns.add_collection(Collection.from_module(fabfile.local))
ns.add_collection(Collection.from_module(fabfile.production))
