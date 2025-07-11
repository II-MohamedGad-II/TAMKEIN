# Generated by Django 5.1.5 on 2025-02-19 10:18

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0002_answer_delete_useranswer'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answered_at',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='is_correct',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='userid',
        ),
        migrations.AddField(
            model_name='answer',
            name='answeredat',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='iscorrect',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.question'),
        ),
    ]
