from django.shortcuts import render_to_response
from contact.forms import ContactForm

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
        form = ContactForm(initial={'subject':'I lov this site'})
    return render_to_response('contact_form.html', {'form': form})
