from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import \
    CreateView, \
    DetailView, \
    ListView, \
    UpdateView, \
    DeleteView

from .models import Post, Category

# View function:
# func: request -> HTTPRespnse

# def post_list(request, param):
#    if request.method == 'GET':
#        object_list = Post.objects.all()
#        return render(request, 'posts/post_list.html', {'blog_posts': Paginate(object_list, 2)})

# Class-based Views:

class PostDetail(DetailView):
    model = Post


class PostList(ListView):
    model = Post
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all
        return context


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'description', 'content']


class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'description', 'content']


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog')


class CategoryList(ListView):
    model = Category


class CategoryDetail(DetailView):
    model = Category
    latest_post_numbers = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_posts'] = self.get_object().post_set.all()[:self.latest_post_numbers]
        context['posts_number'] = self.get_object().post_set.count()
        return context

