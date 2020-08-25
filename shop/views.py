from django.shortcuts import render

offers = [
    {
        'developer': 'CD Projekt RED', 
        'name': 'The Witcher 3: Wild Hunt',
        'description': 'Greatest game of all time',
        'release_date': 'May 18, 2015'
    },
    {
        'developer': 'Arkane Studios', 
        'name': 'Dishonored 2',
        'description': 'Most creative game of all time',
        'release_date': 'November 11, 2016'
    }
]

def home(request):
    context = { 'offers': offers }
    return render(request, 'shop/home.html', context)
