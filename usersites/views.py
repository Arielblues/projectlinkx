from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Usersites, Sitecategory
from bootstrap_modal_forms.generic import BSModalCreateView
from .forms import BookModelForm, UrlModelForm
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView, 
    DeleteView,
)

# Create your views here.
@login_required
def xhomeuser(request):
    """ Show the user his/her list of books. """
    user = instance=request.user
    username = User.objects.get(username=user.username)

    context = {
        "authors": list(Usersites.objects.filter(author=username).order_by('author').values_list('author', flat=True).distinct()),
        "posts": Usersites.objects.filter(author=username),
       # "genres": list(Post.objects.filter(user=username).order_by().values_list('title', flat=True).distinct()),
       # "user": str(user)
    }
    return render(request, 'usersites/home.html', context)



class xPostListView(ListView):
    model = Usersites
    template_name = 'usersites/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2


class xUserPostListView(ListView):
    model = Usersites
    template_name = 'usersites/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Usersites.objects.filter(author=user).order_by('-date_posted')


class xPostDetailView(DetailView):
    model = Usersites


class xPostCreateView(LoginRequiredMixin, CreateView):
    model = Usersites
    #fields = ['url', 'country', 'language', 'categories']
    form_class = UrlModelForm


    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)  # Get the form as usual
        user = self.request.user
        form.fields['categories'].queryset = Sitecategory.objects.filter(author=user)
        return form




    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class xPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Usersites
    fields = ['country', 'language']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class xPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Usersites
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



class SitecategoryCreateView(LoginRequiredMixin, CreateView):
    model = Sitecategory
    fields = ['title', 'slug', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class SitecategoryDetailView(DetailView):
    model = Sitecategory




# Create your views here.
@login_required
def xxhomeuser(request):
    """ Show the user his/her list of books. """
    user = instance=request.user
    username = User.objects.get(username=user.username)
    model = Sitecategory
    fields = ['title', 'slug', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    context = {
        "authors": list(Sitecategory.objects.filter(author=username).order_by('author').values_list('author', flat=True).distinct()),
        "posts": Sitecategory.objects.filter(author=username),
       # "genres": list(Post.objects.filter(user=username).order_by().values_list('title', flat=True).distinct()),
       # "user": str(user)
    }
    return render(request, 'usersites/home2.html', context)


class BookCreateView(BSModalCreateView):
    template_name = 'usersites/sitecategoryform2.html'
    form_class = BookModelForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('xxblog-homeuser')




    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
def xxxhomeuser(request):

    logged_in_user = request.user
    logged_in_user_posts = Sitecategory.objects.filter(author=user)

    return render(request, 'usersites/home2.html', {'posts': logged_in_user_posts})