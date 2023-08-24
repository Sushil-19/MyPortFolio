from django.contrib import admin
from .models import Services
from .models import Pricing
from .models import Blogs
from .models import MyInfo
from .models import Expertise
from .models import Education
from .models import Experiance
from .models import Skills
from .models import Language
from .models import Project

# Register your models here.

admin.site.register(Services)
admin.site.register(Pricing)
admin.site.register(Blogs)
admin.site.register(MyInfo)
admin.site.register(Expertise)
admin.site.register(Education)
admin.site.register(Experiance)
admin.site.register(Skills)
admin.site.register(Language)
admin.site.register(Project)
