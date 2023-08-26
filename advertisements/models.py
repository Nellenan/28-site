from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Advertisement(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=80, verbose_name='заголовок')
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=12, decimal_places=2)
    auction = models.BooleanField('возможность торга', help_text='Отметьте, если торг уместен.obj = AD')
    created_at = models.DateTimeField('дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField('изображение', upload_to="images/")

    @admin.display(description="Дата создания")
    def create_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            create_time = self.created_at.time().strftime("%H:%M")
            return format_html("<span style='color: green'>Сегодня в {}</span>", create_time)
        return self.created_at.strftime("%d.%m.%Y - %H:%M")

    @admin.display
    def update_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            update_time = self.updated_at.time().strftime("%H:%M")
            return format_html("<span style='color: blue'>Сегодня в {}</span>", update_time)
        return self.updated_at.strftime("%d.%m.%Y - %H:%M")

    @admin.display
    def view_image(self):
        if self.image != "":
            return format_html("<img src={} width='50'>", self.image.url)
        return "Нет изображения!"

    def __str__(self):
        return f'id={self.id} title={self.title}, price={self.price}'

    class Meta:
        db_table = 'advertisement'
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'
