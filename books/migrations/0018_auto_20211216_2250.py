# Generated by Django 3.2.9 on 2021-12-16 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0017_alter_book_publishdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
