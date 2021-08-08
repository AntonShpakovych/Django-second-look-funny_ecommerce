from django.contrib import admin
from .models import Laptop, Mobile, PC_table


admin.site.register(Laptop)
admin.site.register(PC_table)
admin.site.register(Mobile)
