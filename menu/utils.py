import keyword
from re import search
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from menu.models import Dishs


def q_search(query):

    # if query.isdigit() and len(query) <= 5:
    #     return Dishs.objects.filter(id=int(query))

    vector = SearchVector("name", "description")
    query = SearchQuery(query)

    return (
        Dishs.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )

    # keywords = [word for word in query.split() if len(word) > 2]

    # q_objects = Q()

    # for token in keywords:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(name__icontains=token)

    # return Dishs.objects.filter(q_objects)
