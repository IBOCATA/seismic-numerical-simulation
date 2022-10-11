dtables = [tables]
    existing_tables = []

    for table in tables:
        db_cursor.execute(check_exists_query, [table])
        result = db_cursor.fetchone()
        if result:
            existing_tables.append(table)

    operations = [
        migrations.RunSQL(base_query.format(table=existing_table)) for existing_table in existing_tables
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
        'PORT': '8000'
    }
}

 