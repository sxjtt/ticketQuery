# Generated by Django 3.1.7 on 2021-05-01 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_manage', '0002_auto_20210501_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='train_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ticket_manage.traintype', verbose_name='车次类型（k..z..）'),
        ),
    ]
