from django.shortcuts import render,HttpResponse
from .tasks import test_func
# Create your views here.
from send_mail_app.tasks import send_mail_func

def test(request):
    test_func.delay()
    return HttpResponse("done")

def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("sent")