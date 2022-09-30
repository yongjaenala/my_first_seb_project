from django.shortcuts import render
from django.views.generic import *

from boards.models import Board

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin

from django.conf import settings
# Create your views here.

#---ListView

class BoardLV(ListView):
    model = Board
    template_name = 'boards/board_list.html'
    context_object_name = 'boards'
    paginate_by = 3

#---DetailView
class BoardDV(DetailView):
    model = Board

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"boards-{self.object.id}-{self.object.slug}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.slug}"
        return context



class BoardCreateView(LoginRequiredMixin, CreateView):
    model = Board
    fields = ['title', 'slug', 'content',]
    initial = {'slug' : '자동으로_완성되니_적지마세요'}
    # fields=['title', 'description', 'content', 'tags']
    success_url = reverse_lazy('boards:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class BoardChangeLV(LoginRequiredMixin, ListView):
    template_name = 'boards/board_change_list.html'

    def get_queryset(self):
        return Board.objects.filter(owner = self.request.user)

class BoardUpdateView(OwnerOnlyMixin, UpdateView):
    model = Board
    fields = ['title', 'slug', 'content']
    success_url = reverse_lazy('boards:index')

class BoardDeleteView(OwnerOnlyMixin, DeleteView):
    model = Board
    success_url = reverse_lazy('boards:index')

    