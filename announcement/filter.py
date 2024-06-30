import django_filters

from announcement.models import Adt


class AnnouncementFilter(django_filters.FilterSet):
    """Фильтр на поиск по названию объявление"""

    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = Adt
        fields = ["title"]
