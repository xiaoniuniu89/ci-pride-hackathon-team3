from django.shortcuts import render


def donate(request):
    """ A view to return the donation page """
    return render(request, 'charity/charity.html')
