from django.db import models


class Session(models.Model):
    title = models.CharField(verbose_name='عنوان', max_length=50, unique=True)
    session_datetime = models.DateTimeField(verbose_name='تاریخ برگزاری')
    start_session_time = models.TimeField(verbose_name='ساعت شروع')
    end_session_time = models.TimeField(verbose_name='ساعت پایان')
    presentations_count = models.IntegerField(verbose_name='تعداد ارائه‌ها')
    address = models.CharField(verbose_name='نشانی محل برگزاری', max_length=255)
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True)

    def __str__(self):
        return self.title


class Presentation(models.Model):
    PRESENTATION_TYPE_CHOICES = (
        ('speech', 'Speech'),
        ('workshop', 'Workshop'),
        ('poster', 'Poster'),
        ('free_discussion', 'Free discussion')
    )
    user = models.ForeignKey('auth.User', verbose_name='کاربر', on_delete=models.CASCADE)
    session = models.ForeignKey('Session', verbose_name='جلسه', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='عنوان', max_length=50)
    description = models.CharField(verbose_name='توضیحات', max_length=500)
    presentation_type = models.CharField(verbose_name='نوع ارائه', max_length=30, choices=PRESENTATION_TYPE_CHOICES)
    equipment = models.CharField(verbose_name='تجهیزات مورد نیاز', max_length=500, null=True, blank=True)
    email = models.EmailField(verbose_name='ایمیل')
    phone_number = models.CharField(max_length=10, verbose_name='شمارهٔ تلفن همراه')
    article_attachment = models.FileField(verbose_name='فایل مقاله', upload_to='media/article', null=True, blank=True)
    slides_attachment = models.FileField(verbose_name='فایل اسلایدها', upload_to='media//slides/', null=True,
                                         blank=True)
    duration = models.IntegerField(verbose_name='مدت زمان مورد نیاز به دقیقه')
    start_time = models.TimeField(verbose_name='ساعت شروع', null=True, blank=True)
    end_time = models.TimeField(verbose_name='ساعت پایان', null=True, blank=True)
    is_verified = models.BooleanField(verbose_name="آیا تاییدشده است؟", default=False)

    def __str__(self):
        return self.title


class SessionComment(models.Model):
    user = models.ForeignKey('auth.User', verbose_name='کاربر', on_delete=models.CASCADE)
    session = models.ForeignKey('Session', verbose_name='جلسه', on_delete=models.CASCADE)
    text = models.CharField(verbose_name='متن نظر', max_length=500)
    creation_datetime = models.DateTimeField(verbose_name='تاریخ ثبت نظر')


class PresentationComment(models.Model):
    user = models.ForeignKey('auth.User', verbose_name='کاربر', on_delete=models.CASCADE)
    presentation = models.ForeignKey('Presentation', verbose_name='ارائه', on_delete=models.CASCADE)
    text = models.CharField(verbose_name='متن نظر', max_length=500)
    creation_datetime = models.DateTimeField(verbose_name='تاریخ ثبت نظر')
