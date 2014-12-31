from django import template
from django.contrib.contenttypes.models import ContentType
from visits.models import VisitCount

register = template.Library()


@register.inclusion_tag(file_name="visits/includes/count_visit.html", takes_context=True)
def count_visit_ajax(context, item):
    """ prepare the Ajax call to count the visit """
    item_type = ContentType.objects.get_for_model(item)
    visit_count, created = VisitCount.objects.get_or_create(
        item_type=item_type,
        item_id=item.id
    )
    return {'visit_count': visit_count}