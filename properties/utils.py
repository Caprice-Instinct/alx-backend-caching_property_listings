from django.core.cache import cache
from django_redis import get_redis_connection
from .models import Property
import logging

def get_all_properties():
    queryset = cache.get('all_properties')
    if queryset is None:
        queryset = Property.objects.all()
        cache.set('all_properties', queryset, 3600)
    return queryset

def get_redis_cache_metrics():
    redis_conn = get_redis_connection("default")
    info = redis_conn.info()
    
    hits = info.get('keyspace_hits', 0)
    misses = info.get('keyspace_misses', 0)
    total = hits + misses
    hit_ratio = hits / total if total > 0 else 0
    
    metrics = {
        'keyspace_hits': hits,
        'keyspace_misses': misses,
        'hit_ratio': hit_ratio
    }
    
    logging.info(f"Redis Cache Metrics - Hits: {hits}, Misses: {misses}, Hit Ratio: {hit_ratio:.2f}")
    return metrics