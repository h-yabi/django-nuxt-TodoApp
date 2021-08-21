from django.db import models

# Create your models here.
class TodoModel(models.Model):
  PRIORITY = (
      ("Low", "Low"),
      ("Middle", "Middle"),
      ("High", "High"),
  )
  title = models.CharField(max_length=20)
  description = models.CharField(max_length=100)
  pictur = models.FileField()
  priority = models.CharField(choices=PRIORITY, max_length=10)

  def __str__(self):
    return self.title