from django.db import models

GENRE = (
    ('Horror', 'Horror'),
    ('Comedy', 'Comedy')
)


class Show(models.Model):
    title = models.CharField(max_length=100, verbose_name='Enter your film name')
    description = models.TextField(verbose_name='Enter disctiption on this film', blank=True)
    images = models.ImageField(upload_to='films/')
    cost = models.PositiveIntegerField(verbose_name='Enter your price')
    genres = models.CharField(max_length=100, verbose_name='Enter your genre', choices=GENRE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


