# Generated by Django 4.1.1 on 2022-12-02 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sellpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100, null=True)),
                ('pirce', models.IntegerField(null=True)),
                ('age', models.IntegerField(null=True)),
                ('description', models.TextField(max_length=800)),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
