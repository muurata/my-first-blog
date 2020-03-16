from django.urls import path
from . import views
from .forms import PostForm

urlpatterns = [
    path('',views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    
]

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})