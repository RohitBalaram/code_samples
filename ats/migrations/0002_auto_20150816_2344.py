# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rdgs',
            name='d_o_b',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rdgs',
            name='econ_dis',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rdgs',
            name='ell',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rdgs',
            name='ethnic',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rdgs',
            name='first_name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rdgs',
            name='gender',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rdgs',
            name='grade',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rdgs',
            name='last_name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rdgs',
            name='level',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rdgs',
            name='off_cls',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rdgs',
            name='school',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rdgs',
            name='spec_ed',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rdgs',
            name='student_id',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rdgs',
            name='tracking_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
