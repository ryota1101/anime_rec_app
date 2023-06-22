from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Genre(models.Model):
    """ジャンルマスタ"""
    name = models.CharField(max_length=30,unique=True)
    en_name = models.CharField(max_length=30)

    def __str__(self):
        return self.name;

class Studio(models.Model):
    """スタジオマスタ"""
    name = models.CharField(max_length=50,unique=True)
    en_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name;

class Media(models.Model):
    """メディアマスタ"""
    name = models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.name;

class Year(models.Model):
    """年マスタ"""
    num = models.IntegerField(unique=True)

    def __str__(self):
        return self.num;
    
class Season(models.Model):
    """季節マスタ"""
    name = models.CharField(max_length=10,unique=True)
    en_name = models.CharField(max_length=10)

    def __str__(self):
        return self.name;

class Source(models.Model):
    """原作マスタ"""
    name = models.CharField(max_length=30,unique=True)
    en_name = models.CharField(max_length=30)

    def __str__(self):
        return self.name;
    
class Anime(models.Model):
    """アニメテーブル"""
    anime_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    en_title = models.CharField(max_length=200)
    media = models.ForeignKey(Media, on_delete=models.SET_NULL,null=True)
    episodes = models.IntegerField()
    rating = models.FloatField()
    members =  models.IntegerField()
    year = models.ForeignKey(Year, on_delete=models.SET_NULL,null=True)
    season = models.ForeignKey(Season, on_delete=models.SET_NULL,null=True)
    source = models.ForeignKey(Source, on_delete=models.SET_NULL,null=True)
    synopsis = models.TextField()
    website = models.URLField()
    image_path = models.CharField(max_length=400)

    def __str__(self):
        return self.anime_id;

class Genres(models.Model):
    """ジャンルテーブル"""
    anime_id = models.ForeignKey(Anime, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.anime_id;

class Studios(models.Model):
    """スタジオテーブル"""
    anime_id = models.ForeignKey(Anime, on_delete=models.CASCADE)
    studio = models.ForeignKey(Studio, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.anime_id;

class Utility(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.key;