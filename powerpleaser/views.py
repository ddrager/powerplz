from django.http import HttpResponse


def home(response):
    html = "<html><body>This is the powerpleaser app. Hello there!</body></html>"
    return HttpResponse(html)

