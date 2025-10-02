from django.http import HttpResponse

# Create your views here.
def product_list(request):
    return HttpResponse('catalog')
def product_detail():
    pass
def product_category(request, category):
    return HttpResponse(f'Категория {category}')