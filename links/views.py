from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import LinkForm
from .models import Link
from .utilities import getFreeLink

LENGTH_OF_SHORT_LINK = 6


def start_page(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            l = Link()
            l.orginal_url = form.cleaned_data.get('link')
            l.short_url = getFreeLink(6)
            l.clicked = 0
            l.save()

            context = {
                'orginal_url': l.orginal_url,
                'short_url': l.short_url,
            }
            return render(request, 'detail.html', context)
    else:
        return render(request, "index.html", {})


def redirect_page(request, link):
    l = Link.objects.filter(short_url=link).first()
    l.clicked = l.clicked + 1
    l.save()

    return HttpResponseRedirect(l.orginal_url)


def stats_page(request, link):
    l = Link.objects.filter(short_url=link).first()

    context = {
        "orginal": l.orginal_url,
        "clicked": l.clicked,
    }

    return render(request, "stats.html", context)
