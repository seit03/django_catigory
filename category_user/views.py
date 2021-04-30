from unicodedata import category

from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView

from category_user.forms import CommentForm
from category_user.models import Category, TVShow, Comment


class CategoryListView(ListView):
    model = category
    template_name = 'category/category_list.html'

    def get_queryset(self):
        return Category.objects.all()


class CategoryDetailList(DetailView):
    model = Category
    template_name = 'category/category_detail_list.html'


class TVShowListView(ListView):
    model = TVShow
    template_name = 'category/tvshow_list.html'

    def get_queryset(self):
        return TVShow.objects.all()


class TVShowDetailView(DetailView):
    model = TVShow
    template_name = 'category/tvshow_detail_list.html'
    extra_context = {'form': CommentForm()}

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        if request.user:
            show_id = kwargs['pk']
            show = TVShow.objects.get(pk=show_id)
            form = CommentForm(request.POST, initial={'show': show})
            if form.is_valid():
                form.seve()
        return self.get(request, *args, **kwargs)


class CommentListView(ListView):
    model = Comment
    template_name = 'category/comment_list.html'

    def get_queryset(self):
        return Comment.objects.all()


class CommentDetailView(DetailView):
    model = Comment
    template_name = 'category/comment_detail_list.html'
