from django.contrib import admin
from .models import Answer,Question,Attemtnumber,Category
# Register your models here.


class AttemptAdmin(admin.ModelAdmin):
    list_display=["student","marks","noattempt","totalattemptquestion","toatalquestion"]

admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Attemtnumber,AttemptAdmin)
admin.site.register(Category)
