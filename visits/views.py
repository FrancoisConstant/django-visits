import json

from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods

from .models import VisitCount
from .services import update_visit_count


@require_http_methods(["POST"])
def count_visit_ajax(request):
    """ add 1 visit if everything is OK, cf.update_visit_count """
    if not request.is_ajax():
        raise Http404()

    visit_count = get_object_or_404(VisitCount, id=request.POST.get('visit_count_id'))
    update_visit_count(request, visit_count)

    return HttpResponse(json.dumps({'status': True}), mimetype="application/json")