from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Category"

    @staticmethod
    def get_all_categories():
        return Category.objects.all()


