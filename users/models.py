from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователь"""

    username = None
    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Введите email (уникальный)"
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        null=True,
        blank=True,
        help_text="Введите номер телефона",
    )
    country = models.CharField(
        max_length=35,
        verbose_name="Страна",
        blank=True,
        null=True,
        help_text="Укажите страну",
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="Аватар",
        null=True,
        blank=True,
        help_text="Загрузите свой аватар",
    )

    # Поля для аутентификации
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    # Явно указываем related_name для избежания конфликтов
    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name="groups",
        blank=True,
        help_text="The groups this user belongs to.",
        related_name="custom_user_set",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name="user permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="custom_user_permissions_set",
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        # Добавляем db_table, чтобы избежать конфликтов имён
        db_table = "custom_user"
        permissions = [
            ("can_block_users", "Can block users"),
        ]

    def __str__(self):
        return self.email
