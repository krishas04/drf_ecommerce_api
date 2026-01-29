from rest_framework.views import APIView
from django.db.models import Max
from rest_framework.response import Response

from product.models.product import Product
from product.serializers.product_info_serializer import ProductInfoSerializer

class ProductInfoAPIView(APIView):
  def get(self,request):
    qs= Product.objects.only('id','name','price')
    data={
      'products': qs,
      'count': qs.count(),
      'max_price': qs.aggregate(max_price=Max('price'))['max_price'] # aggregate() returns a dict so to extract the value you are using 'products.aggregate(...)[ 'max_price' ]'
    }
    return Response(ProductInfoSerializer(data).data)
