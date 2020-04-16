# Generated by Django 3.0.4 on 2020-04-15 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='list',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.List'),
        ),
        migrations.AlterField(
            model_name='list',
            name='board',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.Board'),
        ),
    ]
