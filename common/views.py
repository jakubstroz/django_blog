from django.shortcuts import render


def about_us(request):
    title = 'About us'
    context = {'title':title}
    return render(request, 'common/about.html', context)


def contact_view(request):
    title = 'Contact'
    context = {'title':title}
    return render(request, 'common/contact.html', context)