from django.shortcuts import render


def about(request):
    """View функция для страницы about."""
    return render(request, 'pages/about.html')


def rules(request):
    """View функция для страницы с правилами."""
    return render(request, 'pages/rules.html')
