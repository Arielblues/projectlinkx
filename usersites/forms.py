#forms.py
from bootstrap_modal_forms.mixins import LoginAjaxMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Sitecategory, Usersites
from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms

class BookModelForm(LoginRequiredMixin, BSModalModelForm):
    class Meta:
        model = Sitecategory
        fields = ['title', 'slug', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UrlModelForm(LoginRequiredMixin, forms.ModelForm):




    class Meta:
        model = Usersites
        fields = ['url', 'country', 'language', 'categories', 'kwordsss']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)