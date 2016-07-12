from django.test import TestCase
from etl.matviews import matview_refresh
from .mv_models import (GetAllAtsReports,)


class MatviewModelSchemaTests(TestCase):

    def setUp(self):
        matview_refresh('test_dev')

    def test_get_all_ats_reports(self):
        try:
            a = GetAllAtsReports.objects.all()
        except:
            print(traceback.format_exc())
            print(sys.exc_info()[0])