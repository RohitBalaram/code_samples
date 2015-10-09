from rest_framework import renderers, generics
from . import serializers, models, mv_models


class AtsReportViewSet(generics.ListAPIView):
    renderer_classes = (renderers.JSONRenderer,)
    ats_report_map = {
        'rdgs': {'model': models.Rdgs},
        'rbir': {'model': models.Rbir},
        'rmel': {'model': models.Rmel},
        'rhin': {'model': models.Rhin},
        'rhil': {'model': models.Rhil},
        'rtrr': {'model': models.Rtrr},
        'radr': {'model': models.Radr},
        'rpob': {'model': models.Rpob},
        'rsfm': {'model': models.Rsfm},
        'rnec': {'model': models.Rnec},
        'rocl': {'model': models.Rocl},
        'rspd': {'model': models.Rspd},
        'radpa': {'model': models.Radpa},
        'radpd': {'model': models.Radpd},
        'all_reports': {'model': mv_models.GetAllAtsReports}
    }

    def get_queryset(self):
        report = self.kwargs['data_cache']
        self.serializer_class = serializers.AtsSerializer
        self.serializer_class.Meta.model = self.ats_report_map[report]['model']
        self.filter_fields = tuple(self.serializer_class.Meta.model._meta.get_all_field_names())
        queryset = self.serializer_class.Meta.model.objects.all()
        return queryset
