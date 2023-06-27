from .models import Anime                       # モデル呼出
from rest_framework.generics import ListAPIView, RetrieveAPIView    # API
from .serializers import SampleSerializer  # APIで渡すデータをJSON,XML変換

class api(ListAPIView):
    # 対象とするモデルのオブジェクトを定義
    queryset = Anime.objects.all()[0:10]

    # APIがデータを返すためのデータ変換ロジックを定義
    serializer_class = SampleSerializer

    # 認証
    permission_classes = []
    
class api_key(RetrieveAPIView):
    # 対象とするモデルのオブジェクトを定義
    queryset = Anime.objects.all()

    # APIがデータを返すためのデータ変換ロジックを定義
    serializer_class = SampleSerializer

    # 認証
    permission_classes = []