#!/bin/bash

sed -i 's/^SLAPD_SERVICES="ldap.*/SLAPD_SERVICES="ldap:\/\/\/ ldapi:\/\/\/ ldaps:\/\/\/\"/g' /etc/default/slapd