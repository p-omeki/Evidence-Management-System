from django.shortcuts import render


def home(request):
    context = {"section": "home"}
    template_name = "home.html"
    return render(request, template_name, context)


def about(request):
    return render(request, "about.html")


def features(request):
    return render(request, "features.html")


def services(request):
    return render(request, "services.html")


def contact(request):
    context = {"section": "contact"}
    template_name = "contact.html"
    return render(request, template_name, context)

def faqs(request):
    return render(request, "faqs.html")
