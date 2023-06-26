from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Genre, Anime, Genres, Utility
from .forms import SearchForm
from django.db.models import Q

class FirstIndexView(generic.TemplateView):
    template_name = 'index.html'

class IndexView(generic.ListView):
    model = Anime
    template_name = 'list.html'
    context_object_name = 'anime_list'
    paginate_by = 50
    
    def post(self, request, *args, **kwargs):
        form_value = [
            self.request.POST.get('title', None),
            self.request.POST.get('members', None),
            self.request.POST.get('rating', None),
        ]
        request.session['form_value'] = form_value
        # 検索時にページネーションに関連したエラーを防ぐ
        self.request.GET = self.request.GET.copy()
        self.request.GET.clear()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # sessionに値がある場合、その値をセットする。（ページングしてもform値が変わらないように）
        title = ''
        members = ''
        rating = ''
        if 'form_value' in self.request.session:
            form_value = self.request.session['form_value']
            title = form_value[0]
            members = form_value[1]
            rating = form_value[2]
        default_data = {'title': title,  # タイトル
                        'members': members,  # 登録者
                        'rating': rating,  # 評価
                        }
        test_form = SearchForm(initial=default_data) # 検索フォーム
        context['test_form'] = test_form
        return context
    
    def get_queryset(self):
        # sessionに値がある場合、その値でクエリ発行する。
        if 'form_value' in self.request.session:
            form_value = self.request.session['form_value']
            title = form_value[0]
            members = form_value[1]
            rating = form_value[2]
            # 検索条件
            condition_title = Q()
            condition_members = Q()
            condition_rating = Q()
            if len(title) != 0 and title[0]:
                condition_title = Q(title__icontains=title)
            if len(members) != 0 and members[0]:
                condition_members = Q(members__gt=members)
            if len(rating) != 0 and rating[0]:
                condition_rating = Q(rating__gt=rating)
            return Anime.objects.select_related().filter(condition_title & condition_members & condition_rating)
        else:
            # 全て返す
            return Anime.objects.all()
    

class GenreView(generic.ListView):
    template_name = 'list_genre.html'
    context_object_name = 'genre_list'
    paginate_by = 2
    def get_queryset(self):
        return Anime.objects.all()
    
class DetailView(generic.DetailView):
    model = Anime
    template_name = 'detail.html'