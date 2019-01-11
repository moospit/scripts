import pkg_resources
from subprocess import call

for pack in [dist.project_name for dist in pkg_resources.working_set]:
    print("Upgrading", pack)
    call("pip install --upgrade" + pack, shell=True)
