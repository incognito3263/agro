from django.contrib import admin

from .models import Product, News, Gallery, Send, Pdf


admin.site.register(News),
admin.site.register(Product),
admin.site.register(Gallery),
admin.site.register(Send),
admin.site.register(Pdf),
