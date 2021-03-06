# Generated by Django 3.2.9 on 2021-11-26 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('publication_date', models.DateTimeField(verbose_name='publication date')),
                ('isbn_number', models.IntegerField(default=0)),
                ('page_number', models.IntegerField(default=0)),
                ('front_page_url', models.URLField()),
                ('publication_language', models.CharField(max_length=100)),
            ],
        ),
    ]
