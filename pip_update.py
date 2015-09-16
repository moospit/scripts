import os
import pip
from subprocess import call


def get_package_information():
    """ Read all current installed packages """
    packages = {}
    for dist in pip.get_installed_distributions():
        packages[dist.project_name] = dist.version

    return packages


def update_packages(packages):
    """ Update all packages via pip """
    for pack, oldver in packages.items():
        if pip.main(['install', '--upgrade', '--quiet', pack]) == 0:
            newver = next(d.version for d in pip.get_installed_distributions()
                          if d.project_name == pack)
        else:
            print("[!] Update of {} failed".format(pack))
            continue

        if newver > oldver:
            print("[*] {:>20}: {:>10} -> {:<10}".format(pack, oldver, newver))
        else:
            print("[*] {:>20}: {:>10}".format(pack, oldver))


def main():
    """ The main routine """
    print("[*] {:*^50}\n[*]".format(" PIP Updater "))
    packages = get_package_information()
    update_packages(packages)
    print("[*]\n[*] {:*^50}".format(" PIP Updater finished "))
    input("[*] Press any key to close")

if __name__ == "__main__":
    main()
