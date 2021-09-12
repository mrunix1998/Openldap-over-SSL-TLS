import os
import shlex
import subprocess, time
from getpass import getpass

print("""
    1 - OpenLdap server without SSL/TLS
    2 - OpenLdap client without SSL/TLS
    3 - Openldap server with SSL/TLS
    4 - OpenLdap client with SSL/TLS
""")

num = input("Enter Your choice : ")
distro = input("Enter Your release of ubuntu [focal | bionic | xenial] : ")


def generate_ssl(distro):
    try:
        os.popen('echo "#TLS_CACERT    /etc/ssl/certs/ca-certificate" > /etc/ldap/ldap.conf').read()
        time.sleep(1)
        print("config set")
        os.popen('echo "TLS_REQCERT   /etc/ssl/certs/ca-certificate" >> /etc/ldap/ldap.conf').read()
        print("config set")
        time.sleep(1)
        subprocess.run('openssl genrsa -aes128 -out /etc/ssl/private/server.key 2048'.split())
        time.sleep(1)
        subprocess.run('openssl rsa -in /etc/ssl/private/server.key -out /etc/ssl/private/server.key'.split())
        time.sleep(1)
        subprocess.run('openssl req -new -days 3650 -key /etc/ssl/private/server.key -out /etc/ssl/private/server.csr'.split())
        time.sleep(1)
        subprocess.run('openssl x509 -in /etc/ssl/private/server.csr -out /etc/ssl/private/server.crt -req -signkey /etc/ssl/private/server.key -days 3650'.split())
        time.sleep(1)
        subprocess.run('cp /etc/ssl/private/{server.key,server.crt} /etc/ssl/certs/ca-certificates.crt /etc/ldap/sasl2/'.split())
        time.sleep(1)
        subprocess.run('chown openldap. /etc/ldap/sasl2/server.key /etc/ldap/sasl2/server.crt /etc/ldap/sasl2/ca-certificates.crt'.split())
        time.sleep(1)
        if distro == 'xenial':
            subprocess.run('bash command.sh'.split())
            subprocess.run('ldapmodify -Y EXTERNAL -H ldapi:/// -f mod_ssl.ldif'.split())
        subprocess.run('systemctl restart slapd'.split())
        print('\n')
        time.sleep(1)
        subprocess.run('systemctl status slapd'.split())
    except BaseException as e:
        print(e)


def run(command, type):
    print("Installing Openldap ", type, end="")
    for i in range(4):
        print('.', end='')
        time.sleep(1)
    time.sleep(3)
    process = subprocess.run(command.split(),
                             input=getpass("password :"), encoding="ascii")
    print(process.stdout)


if num == '1':
    if distro == 'focal':
        run('sudo -S bash openldap.server.installer.sh install', 'sever')
    elif distro == 'bionic':
        run('sudo -S bash openldap.server.installer.sh install', 'server')
    elif distro == 'xenial':
        run('sudo -S bash openldap.server.installer.sh install', 'server')

elif num == '2':
    if distro == 'focal':
        run('sudo -S bash openldap.client.installer.sh install', 'client')
    elif distro == 'bionic':
        run('sudo -S bash openldap.client.installer.sh install', 'client')
    elif distro == 'xenial':
        run('sudo -S bash openldap.client.installer.sh install', 'client')

elif num == '3':
    if distro == 'focal':
        try:
            run('sudo -S bash  openldap.sslserver.installer.sh install', 'server')
        except BaseException as e:
            print(e)
        generate_ssl(distro)
    elif distro == 'bionic':
        try:
            run('sudo -S bash  openldap.sslserver.installer.sh install', 'server')
        except BaseException as e:
            print(e)
        generate_ssl(distro)

    elif distro == 'xenial':
        try:
            run('sudo -S bash  openldap.sslserver.installer.sh install', 'server')
        except BaseException as e:
            print(e)
        generate_ssl(distro)

elif num == '4':
    if distro == 'focal':
        try:
            run('sudo -S bash openldap.sslclient.installer.sh install', 'client')
        except BaseException as e:
            print(e)
        generate_ssl(distro)

    elif distro == 'bionic':
        try:
            run('sudo -S bash openldap.sslclient.installer.sh install', 'client')
        except BaseException as e:
            print(e)
        generate_ssl(distro)

    elif distro == 'xenial':
        try:
            run('sudo -S bash openldap.sslclient.installer.sh install', 'client')
        except BaseException as e:
            print(e)
        generate_ssl(distro)