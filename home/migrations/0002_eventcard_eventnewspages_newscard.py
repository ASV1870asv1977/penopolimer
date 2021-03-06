# Generated by Django 3.2.8 on 2021-10-31 07:12

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventNewsPages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Новости и мероприятия',
                'verbose_name_plural': 'Новости и мероприятия',
            },
        ),
        migrations.CreateModel(
            name='NewsCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('news_data', models.CharField(max_length=2)),
                ('news_month', models.CharField(max_length=8)),
                ('news_name', wagtail.core.fields.RichTextField(blank=True, max_length=100, null=True)),
                ('news_description', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('news', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='home.eventnewspages')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('event_data', models.CharField(max_length=2)),
                ('event_month', models.CharField(max_length=8)),
                ('event_name', wagtail.core.fields.RichTextField(blank=True, max_length=100, null=True)),
                ('event_description', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('event', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='home.eventnewspages')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
