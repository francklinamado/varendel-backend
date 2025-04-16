import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscriptions', '0001_initial'),
        ('students', '0002_alter_student_inscriptions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='inscriptions',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_inscription', null=False, to='inscriptions.inscription'),
        ),
    ]

