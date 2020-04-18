from django.db import models

# Create your models here.


class Todo(models.Model):
    thing = models.CharField(max_length=50)  #此处的thing表示待办事项
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.thing   #返回Todo类（表）的thing