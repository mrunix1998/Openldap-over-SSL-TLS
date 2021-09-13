import os
import shlex
import subprocess, time
from getpass import getpass

print("""
    1 - OpenLdap server without SSL/TLS
    2 - OpenLdap client without SSL/TLS
    3 - Generate SSL/TLS for openldap server ( Berfor use this section please install openldap with section 1 ) 
    4 - Generate SSL/TLS for openldap client ( Berfor use this section please install openldap with section 2 )
""")

num = input("Enter Your choice : ")
distro = input("Enter Your release of ubuntu [focal | bionic | xenial] : ")


def use_ssl(distro):
    try:
        print("Generating self signed SSL for openldap-client")
        if distro == 'focal':
            os.popen('apt install -y nslcd nscd').read()
            time.sleep(1)
            os.popen('echo "ssl start_tls" >> /etc/nslcd.conf').read()
            time.sleep(1)
            os.popen('echo "tls_reqcert allow" >> /etc/nslcd.conf').read()
            time.sleep(1)
            subprocess.run('systemctl restart slapd'.split())
        else :
            os.popen('echo "TLS_REQCERT allow" >> /etc/ldap/ldap.conf').read()
            time.sleep(2)
            os.popen('cat ldap.conf > /etc/ldap.conf')
            time.sleep(2)
        print("Done")
    except BaseException as e:
        print(e)


def generate_ssl():
    try:
        print("Generating self signed SSL for openldap-server")
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
        subprocess.run('cp /etc/ssl/private/server.key /etc/ssl/private/server.crt /etc/ssl/certs/ca-certificates.crt /etc/ldap/sasl2/'.split())
        time.sleep(1)
        subprocess.run('chown openldap. /etc/ldap/sasl2/server.key /etc/ldap/sasl2/server.crt /etc/ldap/sasl2/ca-certificates.crt'.split())
        time.sleep(1)
        subprocess.run('bash add_ldaps.sh'.split())
        time.sleep(2)
        subprocess.run('ldapmodify -Y EXTERNAL -H ldapi:/// -f mod_ssl.ldif'.split())
        time.sleep(2)
        subprocess.run('systemctl restart slapd'.split())
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
        run('sudo -S bash openldap.server.installer.sh install', 'server')
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
            generate_ssl()
        except BaseException as e:
            print(e)
    elif distro == 'bionic':
        try:
            generate_ssl()
        except BaseException as e:
            print(e)

    elif distro == 'xenial':
        try:
            generate_ssl()
        except BaseException as e:
            print(e)

elif num == '4':
    if distro == 'focal':
        try:
            use_ssl(distro)
        except BaseException as e:
            print(e)

    elif distro == 'bionic':
        try:
            use_ssl(distro)
        except BaseException as e:
            print(e)

    elif distro == 'xenial':
        try:
            use_ssl(distro)
        except BaseException as e:
            print(e)