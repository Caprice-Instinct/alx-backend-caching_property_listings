from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from .utils import get_all_properties
import json

@cache_page(60 * 15)
def property_list(request):
    properties = get_all_properties().values('id', 'title', 'description', 'price', 'location', 'created_at')
    response = HttpResponse(json.dumps(list(properties)), content_type='application/json')
    return response