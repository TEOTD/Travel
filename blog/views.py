from django.shortcuts import render, redirect
from .models import Post, Places, Book
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import comment

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def home(request):
    return render(request, 'blog/no-auth.html')


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


@login_required
def user_auth(request):
    print(request.user.is_superuser)
    if request.user.is_superuser == True:
        return redirect('users-admin')
    context = {
        'places': Places.objects.all()
    }
    return render(request, 'blog/auth.html', context)


@login_required
def user_admin(request):
    context = {
        'places': Places.objects.all(),
        'books': Book.objects.all(),
        'comm': comment.objects.all()
    }
    return render(request, 'blog/admin.html', context)


class PostListView(ListView):
    model = Places
    template_name = 'blog/admin.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'places'


class PostDetailView(DetailView):
    model = Places


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Places
    fields = ['id', 'name', 'price', 'per',
              'adv1', 'adv2', 'adv3', 'adv4', 'amount']

    def form_valid(self, form):
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Places
    fields = ['id', 'name', 'price', 'per',
              'adv1', 'adv2', 'adv3', 'adv4', 'amount']

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        place = self.get_object()
        return True


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Places
    success_url = '/home'

    def test_func(self):
        place = self.get_object()
        return True

# class PostDeleteView1(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Book
#     success_url = '/home'
#
#     def test_func(self):
#         book= self.get_object()
#         return True
