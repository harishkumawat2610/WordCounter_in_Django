# WordCounter_in_Django

# Install Django Web Framework
<p> Django is a free, open source web framework that allows you to build web applications more easily and quickly with less coding. It is fast, secure framework written using Python programming language. In this brief tutorial, let us see how to install Django framework in Ubuntu 18.04 LTS server. Although this will work on other Debian/Ubuntu based systems and its derivatives like Linux Mint.</p>

## We can install Django in Ubuntu in two methods.

-  1.Using Ubuntu official repositories 
-  2.Using pip (Recommended method).

### We will see both methods.

# 1. Install Django Web Framework In Ubuntu using official repositories


```sh
$ sudo apt-get update
```
```sh
$ sudo apt-get install python-django
```
## Sample output:
```sh
Reading package lists... Done
Building dependency tree 
Reading state information... Done
The following additional packages will be installed:
 javascript-common libjs-jquery libpython-stdlib python
 python-django-common python-minimal python-sqlparse python-tz
 python2.7 python2.7-minimal
Suggested packages:
 apache2 | lighttpd | httpd python-doc python-tk python-psycopg2
 python-pymysql python-flup python-sqlite python-memcache python-pil
 python-bcrypt python-yaml geoip-database-extra
 | geoip-database-contrib gettext python-django-doc ipython bpython
 libgdal1 python-sqlparse-doc python2.7-doc binutils binfmt-support
The following NEW packages will be installed:
 javascript-common libjs-jquery libpython-stdlib python python-django
 python-django-common python-minimal python-sqlparse python-tz
 python2.7 python2.7-minimal
0 upgraded, 11 newly installed, 0 to remove and 30 not upgraded.
Need to get 3,951 kB of archives.
After this operation, 29.7 MB of additional disk space will be used.
Do you want to continue? [Y/n]
```
<h5>Type Y and press Enter when it asks you to continue to install Django.</h5>

# Raw GUI for Project

<img src="https://drive.google.com/uc?id=1prkbfV8a2LDnHqdYFyDs77mp6hNYsHs6" alt="alt text"/>

## Verify Django

We have installed Django on Ubuntu. Run the following command from the Terminal whether Django has been successfully installed or not.

```sh
$ django-admin --version
```

## Sample output:
```sh
2.1.7
```

# 2. Install Django Web Framework In Ubuntu using pip

This is officially recommended by Django project team. You can get most recent stable version of Django by using Python package manager called pip.

## Update the repositories list using command:

```sh
$ sudo apt-get update
```

## Install pip using any one of the command below.

### For Python 2 or lower versions:

## Update the repositories list using command:

```sh
$ sudo apt-get install python-pip
```

## Now, install Django if you use python 2:

```sh
$ sudo pip install django
```

### For python 3:

```sh
$ sudo apt-get install python3-pip
```

## If you use python 3, then use following command instead:

```sh
$ sudo pip3 install django
```

You can use either Python 2 or Python 3. I use Python 3 for the purpose of this tutorial.

### To verify the Django version, run:

```sh
$ django-admin --version
```

### Sample output:
```sh
2.1.7
```
