# Generated by Django 3.1.7 on 2021-05-24 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_manage', '0007_auto_20210524_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='arrive_type',
            field=models.CharField(default='正点', max_length=32, verbose_name='正点/晚点'),
        ),
    ]
