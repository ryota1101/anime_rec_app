#  APIの出力をJSON,XMLデータに変換
from rest_framework import serializers
from .models import Anime

class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime                    # 呼び出すモデル
        fields = ["anime_id","title","rating"]  # API上に表示するモデルのデータ項目