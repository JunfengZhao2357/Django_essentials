from django.shortcuts import render
from django.db.models import Value, DecimalField
from django.db.models import Q, F, Func, Count, ExpressionWrapper
from django.db.models.functions import Concat
from django.http import HttpResponse
from store.models import Product, OrderItem, Customer, Collection


# Create your views here.
# Handle request and send response

def say_hello(request):
    # Update objects (update data in DB)
    collection = Collection.objects.get(pk=11)
    # we can't use collection = Collection(pk=11) 
    # since in this way, if we don't update title
    # Django will give title an empty value bu default
    collection.featured_product = None
    collection.save()
    
    # Second method  faster one
    Collection.objects.filter(pk=11).update(featured_product=None)
    
    
    # Create objects (Insert data into DB)
    # collection = Collection()
    # collection.title = 'Video Games'
    # collection.featured_product = Product(pk=1)
    # collection.save()
    
    # Expression wrapper
    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # query_set = Product.objects.annotate(
    #     discount_price=discounted_price
    # )
    
    # Grouing data
    # in customer model, we don't have the order field 
    # but in order model, customer is a foreign key
    # then in customer table, the 'order' will be used as a field in Django
    # query_set = Customer.objects.annotate(
    #     orders_count=Count('order')
    # )
    
    
    # Calling DataBase function
    # query_set = Customer.objects.annotate(
    #     # CONCAT
    #     full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')
    # )
    # # using Django database functions to achieve this
    # query_set = Customer.objects.annotate(
    #     # CONCAT
    #     full_name=Concat('first_name', Value(' '), 'last_name')
    # )
    
    
    # Annotate a Object
    # query_set = Customer.objects.annotate(new_id=F('id') + 1)
    
    # Select exact fields only in the Query
    # Select products that have been ordered and sort them by title
    # query_set = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    
    
    # Limit result:
    # 5, 6, 7, 8, 9
    # query_set = Product.objects.all()[5:10]
    
    # Sorting
    # Sort the unit price in the ASC order , if there are same ones, sort the title in DSC
    # and then reverse the result
    # query_set = Product.objects.order_by('unit_price', '-title').reverse()
    
    
    # compare for two fields:
    # Products: inventory = price
    # query_set = Product.objects.filter(inventory=F('unit_price'))
    
    # Products: inventory < 10 AND price < 20
    # query_set = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
    # Products: inventory < 10 OR price < 20, we need to use Q object to realize 'OR'
    # query_set = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    # Q and: Q(inventory__lt=10) & Q(unit_price__lt=20)
    # not Q: ~Q(inventory__lt=10)
    
    # filtered_set = query_set.filter(unit_price__gt=20)
    # filtered_set_2 = query_set.filter(unit_price__range=(20,30))
    
    # we can use 'pk' instead of 'id' to search for id=1 product
    # 'pk' stands for primary key and we can also use id=1 to search
    # product = Product.objects.get(pk=1)
    
    # get the total number of how many items in the table
    # total_num = Product.objects.count()
    
    # we can also filter the all query set 
    # eg, 
    # filtered_set = query_set.filter().filter().order_by()
    return render(request, 'hello.html', {'name': 'Junfeng'})