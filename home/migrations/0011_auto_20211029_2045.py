# Generated by Django 3.2.8 on 2021-10-29 17:45

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0010_aboutimage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AboutImage',
            new_name='HomeSlidesImage',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='name_page',
        ),
        migrations.AlterField(
            model_name='homeslidesimage',
            name='equipment',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='slides', to='home.homepage'),
        ),
    ]
