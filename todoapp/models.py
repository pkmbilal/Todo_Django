from django.db import models

# Create your models here.
class Todo(models.Model):
    todoName = models.CharField(max_length=100, blank=False, null=False)
    isCompleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    lastUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.todoName
    
    class Meta:
        verbose_name_plural = "Todo's"