# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ats', '0002_auto_20150816_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radpa',
            name='adm_cde',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radpa',
            name='adm_cls',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radpa',
            name='adm_grd',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radpa',
            name='adm_rea',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radpa',
            name='apt_flr',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radpa',
            name='birth_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='radpa',
            name='cur_cls',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radpa',
            name='cur_grd',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radpa',
            name='day_ofadm',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='radpa',
            name='documents_code',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radpa',
            name='from_dbn',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radpa',
            name='geo_cde',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radpa',
            name='hm_lg',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radpa',
            name='pob_cde',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radpa',
            name='recs_rcvd_sent',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radpa',
            name='school',
            field=models.CharField(db_column='dbn', blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radpa',
            name='st',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radpa',
            name='street_address',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radpa',
            name='student_id',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='radpa',
            name='student_name',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radpa',
            name='sx',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radpa',
            name='tracking_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='radpa',
            name='zip_cde',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radr',
            name='a_c_flag',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radr',
            name='apt_num',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radr',
            name='dist_code',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radr',
            name='err_code',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radr',
            name='first_name',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radr',
            name='grd',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radr',
            name='grd_level',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radr',
            name='house_num',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radr',
            name='house_stat',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radr',
            name='last_name',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radr',
            name='non_res',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radr',
            name='off_cls',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radr',
            name='phone_number',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radr',
            name='res_boro',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radr',
            name='res_dist',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radr',
            name='school',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radr',
            name='sex',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radr',
            name='street_name',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radr',
            name='student_id',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='radr',
            name='tracking_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='radr',
            name='zip',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rhil',
            name='admission_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rhil',
            name='birth_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rhil',
            name='excludable_date',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rhil',
            name='exempt_code',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rhil',
            name='exempt_end_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rhil',
            name='grd_cde',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rhil',
            name='grd_lvl',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rhil',
            name='immun_stat',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rhil',
            name='immun_type',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rhil',
            name='incmpl',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rhil',
            name='off_cls',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rhil',
            name='phone_number',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rhil',
            name='school',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rhil',
            name='sex',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rhil',
            name='student_id',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rhil',
            name='student_name',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rhil',
            name='tracking_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rhin',
            name='date_of_birth',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rhin',
            name='description',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rhin',
            name='first_name',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rhin',
            name='grade_code',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rhin',
            name='grade_level',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rhin',
            name='health_ins_code',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rhin',
            name='last_name',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rhin',
            name='off_class',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rhin',
            name='school',
            field=models.CharField(db_column='dbn', blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rhin',
            name='sex',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rhin',
            name='student_id',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rhin',
            name='tracking_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rmel',
            name='birth_date',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rmel',
            name='grade',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rmel',
            name='grade_level',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rmel',
            name='home_room',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rmel',
            name='incomplete_reasons',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rmel',
            name='meal_code',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rmel',
            name='official_class',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rmel',
            name='phone_number',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rmel',
            name='school',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rmel',
            name='sex',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rmel',
            name='source',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rmel',
            name='student_id',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rmel',
            name='student_name',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rmel',
            name='tracking_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rnec',
            name='american_indian_alaskan',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rnec',
            name='asian',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rnec',
            name='black',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rnec',
            name='first_name',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rnec',
            name='grade_code',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rnec',
            name='grade_level',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rnec',
            name='hawaiian_pacific_islander',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rnec',
            name='hispanic',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rnec',
            name='last_name',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rnec',
            name='off_class',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rnec',
            name='old_ethnic_code',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rnec',
            name='school',
            field=models.CharField(db_column='dbn', blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rnec',
            name='sex',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rnec',
            name='student_id',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rnec',
            name='tracking_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rnec',
            name='white',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rocl',
            name='advisor',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rocl',
            name='dob',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rocl',
            name='gl',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rocl',
            name='grade',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rocl',
            name='loc',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rocl',
            name='name',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rocl',
            name='ocl',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rocl',
            name='phone_num',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rocl',
            name='room',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rocl',
            name='school',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rocl',
            name='sex',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rocl',
            name='staff_1',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rocl',
            name='staff_2',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rocl',
            name='status',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rocl',
            name='student_id',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rocl',
            name='teacher',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rocl',
            name='tracking_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rpob',
            name='first_enter_nyc_date',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rpob',
            name='first_name',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rpob',
            name='geo_code',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rpob',
            name='grade',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rpob',
            name='grade_level',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rpob',
            name='home_language_code',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rpob',
            name='last_name',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rpob',
            name='official_class',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rpob',
            name='place_of_birth',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rpob',
            name='school',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rpob',
            name='sex',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rpob',
            name='student_id',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rpob',
            name='tracking_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rpob',
            name='x_coded',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rsfm',
            name='admit_code',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rsfm',
            name='admit_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rsfm',
            name='admit_reason',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rsfm',
            name='birth_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rsfm',
            name='class_field',
            field=models.CharField(db_column='class', blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rsfm',
            name='first_name',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rsfm',
            name='grade',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rsfm',
            name='last_name',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rsfm',
            name='level',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rsfm',
            name='prev_admit_code',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rsfm',
            name='prev_admit_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rsfm',
            name='prev_class',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rsfm',
            name='prev_discharge_code',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rsfm',
            name='prev_discharge_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rsfm',
            name='prev_grade',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rsfm',
            name='prev_level',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rsfm',
            name='prev_school',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rsfm',
            name='school',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rsfm',
            name='sex',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rsfm',
            name='student_id',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rsfm',
            name='tracking_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
