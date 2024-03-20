from django.shortcuts import render ,HttpResponseRedirect
from website.forms import newslettr , ContactForms
from django.contrib import messages
# Create your views here.
def index_view(request):
    return render(request, 'web/index.html')

def about_view(request):
    return render(request, 'web/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForms(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.name = "ananymous"
            contact.save()
            messages.add_message(request,messages.SUCCESS,'your tikct submited successfuly')
        else:
            messages.add_message(request,messages.ERROR,'your tikct didnt submited')
    else:
        form = ContactForms()
    return render(request, 'web/contact.html', {'form': form})

def newsletter(request):
    if request.method == 'POST':
        form=newslettr(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your tikct submited successfuly')
            return HttpResponseRedirect('blog/')
        else:
            messages.error(request, 'Your ticket did not submit')
            return HttpResponseRedirect('blog/')
    else:
        return HttpResponseRedirect('blog/')
