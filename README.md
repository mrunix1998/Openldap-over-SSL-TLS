# RUN WITH PYTHON VERSION 3.8
## openldap.installer
Auto install and configure openldap in ubuntu
three distribution of ubuntu -> focal - bionic - xenial

## Run guid
To run this project you need to some config based on your config that considered

> $ sudo apt-get dist-upgrade \
$ sudo apt-get update \
$ sudo python3.8 main.py 

in ldap.conf file: 
> uri = is your ldap / ldaps url
> base = is your ldap / ldaps domain name 
> rootbinddn = is your distinguished name of uri