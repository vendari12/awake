# Generated by Django 2.1.5 on 2020-01-04 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_item_label_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('BG', 'BAGS'), ('LRS', 'SHOES'), ('JCT', 'JACKET'), ('MS', 'MEN SHIRT'), ('MSOO', 'MEN SHOES'), ('MT', 'MEN TROUSERS'), ('WS', 'WOMEN SHIRT'), ('WSK', 'WOMEN SKIRT'), ('WSH', 'WOMEN SHOES'), ('WG', 'WOMEN GOWNS')], max_length=50),
        ),
    ]