from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect


def home(request):
    template_name = 'home.html'

    return render(request, template_name)

# def handler404(request, *args, **argv):
#     response = render_to_response('base_nav.html', {},
#                                   context_instance=RequestContext(request))
#     response.status_code = 404
#     return response
