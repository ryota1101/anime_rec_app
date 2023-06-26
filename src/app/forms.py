from django import forms
from .models import Anime

class SearchForm(forms.Form):
    title = forms.CharField(
        initial='',
        label='タイトル',
        required = False, # 必須ではない
    )
    members = forms.IntegerField(
        initial='',
        label='登録者(上)',
        required=False,  # 必須ではない
    )
    rating = forms.FloatField(
        initial='',
        label='評価スコア(上)',
        required=False,  # 必須ではない
    )