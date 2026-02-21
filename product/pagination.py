from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination

#LimitOffsetPagination
class CategoryPagination(LimitOffsetPagination):
  default_limit=2
  max_limit=5

#custom pagination with link of response in header 
class ProductPagination(PageNumberPagination):
  page_size=5
  def get_paginated_response(self,data):
    response= Response({
            'count': self.page.paginator.count,
            'results': data
            })
    links = []

    next_link = self.get_next_link()
    if next_link:
      links.append(f'<{next_link}>; rel="next"')

    prev_link = self.get_previous_link()
    if prev_link:
      links.append(f'<{prev_link}>; rel="prev"')

    if links:
      response['Link'] = ', '.join(links)

    return response