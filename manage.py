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
