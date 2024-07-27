from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid


class CustomUserManager(BaseUserManager):
    """Менеджер пользователя."""
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email address is required')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)
    

class User(AbstractUser):
    """Модель пользователя."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    GENDER_TYPES = (
        ("woman", 'женщина'),
        ("man", 'мужчина'),
    )
    bio = models.TextField('Описание', max_length=500, blank=True)
    date_joined = models.DateTimeField("Дата регистрации", default=timezone.now)
    birth_date = models.DateField('Дата рождения', null=True, blank=True)
    avatar = models.ImageField("Фото", upload_to='avatars', blank=True, null=True)
    gender = models.CharField("Пол", choices=GENDER_TYPES, max_length=10, blank=True)
    slug = models.SlugField(max_length=40, unique=True, blank=True)
    phone = models.CharField('Телефон', max_length=12, blank=True)
    email = models.EmailField('Email адрес', unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Генерация slug на основе username
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)  
        super().save(*args, **kwargs)
        

    @property
    def full_name(self):
        return '{} {}'.format(self.last_name, self.first_name)
        
    def __str__(self):
        return f'{self.username}: {self.first_name} - {self.email}'
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'




class FriendshipRequest(models.Model):
    """Модель запроса в друзья."""
    
    SENT = 'отправлено'
    ACCEPTED = 'принято'
    REJECTED = 'отклонено'
    EMPTY = ''


    STATUS_CHOICES = (
        (SENT, 'Отправлено'),
        (ACCEPTED, 'Принято'),
        (REJECTED, 'Отклонено'),
        (EMPTY, ''),

    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_for = models.ForeignKey(User, related_name='received_friendshiprequests', on_delete=models.CASCADE, verbose_name='Кто отправляет')
    created_at = models.DateTimeField("Дата", auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_friendshiprequests', on_delete=models.CASCADE, verbose_name='Кому отправляет')
    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES, default=EMPTY)

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'

    @property
    def full_name(self):
        return '{} {} {}'.format(self.created_for,  self.created_by, self.status,)

    def __str__(self):
        return f'{self.created_for} - {self.created_by} статус: {dict(self.STATUS_CHOICES)[self.status]}'
