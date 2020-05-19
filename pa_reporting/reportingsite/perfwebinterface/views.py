from django.shortcuts import render

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Performance Auto',
        'content': 'Test Content',
        'date_posted': 'August 27, 2019'
    },
{
        'author': 'Janes',
        'title': 'Performance Auto2',
        'content': 'Second Test Content',
        'date_posted': 'August 28, 2019'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'perfwebinterface/perfwebinterface.html', context)

def results(request):
    return render(request, 'perfwebinterface/results.html')

def compare(request):
    return render(request, 'perfwebinterface/compare.html')

def statistics(request):
    return render(request, 'perfwebinterface/statistics.html')

def links(request):
    return render(request, 'perfwebinterface/links.html')

def contact(request):
    return render(request, 'perfwebinterface/contact.html')

def about(request):
    return render(request, 'perfwebinterface/about.html')


