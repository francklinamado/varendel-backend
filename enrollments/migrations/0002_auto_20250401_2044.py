# Generated by Django 5.1.1 on 2025-04-01 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name="enrollment",
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=False),
        )
        
    ]
