
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Kitablar, options3
from django.views.generic import View, ListView, DetailView
from django.contrib import messages
from django.utils.translation import gettext as _
import random


def about(request):
    from django.utils import translation
    #user_language = 'en'
    # translation.activate(user_language)
    # request.session[translation.LANGUAGE_SESSION_KEY] =
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]
    return render(request, 'about.html')


class index(ListView):
    def get(self, *args, **kwargs):
        keyword = self.request.GET.get('keyword', '')
        dil = self.request.GET.get('dil', '')
        if keyword or dil:
            data = Kitablar.objects.filter(
                Ad__contains=keyword, dil__contains=dil)
        else:
            data = Kitablar.objects.all()
        if not data:
            _messages.warning(self.request, "Axtarışa uyğun nəticə tapılmadı")
        return render(self.request, 'index.html', {'data': data})


class detail(ListView):
    template_name = 'detail.html'

    def get_queryset(self):
        self.data = get_object_or_404(Kitablar, id=self.kwargs['id'])
        return self.data

    def get_context_data(self, **kwargs):
        is_favorite = False
        if self.data.favourite.filter(id=self.request.user.id):
            is_favorite = True
        random_books = random.sample(list(Kitablar.objects.all()), 3)
        context = super().get_context_data(**kwargs)
        context['random_books'] = random_books
        context['data'] = self.data
        context['is_favorite'] = is_favorite
        return context

# Kateqoriyalar


class categories(ListView):
    template_name = 'categories.html'

    def get_queryset(self):
        keyword = self.request.GET.get('keyword', '')
        dil = self.request.GET.get('dil', '')
        if keyword or dil:
            self.janr = Kitablar.objects.filter(
                janr=self.kwargs['janr'], Ad__contains=keyword, dil__contains=dil)
        else:
            self.janr = Kitablar.objects.filter(janr=self.kwargs['janr'])
        if not self.janr:
            self.janr = Kitablar.objects.filter(janr=self.kwargs['janr'])
            messages.warning(self.request, "Axtarışa uyğun nəticə tapılmadı")
        return self.janr

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['janr'] = self.janr
        janrlar = set()
        for i in Kitablar.objects.exclude(janr=self.janr[0].janr):
            if i not in janrlar:
                janrlar.add((i.janr, i.get_janr_display()))
        context['janrlar'] = janrlar
        return context


def favourite_post(request, fav_id):
    items = get_object_or_404(Kitablar, id=fav_id)
    if request.method == 'POST':
        if items.favourite.filter(id=request.user.id).exists():
            items.favourite.remove(request.user)
            messages.warning(request, "Sevimlilərdən kənarlaşdırıldı")
        else:
            items.favourite.add(request.user)
            messages.info(request, "Sevimlilərə əlavə edildi")
    return redirect('books:detail', fav_id)


def favorite_list(request):
    user = request.user
    favorite_posts = user.favourite.all()
    context = {
        'favorite_posts': favorite_posts
    }
    return render(request, 'favourites.html', context)
