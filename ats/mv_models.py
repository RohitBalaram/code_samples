from django.db import models


class GetAllAtsReports(models.Model):
    id = models.IntegerField(null=True)
    token = models.CharField(max_length=255, null=True)
    report_title = models.CharField(max_length=255, null=True)
    has_charts = models.CharField(max_length=255, null=True)
    school = models.CharField(max_length=255, null=True)
    tracking_date = models.DateField(null=True)

    class Meta:
        db_table = 'get_all_ats_reports'
        managed = False
        app_label = 'ats'
