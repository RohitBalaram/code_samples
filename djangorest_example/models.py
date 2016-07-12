from django.db import models


# Custom Managers

class AtsManager(models.Manager):
    def latest_set(self):
        latest_date = self.latest('tracking_date')
        return self.filter(tracking_date=latest_date.tracking_date)


# Models

class Radpa(models.Model):
    dbn = models.CharField(max_length=255, blank=True, null=True)
    day_ofadm = models.DateField(blank=True, null=True)
    student_name = models.CharField(max_length=255, blank=True, null=True)
    st = models.CharField(max_length=255, blank=True, null=True)
    sx = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    cur_grd = models.CharField(max_length=255, blank=True, null=True)
    cur_cls = models.CharField(max_length=255, blank=True, null=True)
    adm_grd = models.CharField(max_length=255, blank=True, null=True)
    adm_cls = models.CharField(max_length=255, blank=True, null=True)
    adm_cde = models.CharField(max_length=255, blank=True, null=True)
    adm_rea = models.CharField(max_length=255, blank=True, null=True)
    hm_lg = models.CharField(max_length=255, blank=True, null=True)
    street_address = models.CharField(max_length=255, blank=True, null=True)
    apt_flr = models.CharField(max_length=255, blank=True, null=True)
    zip_cde = models.CharField(max_length=255, blank=True, null=True)
    pob_cde = models.CharField(max_length=255, blank=True, null=True)
    geo_cde = models.CharField(max_length=255, blank=True, null=True)
    from_dbn = models.CharField(max_length=255, blank=True, null=True)
    recs_rcvd_sent = models.CharField(max_length=255, blank=True, null=True)
    documents_code = models.CharField(max_length=255, blank=True, null=True)
    tracking_date = models.DateField(blank=True, null=True)

    # Managers
    objects = models.Manager()  # The default manager.
    ats_objects = AtsManager()  # The ATS manager.

    class Meta:
        db_table = 'ats_radpa'


class Radpd(models.Model):
    dbn = models.CharField(max_length=255, blank=True, null=True)
    day_of_disch = models.DateField(blank=True, null=True)
    student_name = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    birth_dte = models.DateField(blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    cur_grd = models.CharField(max_length=255, blank=True, null=True)
    cur_cls = models.CharField(max_length=255, blank=True, null=True)
    admission_dte = models.CharField(max_length=255, blank=True, null=True)
    dis_cde = models.CharField(max_length=255, blank=True, null=True)
    dis_reason_dipl_typ = models.CharField(max_length=255, blank=True, null=True)
    new_street_address = models.CharField(max_length=255, blank=True, null=True)
    apt_flr = models.CharField(max_length=255, blank=True, null=True)
    zip_cde = models.CharField(max_length=255, blank=True, null=True)
    pst_sec_pln = models.CharField(max_length=255, blank=True, null=True)
    geo_cde = models.CharField(max_length=255, blank=True, null=True)
    to_boro = models.CharField(max_length=255, blank=True, null=True)
    dist = models.CharField(max_length=255, blank=True, null=True)
    schl = models.CharField(max_length=255, blank=True, null=True)
    con_frm_dis = models.CharField(max_length=255, blank=True, null=True)
    recs_rcvd_sent = models.CharField(max_length=255, blank=True, null=True)
    documents_code = models.CharField(max_length=255, blank=True, null=True)
    tracking_date = models.DateField(blank=True, null=True)

    # Managers
    objects = models.Manager()  # The default manager.
    ats_objects = AtsManager()  # The ATS manager.

    class Meta:
        db_table = 'ats_radpd'


class Radr(models.Model):
    last_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    grd = models.CharField(max_length=255, blank=True, null=True)
    grd_level = models.CharField(max_length=255, blank=True, null=True)
    off_cls = models.CharField(max_length=255, blank=True, null=True)
    house_num = models.CharField(max_length=255, blank=True, null=True)
    street_name = models.CharField(max_length=255, blank=True, null=True)
    apt_num = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=255, blank=True, null=True)
    res_boro = models.CharField(max_length=255, blank=True, null=True)
    res_dist = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    a_c_flag = models.CharField(max_length=255, blank=True, null=True)
    err_code = models.CharField(max_length=255, blank=True, null=True)
    dist_code = models.CharField(max_length=255, blank=True, null=True)
    non_res = models.CharField(max_length=255, blank=True, null=True)
    house_stat = models.CharField(max_length=255, blank=True, null=True)
    tracking_date = models.DateField(blank=True, null=True)
    school = models.CharField(max_length=255, blank=True, null=True)

    # Managers
    objects = models.Manager()  # The default manager.
    ats_objects = AtsManager()  # The ATS manager.

    class Meta:
        db_table = 'ats_radr'


