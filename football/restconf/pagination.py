from rest_framework import pagination


class FootballAPIPagination(pagination.LimitOffsetPagination):
    default_limit   = 100
    max_limit       = 200
