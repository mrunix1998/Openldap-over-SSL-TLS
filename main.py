import subprocess
import time

print("""
    1 - OpenLdap server without SSL/TLS
    2 - OpenLdap client without SSL/TLS
    3 - Openldap server with SSL/TLS
    4 - OpenLdap client with SSL/TLS
""")

num = input("Enter Your choice : \n")
distro = input("Enter Your release of ubuntu [focal | bionic | xenial] : ")


if num == '1':
    if distro == 'focal':
        print("Installing Openldap ...")
        time.sleep(5)
        subprocess.run("bash", "open")
    elif distro == 'bionic':
        pass
    elif distro == 'xenial':
        pass
elif num == '2':
    if distro == 'focal':
        print("2-bionic")
    elif distro == 'bionic':
        pass
    elif distro == 'xenial':
        pass
elif num == '3':
    if distro == 'focal':
        print("3-bionic")
    elif distro == 'bionic':
        pass
    elif distro == 'xenial':
        pass
elif num == '4':
    if distto == 'focal':
        print("4-bionic")
    elif distro == 'bionic':
        pass
    elif distro == 'xenial':
        pass