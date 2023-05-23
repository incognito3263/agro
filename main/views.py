from django.conf import settings
from django.shortcuts import render

from main.forms import Sendd
from main.models import Product, News, Gallery, Send, Pdf
from django.core.mail import send_mail
from agro.settings import BASE_DIR
from django.http import FileResponse, HttpResponse
from django.http import HttpResponseRedirect
import io, os






def venue_pdf(request, pk):
    vanue = Pdf.objects.get(pk=pk)

    absolute_url = str(BASE_DIR) + vanue.pdf.url
    with open(absolute_url, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type="application/pdf")
        response['Content-Disposition'] = "attachment; filename" + vanue.pdf.name
        return response





def home(request):
    nows = News.objects.order_by("-id")[:3]

    tex = {
        "nows": nows
    }

    return render(request, 'main/index.html', tex)






def servicer(request):
    pro = Product.objects.all()

    ctx = {
        "pro": pro
    }
    return render(request, 'main/services.html', ctx)


def gallery(request):
    gel = Gallery.objects.all()

    ctx = {
        "gel": gel
    }
    return render(request, 'main/gallery.html', ctx)


def contact(request):
    model = Send()
    form = Sendd(request.POST,instance=model)
    if request.POST:
        if form.is_valid():
            data = request.POST
            form.save()
            message = f"Xabar keldi:\nIsmi: {data['full']}\nEmail: {data['email']}\nMavzu: {data['subject']}\nXabar: {data['message']}"
            # print(message, 'SALOM')
            subject = 'Saytdan'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['gulbaba@agrobusinessllc.com', 'info@agrobusinessllc.com']
            send_mail(subject, message, email_from, recipient_list)


    return render(request, 'main/contact.html',{"form":form})


def news(request):
    nows = News.objects.all()
    pdf = Pdf.objects.all()

    tex = {
        "nows": nows,
        'pdf': pdf
    }

    return render(request, 'main/news.html', tex)
