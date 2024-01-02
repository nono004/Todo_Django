# Generated by Django 4.2.1 on 2024-01-02 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_alter_todomodel_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='Category',
            field=models.CharField(choices=[('work', '仕事'), ('study', '勉強'), ('hobby', '趣味'), ('others', 'その他')], default='work', max_length=10),
            preserve_default=False,
        ),
    ]