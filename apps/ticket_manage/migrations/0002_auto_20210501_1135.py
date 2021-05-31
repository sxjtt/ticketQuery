# Generated by Django 3.1.7 on 2021-05-01 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_manage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='target_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='target_place', to='ticket_manage.placetype', verbose_name='目的地'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='start_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='start_place', to='ticket_manage.placetype', verbose_name='出发地'),
        ),
    ]