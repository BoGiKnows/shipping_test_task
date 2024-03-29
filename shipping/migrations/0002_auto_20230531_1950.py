# Generated by Django 4.2.1 on 2023-05-31 16:49

from django.db import migrations
import csv

def combine_names(apps, schema_editor):
    Location = apps.get_model('shipping', 'Location')
    with open('shipping/data/uszips.csv') as f:
        reader = csv.reader(f)
        next(reader)
        # for row in reader:
        #     Location.objects.get_or_create(
        #         city=row[3],
        #         state=row[4],
        #         zip=int(row[0]),
        #         lon=float(row[2]),
        #         lat=float(row[1])
        #     )
        Location.objects.bulk_create([
            Location(
                city=row[3],
                state=row[4],
                zip=int(row[0]),
                lon=float(row[2]),
                lat=float(row[1])
            )
            for row in reader
        ], ignore_conflicts=True)
        print('data has been loaded')


class Migration(migrations.Migration):
    dependencies = [
        ('shipping', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(combine_names),
    ]
