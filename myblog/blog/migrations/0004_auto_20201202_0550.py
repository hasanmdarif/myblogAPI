# Generated by Django 3.1.3 on 2020-12-02 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201202_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(choices=[('technology', 'Technology'), ('development', 'Developmet'), ('software', 'Software'), ('engineering', 'Engineering'), ('coding', 'Coding')], default='engineering', max_length=50),
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
    ]
