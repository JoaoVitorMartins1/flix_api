from django.db.models import Avg
from rest_framework import serializers
from .models import Movie



class MoviesSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('O ano nao pode ser inferior a 1990')
        return value

    def get_rate(self, obj):#obj = cada filme
        rate=obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate,1)#para usar somente uma casa decimal
        return None
        #reviews = obj.reviews.all() esta indo ate reviews em movie (related name da ligaçao entre reviews e moviwe) e buscando o review
        # if reviews:
        #     sum_reviews = 0
        #     for review in reviews:
        #         sum_reviews+=review.stars
        #     reviews_count=reviews.count()
        #     return (sum_reviews / reviews_count,1)
        # return None

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('A descrição nao pode ultrapassar 200 caracters')
