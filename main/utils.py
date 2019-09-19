from rest_framework import serializers
from shop.models import Product

from .models import Order
from .serializers import OrderSerializer

class Utils(object):

    @staticmethod
    def get_order(request):
        partner = request.user.partner
        order_id = partner.last_order_id or request.session.get('order_id')
        order = None
        if order_id:
            last_order = Order.objects.filter(pk=order_id).first()
            # raise Warning(last_order.status)
            if last_order and last_order.status=='draft':
                return last_order
        
        order = Order(partner=partner)
        orderserializer = OrderSerializer(data=dict(partner=request.user.partner.id))
        orderserializer.is_valid(raise_exception=True)
        order = orderserializer.save()
        partner.last_order_id = order.id
        partner.save()
        request.session['order_id'] = order.id
        return order

    @staticmethod
    def validate_product_qty(data):
        product_id, quantity= data.get('product'), data.get('quantity') 
        product_obj = None 
        errors = []
        if not product_id:
            errors.append({'product':'Missing Product ID.'})
        else:
            product_obj = Product.objects.filter(pk=product_id).first()
            if not product_obj:
                errors.append({'product':'Invalid Product ID.'})
        if not quantity:
            errors.append({'quantity':'Missing Product Quantity.'})
        if len(errors):
            raise serializers.ValidationError(errors)
        return product_obj, quantity
