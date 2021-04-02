from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View, TemplateView, ListView, DetailView
from apps.matbuot.models import Yangiliklar
from .models import *
from django.shortcuts import render
from .forms import ContactForm, SendEmailForm
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib import messages


class HomePage(View):
    template_name = 'home/index.html'

    def get(self, request):
        yangilik = Yangiliklar.objects.order_by('-created')[:6]
        context = {
            'yangilik': yangilik,
        }
        return render(request, self.template_name, context)


class Aloqalar(TemplateView):
    template_name = 'home/aloqa.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["qr"] = Aloqa.objects.get(pk=1)
        except ObjectDoesNotExist:
            context["qr"] = []
        return context


class AloqaSendEmailView(View):
    template_name = 'home/aloqa.html'

    def get(self, request):
        obj = Aloqa.objects.first()
        form = SendEmailForm(request.POST)
        context = {"address": obj, "aloqa": form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = SendEmailForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            email_context = {
                'subject': data['subject'],
                'first_name': data['first_name'],
                'email': data['email'],
                'phone': data['phone'],
                'message': data['message']
            }
            message = {"message": "", "color": ""}
            try:
                from_email = settings.DEFAULT_FROM_EMAIL
                # to_email = 'info@alfraganus-ntm.uz'
                to_email = 'zokirhal@gmail.com'
                html_ = get_template("home/message.html").render(dict(email_context))
                subject = "Online Murojat"
                content = ""
                msg = EmailMultiAlternatives(subject, content, from_email, [to_email])
                msg.attach_alternative(html_, "text/html")
                w = msg.send()
                messages.success(request, 'Письмо отправлено!')
                layout = 'home/success.html'
                message['message'] = "Sizning xabaringiz muvaffaqiyatli junatildi!"
                message['color'] = "green"
                return render(request, layout, message)
            except Exception as e:
                messages.error(request, 'Ошибка отправки')
                layout = 'home/success.html'
                message['message'] = "Xabarni junatishda xatolik yuz berdi. Iltimos keyinroq qayta harakat qiling!"
                message['color'] = "red"
                return render(request, layout, message)
        else:
            return render(request, self.template_name, {"error": "Ошибка регистрации"})


class MaktabHaqida(TemplateView):
    template_name = 'maktab/maktab_haqida.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Maktab haqida'
        return context


class MaktabRamzi(TemplateView):
    template_name = 'maktab/maktab_ramzi.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Maktab ramzi'
        return context


class SendEmail(View):

    template_name = 'home/online_ariza.html'

    def get(self, request):
        form = ContactForm(request.POST)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            email_context = {
                'pupil_lastname': data['pupil_lastname'],
                'pupil_firstname': data['pupil_firstname'],
                'pupil_birthday': data['pupil_birthday'],
                'pupil_class': data['pupil_class'],
                'mother_lastname': data['mother_lastname'],
                'mother_firstname': data['mother_firstname'],
                'mother_birthday': data['mother_birthday'],
                'mother_work': data['mother_work'],
                'mother_phone': data['mother_phone'],
                'mother_email': data['mother_email'],
                'father_lastname': data['father_lastname'],
                'father_firstname': data['father_firstname'],
                'father_birthday': data['father_birthday'],
                'father_work': data['father_work'],
                'father_phone': data['father_phone'],
                'father_email': data['father_email'],
            }
            send = self.send_mail(context=email_context)
            msg = {"message": "", "color": ""}
            if send == 1:
                messages.success(request, 'Письмо отправлено!')
                layout = 'home/success.html'
                msg['message'] = "Sizning Arizangiz qabul qilindi!"
                msg['color'] = "green"
                return render(request, layout, msg)
            else:
                messages.error(request, 'Ошибка отправки')
                layout = 'home/success.html'
                msg['message'] = "Arizani junatishda xatolik yuz berdi. Iltimos keyinroq qayta harakat qiling!"
                msg['color'] = "red"
                return render(request, layout, msg)
        else:
            return render(request, self.template_name, {"error": "Ошибка регистрации"})

    @staticmethod
    def send_mail(context):
        from_email = settings.DEFAULT_FROM_EMAIL
        # to_email = 'info@alfraganus-ntm.uz'
        to_email = 'zokirhal@gmail.com'
        html_ = get_template("home/ariza.html").render(dict(context))
        subject = "Online Ariza"
        content = ""
        msg = EmailMultiAlternatives(subject, content, from_email, [to_email])
        msg.attach_alternative(html_, "text/html")
        sent = msg.send()
        return sent


class Savollar(ListView):
    model = Savollar
    template_name = 'home/savollar.html'
    context_object_name = 'savollar'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Savollar va Javoblar'
        return context


class MaintanceView(TemplateView):
    template_name = 'home/maintance.html'


class FatherAndMotherListView(ListView):
    model = FatherAndMother
    context_object_name = 'father_mother'
    template_name = 'home/ota-ona-list.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_top"] = 'Ota-Ona'
        context['header_title'] = 'Ota-Onalar'
        return context

    def get_queryset(self):
        return FatherAndMother.objects.filter(published=True).order_by('-id')


class FatherAndMotherDetailView(DetailView):
    model = FatherAndMother
    template_name = 'home/ota-ona-detail.html'
    context_object_name = 'jarayon'
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_top"] = 'JARAYON'
        return context
