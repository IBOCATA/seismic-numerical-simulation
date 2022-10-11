django-admin check auth admin myapp
django-admin check --tag models --tag compatibility
django-admin check --database default --database other
django-admin check --deploy --settings=production_settings
from django.db import migrations
from django.db import connection


class Migration(migrations.Migration):
    db_cursor = connection.cursor()
    check_exists_query = "SELECT relname FROM pg_class WHERE relname=%s;"
    base_query = "DELETE FROM {table} WHERE condition;"
    tables = [tables]
    existing_tables = []

    for table in tables:
        db_cursor.execute(check_exists_query, [table])
        result = db_cursor.fetchone()
        if result:
            existing_tables.append(table)

    operations = [
        migrations.RunSQL(base_query.format(table=existing_table)) for existing_table in existing_tables
    ]
$ python3 --version
Python 3.9
$ sudo aptitude install gdal-bin libgdal-dev
$ sudo aptitude install python3-gdal
$ sudo aptitude install binutils libproj-dev
aptitude install binutils libproj-dev
$ docker run --name=postgis -d -e POSTGRES_USER=user001 -e POSTGRES_PASS=123456789 -e POSTGRES_DBNAME=gis -p 5432:5432 kartoza/postgis:9.6-2.4
$ python3 -m venv env
(env) $
$ source env/bin/activate
$ pip install django
$ django-admin.py startproject seismic 3d
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'gis',
        'USER': 'user001',
        'PASSWORD': '123456789',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
$ pip install psycopg2-binary
INSTALLED_APPS = [
    # [...]
    'django.contrib.gis'
]
