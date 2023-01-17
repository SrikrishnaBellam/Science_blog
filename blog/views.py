from django.views import generic
from django.shortcuts import render
from .models import Post, steps

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    def get_object(self):
        return get_object_or_404(Model2, pk=self.kwargs['pk'], using='database2')
    # model = Post
    # template_name = 'post_detail.html'
    
class DisplayDataView(View):
    def get(self, request, pk=None):
        if pk:
            model2 = PostDetail.as_view()(request, pk=pk)
            return model2
        else:
            model1 = stepsList.as_view()(request)
            return model1

class stepsList(Listview):
     model = steps
     template_name = 'post_detail.html'

# def get_step():
#     return steps.objects.all()[0:3]