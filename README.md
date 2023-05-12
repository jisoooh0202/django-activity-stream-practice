# django-activity-stream-practice

For the step by step guide, visit [this post](https://jnpnote.com/django-activity-stream-practice/).

## To Run the project

clone the repo and get into the project directory
```bash
cd djangog-activity-stream-practice
```
create virtualenv

```bash
python -m virtualenv venv
```

activate venv

```bash
source venv/bin/activate
venv/Script/activate # Windows
```

install requirements

```bash
pip install -r requirements.txt
```

create database
```bash
python manage.py migrate
```

create superuser
```bash
python manage.py createsuperuser
```

runserver
```bash
python manage.py runserver
```

Try login multiple times to see the activity.