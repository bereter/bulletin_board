from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from .models import Post, Comment
from .filters import PostFilter
from .forms import CreateFormBoard, CreateFormComment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

class BoardList(ListView):
    model = Post
    ordering = '-date'
    template_name = 'board_posts.html'
    context_object_name = 'posts'
    paginate_by = 15

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class BoardDetail(FormMixin, DetailView):
    model = Post
    template_name = 'board_post.html'
    context_object_name = 'post'
    form_class = CreateFormComment

    def get_success_url(self):
        return reverse('post_detail', args=[str(self.get_object().id)])

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.post = self.get_object()
        self.object.save()
        return super().form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print(context['post'])
    #     return context


class BoardCreate(LoginRequiredMixin, CreateView):
    form_class = CreateFormBoard
    model = Post
    template_name = 'board_create_post.html'

    def form_valid(self, form):
        create_post = form.save(commit=False)
        create_post.user = self.request.user
        return super().form_valid(form)


class BoardUpdate(LoginRequiredMixin, UpdateView):
    form_class = CreateFormBoard
    model = Post
    template_name = 'board_create_post.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].user:
            return self.handle_no_permission()
        return kwargs


class BoardDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'board_delete.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        if self.request.user != self.object.user:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)



class BoardListUser(ListView):
    template_name = 'board_my_posts.html'
    context_object_name = 'posts'
    paginate_by = 15

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)


@login_required
def reply_on(request, pk):
    comment_obj = Comment.objects.get(id=pk)
    comment_obj.status_on()
    return redirect('post_detail', comment_obj.post_id)


@login_required
def reply_off(request, pk):
    comment_obj = Comment.objects.get(id=pk)
    comment_obj.status_off()
    return redirect('post_detail', comment_obj.post_id)
