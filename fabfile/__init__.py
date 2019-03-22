from fabric import task
from invoke import Collection
import local
import production

ns = Collection()
ns.add_collection(Collection.from_module(local))
ns.add_collection(Collection.from_module(production))
