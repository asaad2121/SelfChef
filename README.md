# SelfChef

## Live Website
http://masaadshaikh.pythonanywhere.com/

### Table of Contents
- [Steps for running project](#steps-for-running-project)
    * [Clone Project](#clone-repository)
    * [Environment Setup](#environment-setup)
    * [Installation of Dependencies](#installation-of-dependencies)
    * [Migrations and SuperUser](#migrations-and-superuser)
    * [Running Server](#running-django-server)
    

### Steps for running project:

##### Clone Repository:
```bash
git clone https://github.com/asaad2121/SelfChef.git
cd Book-Management
```

##### Environment Setup:

```bash
pip install virtualenv
virtualenv venv
```
##### Installation of Dependencies:

```bash
source venv/bin/activate
pip install -r requirements.txt
```

##### Migrations and SuperUser
```bash
source venv/bin/activate
source .env
python manage.py migrate
python manage.py createsuperuser
```

##### Running Django Server:

```bash
source venv/bin/activate
source .env
python manage.py runserver
```
