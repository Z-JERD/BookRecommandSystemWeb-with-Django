# Generated by Django 2.0.5 on 2018-05-16 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookRecommand', '0004_auto_20180516_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookUrl',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
