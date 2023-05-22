# Generated by Django 4.2.1 on 2023-05-17 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='Created', max_length=100, verbose_name='Order status ')),
                ('item', models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.CASCADE, to='item.item', verbose_name='Name ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User id ')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Order',
                'ordering': ['id', 'status'],
            },
        ),
    ]