from django.contrib import admin

from django.utils.html import format_html
from django.utils.safestring import mark_safe

from rest_framework.authtoken.admin import TokenAdmin


from django.contrib.admin.widgets import AdminFileWidget 
from django.utils.safestring import mark_safe
from django.forms.widgets import FileInput 

from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld

from django.contrib.auth.admin import UserAdmin


from . models import *









TokenAdmin.raw_id_fields = ['user']
