from django.shortcuts import render


def get_page(request):
    return render(request, template_name='page.html')
