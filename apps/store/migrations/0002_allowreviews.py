# Generated by Django 4.0.4 on 2022-06-30 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllowReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Allow Reviews',
            },
        ),
    ]
