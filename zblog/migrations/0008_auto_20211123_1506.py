# Generated by Django 3.2.9 on 2021-11-23 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zblog', '0007_auto_20211123_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='talkshit',
        ),
        migrations.RemoveField(
            model_name='post',
            name='talkshit_md',
        ),
        migrations.AddField(
            model_name='blogimage',
            name='b_img_alt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]