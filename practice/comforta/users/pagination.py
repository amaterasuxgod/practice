from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class PostPageNumberPagination(PageNumberPagination):
    page_size = 3