class Rbir(models.Model):
    ddbnnn = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    birth_dt = models.DateField(blank=True, null=True)
    off_cls = models.CharField(max_length=255, blank=True, null=True)
    grd_cd = models.CharField(max_length=255, blank=True, null=True)
    grd_lvl = models.CharField(max_length=255, blank=True, null=True)
    street_number = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    apt = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    st = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=255, blank=True, null=True)
    home_phone = models.CharField(max_length=255, blank=True, null=True)
    adult_last_1 = models.CharField(max_length=255, blank=True, null=True)
    adult_first_1 = models.CharField(max_length=255, blank=True, null=True)
    adult_phone_1 = models.CharField(max_length=255, blank=True, null=True)
    adult_last_2 = models.CharField(max_length=255, blank=True, null=True)
    adult_first_2 = models.CharField(max_length=255, blank=True, null=True)
    adult_phone_2 = models.CharField(max_length=255, blank=True, null=True)
    adult_last_3 = models.CharField(max_length=255, blank=True, null=True)
    adult_first_3 = models.CharField(max_length=255, blank=True, null=True)
    adult_phone_3 = models.CharField(max_length=255, blank=True, null=True)
    student_phone = models.CharField(max_length=255, blank=True, null=True)
    meal_cde = models.CharField(max_length=255, blank=True, null=True)
    ytd_attd_pct = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    tracking_date = models.DateField(blank=True, null=True)

    # Managers
    objects = models.Manager()  # The default manager.
    ats_objects = AtsManager()  # The ATS manager.

    class Meta:
        db_table = 'ats_rbir'


class Rdgs(models.Model):
    school = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    d_o_b = models.CharField(max_length=255, blank=True, null=True)
    grade = models.CharField(max_length=255, blank=True, null=True)
    level = models.CharField(max_length=255, blank=True, null=True)
    off_cls = models.CharField(max_length=255, blank=True, null=True)
    spec_ed = models.CharField(max_length=255, blank=True, null=True)
    ethnic = models.CharField(max_length=255, blank=True, null=True)
    ell = models.CharField(max_length=255, blank=True, null=True)
    econ_dis = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    tracking_date = models.DateField(blank=True, null=True)

    # Managers
    objects = models.Manager()  # The default manager.
    ats_objects = AtsManager()  # The ATS manager.

    class Meta:
        db_table = 'ats_rdgs'


