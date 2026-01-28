from django.db.models import Max
from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models.product import Product
from product.serializers.product_info_serializer import ProductInfoSerializer

@api_view(['GET'])
def product_info(request):
  products_qs= Product.objects.all()
  count= products_qs.count()
  max_price=products_qs.aggregate(max_price=Max('price'))['max_price'] # aggregate() returns a dict so to extract the value you are using 'products.aggregate(...)[ 'max_price' ]'
  products=list(products_qs)
  serializer= ProductInfoSerializer({
    'products':products,
    'count': count,
    'max_price':max_price
  })
  return Response(serializer.data)