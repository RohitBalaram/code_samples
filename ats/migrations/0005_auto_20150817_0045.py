# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ats', '0004_auto_20150817_0010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='radpa',
            name='school',
        ),
        migrations.RemoveField(
            model_name='radpd',
            name='school',
        ),
        migrations.RemoveField(
            model_name='rbir',
            name='school',
        ),
        migrations.RemoveField(
            model_name='rhin',
            name='school',
        ),
        migrations.RemoveField(
            model_name='rnec',
            name='school',
        ),
        migrations.RemoveField(
            model_name='rspd',
            name='school',
        ),
        migrations.RemoveField(
            model_name='rtrr',
            name='school',
        ),
        migrations.AddField(
            model_name='radpa',
            name='dbn',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='radpd',
            name='dbn',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rbir',
            name='ddbnnn',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rhin',
            name='dbn',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rnec',
            name='dbn',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rspd',
            name='school_dbn',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rtrr',
            name='dbn',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='radpa',
            name='id',
            field=models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='radpd',
            name='id',
            field=models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='radr',
            name='id',
            field=models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rbir',
            name='id',
            field=models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rdgs',
            name='id',
            field=models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rhil',
            name='id',
            field=models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rhin',
            name='id',
            field=models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rmel',
            name='id',
            field=models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rnec',
            name='id',
            field=models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rocl',
            name='id',
            field=models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rpob',
            name='id',
            field=models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rsfm',
            name='id',
            field=models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rspd',
            name='id',
            field=models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rtrr',
            name='id',
            field=models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False),
        ),
    ]
