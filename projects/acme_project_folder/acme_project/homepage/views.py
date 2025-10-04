# from django.http import HttpResponse
# from django.template import loader

# def index(request):
#     template = loader.get_template('homepage/index.html')
#     return HttpResponse(template.render({}, request))

from django.shortcuts import render

def index(request):
    # хуй знает как добавить этот шаблон :(
    template_name = 'templates/index.html' 
    return render(request, template_name)