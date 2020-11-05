from django.conf import settings
from django.db import models

CATEGORY_CHOICES = (

    ('BG','BAGS' ),
    ('LRS',  'SHOES'),
    ('JCT', 'JACKET'),
    ('MS', 'MEN SHIRT'),
     ('MSOO', 'MEN SHOES'),
     ('MT', 'MEN TROUSERS'),
     ('WS', 'WOMEN SHIRT'),
     ('WSK', 'WOMEN SKIRT'),
     ('WSH', 'WOMEN SHOES'),
     ('WG', 'WOMEN GOWNS'),

     )

LABEL_CHOICES = (
    ('P','primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)


class item(models.Model):
   title = models.CharField(max_length=150)
   price = models.FloatField(default= 50)
   category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
   label_choices = models.CharField(choices=LABEL_CHOICES, max_length=5)

   def _str_(self):
       return self.title


class orderitem(models.Model):
    item = models.ForeignKey(item, on_delete=models.CASCADE)

    def _str_(self) :
        return self.title

class order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(orderitem )
    items_date = models.DateTimeField(auto_now_add= True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def _str_(self):
        return self.user.username