class Rhil(models.Model):
    student_name = models.CharField(max_length=255, blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    grd_cde = models.CharField(max_length=255, blank=True, null=True)
    grd_lvl = models.CharField(max_length=255, blank=True, null=True)
    off_cls = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    admission_date = models.DateField(blank=True, null=True)
    immun_stat = models.CharField(max_length=255, blank=True, null=True)
    excludable_date = models.CharField(max_length=255, blank=True, null=True)
    immun_type = models.CharField(max_length=255, blank=True, null=True)
    incmpl = models.CharField(max_length=255, blank=True, null=True)
    exempt_code = models.CharField(max_length=255, blank=True, null=True)
    exempt_end_date = models.DateField(blank=True, null=True)
    tracking_date = models.DateField(blank=True, null=True)
    school = models.CharField(max_length=255, blank=True, null=True)

    # Managers
    objects = models.Manager()  # The default manager.
    ats_objects = AtsManager()  # The ATS manager.

    class Meta:
        db_table = 'ats_rhil'


class Rhin(models.Model):
    dbn = models.CharField(max_length=255, blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    grade_code = models.CharField(max_length=255, blank=True, null=True)
    grade_level = models.CharField(max_length=255, blank=True, null=True)
    off_class = models.CharField(max_length=255, blank=True, null=True)
    health_ins_code = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    tracking_date = models.DateField(blank=True, null=True)

    # Managers
    objects = models.Manager()  # The default manager.
    ats_objects = AtsManager()  # The ATS manager.

    class Meta:
        db_table = 'ats_rhin'


class Rmel(models.Model):
    student_name = models.CharField(max_length=255, blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    official_class = models.CharField(max_length=255, blank=True, null=True)
    grade = models.CharField(max_length=255, blank=True, null=True)
    grade_level = models.CharField(max_length=255, blank=True, null=True)
    home_room = models.CharField(max_length=255, blank=True, null=True)
    meal_code = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    incomplete_reasons = models.CharField(max_length=255, blank=True, null=True)
    tracking_date = models.DateField(blank=True, null=True)
    school = models.CharField(max_length=255, blank=True, null=True)

    # Managers
    objects = models.Manager()  # The default manager.
    ats_objects = AtsManager()  # The ATS manager.

    class Meta:
        db_table = 'ats_rmel'


class Rnec(models.Model):
    dbn = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    grade_code = models.CharField(max_length=255, blank=True, null=True)
    grade_level = models.CharField(max_length=255, blank=True, null=True)
    off_class = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    hispanic = models.CharField(max_length=255, blank=True, null=True)
    american_indian_alaskan = models.CharField(max_length=255, blank=True, null=True)
    asian = models.CharField(max_length=255, blank=True, null=True)
    hawaiian_pacific_islander = models.CharField(max_length=255, blank=True, null=True)
    black = models.CharField(max_length=255, blank=True, null=True)
    white = models.CharField(max_length=255, blank=True, null=True)
    old_ethnic_code = models.CharField(max_length=255, blank=True, null=True)
    tracking_date = models.DateField(blank=True, null=True)

    # Managers
    objects = models.Manager()  # The default manager.
    ats_objects = AtsManager()  # The ATS manager.

    class Meta:
        db_table = 'ats_rnec'


class Rocl(models.Model):
    ocl = models.CharField(max_length=255, blank=True, null=True)
    room = models.CharField(max_length=255, blank=True, null=True)
    loc = models.CharField(max_length=255, blank=True, null=True)
    teacher = models.CharField(max_length=255, blank=True, null=True)
    advisor = models.CharField(max_length=255, blank=True, null=True)
    staff_1 = models.CharField(max_length=255, blank=True, null=True)
    staff_2 = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    dob = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    gl = models.CharField(max_length=255, blank=True, null=True)
    grade = models.CharField(max_length=255, blank=True, null=True)
    phone_num = models.CharField(max_length=255, blank=True, null=True)
    tracking_date = models.DateField(blank=True, null=True)
    school = models.CharField(max_length=255, blank=True, null=True)

    # Managers
    objects = models.Manager()  # The default manager.
    ats_objects = AtsManager()  # The ATS manager.

    class Meta:
        db_table = 'ats_rocl'


class Rpob(models.Model):
    last_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    grade = models.CharField(max_length=255, blank=True, null=True)
    grade_level = models.CharField(max_length=255, blank=True, null=True)
    official_class = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    x_coded = models.CharField(max_length=255, blank=True, null=True)
    place_of_birth = models.CharField(max_length=255, blank=True, null=True)
    home_language_code = models.CharField(max_length=255, blank=True, null=True)
    geo_code = models.CharField(max_length=255, blank=True, null=True)
    first_enter_nyc_date = models.CharField(max_length=255, blank=True, null=True)
    tracking_date = models.DateField(blank=True, null=True)
    school = models.CharField(max_length=255, blank=True, null=True)

    # Managers
    objects = models.Manager()  # The default manager.
    ats_objects = AtsManager()  # The ATS manager.

    class Meta:
        db_table = 'ats_rpob'


class Rsfm(models.Model):
    last_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    grade = models.CharField(max_length=255, blank=True, null=True)
    level = models.CharField(max_length=255, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=255, blank=True, null=True)
    admit_date = models.DateField(blank=True, null=True)
    admit_code = models.CharField(max_length=255, blank=True, null=True)
    admit_reason = models.CharField(max_length=255, blank=True, null=True)
    prev_school = models.CharField(max_length=255, blank=True, null=True)
    prev_grade = models.CharField(max_length=255, blank=True, null=True)
    prev_level = models.CharField(max_length=255, blank=True, null=True)
    prev_class = models.CharField(max_length=255, blank=True, null=True)
    prev_admit_date = models.DateField(blank=True, null=True)
    prev_admit_code = models.CharField(max_length=255, blank=True, null=True)
    prev_discharge_date = models.DateField(blank=True, null=True)
    prev_discharge_code = models.CharField(max_length=255, blank=True, null=True)
    tracking_date = models.DateField(blank=True, null=True)
    school = models.CharField(max_length=255, blank=True, null=True)

    # Managers
    objects = models.Manager()  # The default manager.
    ats_objects = AtsManager()  # The ATS manager.

    class Meta:
        db_table = 'ats_rsfm'


class Rspd(models.Model):
    network = models.CharField(max_length=255, blank=True, null=True)
    cluster = models.CharField(max_length=255, blank=True, null=True)
    cfn = models.CharField(max_length=255, blank=True, null=True)
    school_dbn = models.CharField(max_length=255, blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    grade = models.CharField(max_length=255, blank=True, null=True)
    level = models.CharField(max_length=255, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=255, blank=True, null=True)
    cap_class = models.CharField(max_length=255, blank=True, null=True)
    cap_data_as_of_dte = models.DateField(blank=True, null=True)
    first_attend_dte = models.DateField(blank=True, null=True)
    conference_dte = models.DateField(blank=True, null=True)
    cap_authorize_dte = models.DateField(blank=True, null=True)
    cap_disc_dte = models.DateField(blank=True, null=True)
    prog_recom_cde = models.CharField(max_length=255, blank=True, null=True)
    prog_recom_desc = models.CharField(max_length=255, blank=True, null=True)
    serv_ctgry = models.CharField(max_length=255, blank=True, null=True)
    serv_description = models.CharField(max_length=255, blank=True, null=True)
    prds_per_wk = models.CharField(max_length=255, blank=True, null=True)
    full_part_time = models.CharField(max_length=255, blank=True, null=True)
    disab_cde = models.CharField(max_length=255, blank=True, null=True)
    disab_desc = models.CharField(max_length=255, blank=True, null=True)
    tm_code_1 = models.CharField(max_length=255, blank=True, null=True)
    test_mod_description_1 = models.CharField(max_length=255, blank=True, null=True)
    tm_code_2 = models.CharField(max_length=255, blank=True, null=True)
    test_mod_description_2 = models.CharField(max_length=255, blank=True, null=True)
    tm_code_3 = models.CharField(max_length=255, blank=True, null=True)
    test_mod_description_3 = models.CharField(max_length=255, blank=True, null=True)
    tm_code_4 = models.CharField(max_length=255, blank=True, null=True)
    test_mod_description_4 = models.CharField(max_length=255, blank=True, null=True)
    tm_code_5 = models.CharField(max_length=255, blank=True, null=True)
    test_mod_description_5 = models.CharField(max_length=255, blank=True, null=True)
    tm_code_6 = models.CharField(max_length=255, blank=True, null=True)
    test_mod_description_6 = models.CharField(max_length=255, blank=True, null=True)
    tm_code_7 = models.CharField(max_length=255, blank=True, null=True)
    test_mod_description_7 = models.CharField(max_length=255, blank=True, null=True)
    tm_code_8 = models.CharField(max_length=255, blank=True, null=True)
    test_mod_description_8 = models.CharField(max_length=255, blank=True, null=True)
    tm_code_9 = models.CharField(max_length=255, blank=True, null=True)
    test_mod_description_9 = models.CharField(max_length=255, blank=True, null=True)
    tm_code_10 = models.CharField(max_length=255, blank=True, null=True)
    test_mod_description_10 = models.CharField(max_length=255, blank=True, null=True)
    promo_cde = models.CharField(max_length=255, blank=True, null=True)
    promo_desc = models.CharField(max_length=255, blank=True, null=True)
    wheelchair_yn = models.CharField(max_length=255, blank=True, null=True)
    cap_school = models.CharField(max_length=255, blank=True, null=True)
    class_in_cap = models.CharField(max_length=255, blank=True, null=True)
    te_code = models.CharField(max_length=255, blank=True, null=True)
    te_description = models.CharField(max_length=255, blank=True, null=True)
    cap_biling_cde = models.CharField(max_length=255, blank=True, null=True)
    cap_biling_desc = models.CharField(max_length=255, blank=True, null=True)
    rs_code_1 = models.CharField(max_length=255, blank=True, null=True)
    rs_description_1 = models.CharField(max_length=255, blank=True, null=True)
    freq_cde_1 = models.CharField(max_length=255, blank=True, null=True)
    dur_cde_1 = models.CharField(max_length=255, blank=True, null=True)
    gp_code_1 = models.CharField(max_length=255, blank=True, null=True)
    first_attd_dte_1 = models.DateField(blank=True, null=True)
    rs_code_2 = models.CharField(max_length=255, blank=True, null=True)
    rs_description_2 = models.CharField(max_length=255, blank=True, null=True)
    freq_cde_2 = models.CharField(max_length=255, blank=True, null=True)
    dur_cde_2 = models.CharField(max_length=255, blank=True, null=True)
    gp_code_2 = models.CharField(max_length=255, blank=True, null=True)
    first_attd_dte_2 = models.DateField(blank=True, null=True)
    rs_code_3 = models.CharField(max_length=255, blank=True, null=True)
    rs_description_3 = models.CharField(max_length=255, blank=True, null=True)
    freq_cde_3 = models.CharField(max_length=255, blank=True, null=True)
    dur_cde_3 = models.CharField(max_length=255, blank=True, null=True)
    gp_code_3 = models.CharField(max_length=255, blank=True, null=True)
    first_attd_dte_3 = models.DateField(blank=True, null=True)
    rs_code_4 = models.CharField(max_length=255, blank=True, null=True)
    rs_description_4 = models.CharField(max_length=255, blank=True, null=True)
    freq_cde_4 = models.CharField(max_length=255, blank=True, null=True)
    dur_cde_4 = models.CharField(max_length=255, blank=True, null=True)
    gp_code_4 = models.CharField(max_length=255, blank=True, null=True)
    first_attd_dte_4 = models.DateField(blank=True, null=True)
    rs_code_5 = models.CharField(max_length=255, blank=True, null=True)
    rs_description_5 = models.CharField(max_length=255, blank=True, null=True)
    freq_cde_5 = models.CharField(max_length=255, blank=True, null=True)
    dur_cde_5 = models.CharField(max_length=255, blank=True, null=True)
    gp_code_5 = models.CharField(max_length=255, blank=True, null=True)
    first_attd_dte_5 = models.DateField(blank=True, null=True)
    rs_code_6 = models.CharField(max_length=255, blank=True, null=True)
    rs_description_6 = models.CharField(max_length=255, blank=True, null=True)
    freq_cde_6 = models.CharField(max_length=255, blank=True, null=True)
    dur_cde_6 = models.CharField(max_length=255, blank=True, null=True)
    gp_code_6 = models.CharField(max_length=255, blank=True, null=True)
    first_attd_dte_6 = models.DateField(blank=True, null=True)
    rs_code_7 = models.CharField(max_length=255, blank=True, null=True)
    rs_description_7 = models.CharField(max_length=255, blank=True, null=True)
    freq_cde_7 = models.CharField(max_length=255, blank=True, null=True)
    dur_cde_7 = models.CharField(max_length=255, blank=True, null=True)
    gp_code_7 = models.CharField(max_length=255, blank=True, null=True)
    first_attd_dte_7 = models.DateField(blank=True, null=True)
    rs_code_8 = models.CharField(max_length=255, blank=True, null=True)
    rs_description_8 = models.CharField(max_length=255, blank=True, null=True)
    freq_cde_8 = models.CharField(max_length=255, blank=True, null=True)
    dur_cde_8 = models.CharField(max_length=255, blank=True, null=True)
    gp_code_8 = models.CharField(max_length=255, blank=True, null=True)
    first_attd_dte_8 = models.DateField(blank=True, null=True)
    rs_code_9 = models.CharField(max_length=255, blank=True, null=True)
    rs_description_9 = models.CharField(max_length=255, blank=True, null=True)
    freq_cde_9 = models.CharField(max_length=255, blank=True, null=True)
    dur_cde_9 = models.CharField(max_length=255, blank=True, null=True)
    gp_code_9 = models.CharField(max_length=255, blank=True, null=True)
    first_attd_dte_9 = models.DateField(blank=True, null=True)
    rs_code_10 = models.CharField(max_length=255, blank=True, null=True)
    rs_description_10 = models.CharField(max_length=255, blank=True, null=True)
    freq_cde_10 = models.CharField(max_length=255, blank=True, null=True)
    dur_cde_10 = models.CharField(max_length=255, blank=True, null=True)
    gp_code_10 = models.CharField(max_length=255, blank=True, null=True)
    first_attd_dte_10 = models.DateField(blank=True, null=True)
    tracking_date = models.DateField(blank=True, null=True)

    # Managers
    objects = models.Manager()  # The default manager.
    ats_objects = AtsManager()  # The ATS manager.

    class Meta:
        db_table = 'ats_rspd'


class Rtrr(models.Model):
    dbn = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    grade = models.CharField(max_length=255, blank=True, null=True)
    grade_level = models.CharField(max_length=255, blank=True, null=True)
    off_class = models.CharField(max_length=255, blank=True, null=True)
    opt_sch = models.CharField(max_length=255, blank=True, null=True)
    opt_grd = models.CharField(max_length=255, blank=True, null=True)
    distance = models.CharField(max_length=255, blank=True, null=True)
    metro_crd_type = models.CharField(max_length=255, blank=True, null=True)
    metro_crd_num = models.CharField(max_length=255, blank=True, null=True)
    bus_stop = models.CharField(max_length=255, blank=True, null=True)
    spec_ed = models.CharField(max_length=255, blank=True, null=True)
    var_no = models.CharField(max_length=255, blank=True, null=True)
    trans_stat = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city_state = models.CharField(max_length=255, blank=True, null=True)
    zip_cde = models.CharField(max_length=255, blank=True, null=True)
    street_cde = models.CharField(max_length=255, blank=True, null=True)
    phone_num = models.CharField(max_length=255, blank=True, null=True)
    change_date = models.DateField(blank=True, null=True)
    tracking_date = models.DateField(blank=True, null=True)

    # Managers
    objects = models.Manager()  # The default manager.
    ats_objects = AtsManager()  # The ATS manager.

    class Meta:
        db_table = 'ats_rtrr'
