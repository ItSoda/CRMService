# Generated by Django 4.2 on 2023-12-16 15:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reviews',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.events'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='events',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='events',
            name='participian',
            field=models.ManyToManyField(related_name='events_participian', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='events',
            name='tags',
            field=models.ManyToManyField(to='events.tags'),
        ),
        migrations.AddField(
            model_name='events',
            name='teams',
            field=models.ManyToManyField(related_name='events_teams', to='events.teams'),
        ),
        migrations.AddField(
            model_name='events',
            name='winners',
            field=models.ManyToManyField(blank=True, related_name='events_winners', to=settings.AUTH_USER_MODEL),
        ),
    ]
