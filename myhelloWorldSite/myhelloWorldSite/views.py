from django.template.loader import get_template
from django.template import Context
from django.http import Http404,HttpResponse
from django.shortcuts import render_to_response
import datetime
from contact.forms import ContactForm

def hello(request):
    return HttpResponse("Hello World")

def current_datetime(request):
    now=datetime.datetime.now()

    return render_to_response('current_datetime.html',{'current_date':now})

def hours_ahead(request,offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()
    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    assert False
    html="<html><body>In %s hours(s), it will be %s .</body></html>" %(offset, dt)
    return HttpResponse(html)


def contact(request):
    if request.method=='POST':
        form=ContctForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject':'I love this site!'}
            )
    return render_to_response('contact_form.html', {'form': form})
