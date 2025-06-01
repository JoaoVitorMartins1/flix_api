from reviews.models import Review
from django.contrib import admin

admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display=('id','movie','stars','comment')