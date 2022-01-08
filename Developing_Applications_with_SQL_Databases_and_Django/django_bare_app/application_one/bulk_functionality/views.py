from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    # Creates a basic html page using a string
    template = "<html>" \
               "This is a view" \
               "</html>"
    # Returns the template as a content response
    return HttpResponse(content=template)

from datetime import date

def get_date(request):
    today = date.today()
    template = "<html> Today's date is: {}".format(today)
    return HttpResponse(content=template)