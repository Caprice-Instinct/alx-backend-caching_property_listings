from django.http import JsonResponse
from .utils import get_all_properties

def property_list(request):
    properties = get_all_properties().values('id', 'title', 'description', 'price', 'location', 'created_at')
    return JsonResponse(list(properties), safe=False)