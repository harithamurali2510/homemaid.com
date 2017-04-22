from django.contrib import admin

# Register your models here.
from .models import MaidSignUp
from .models import ClientSignUp
from .models import Akshaya

#class SignUpAdmin(admin.ModelAdmin):
#	model = SignUp
#	list_display = [ "__unicode__", "timestamp", "updated"]


admin.site.register(MaidSignUp)
admin.site.register(ClientSignUp)
admin.site.register(Akshaya)