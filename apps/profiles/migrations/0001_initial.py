# Generated by Django 4.1.4 on 2022-12-22 02:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=11, region=None
                    ),
                ),
                ("about_me", models.TextField()),
                (
                    "license",
                    models.CharField(blank=True, max_length=30, null=True, unique=True),
                ),
                ("profile_photo", models.ImageField(upload_to="")),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("Male", "Male"),
                            ("Female", "Female"),
                            ("Other", "Other"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "country",
                    django_countries.fields.CountryField(
                        blank=True, max_length=2, null=True
                    ),
                ),
                ("city", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "is_buyer",
                    models.BooleanField(
                        blank=True,
                        default=False,
                        help_text="Are you a buyer",
                        null=True,
                    ),
                ),
                (
                    "is_seller",
                    models.BooleanField(
                        blank=True,
                        default=False,
                        help_text="Are you a seller",
                        null=True,
                    ),
                ),
                (
                    "is_agent",
                    models.BooleanField(
                        blank=True,
                        default=False,
                        help_text="Are you a agent",
                        null=True,
                    ),
                ),
                ("top_agent", models.BooleanField(default=False)),
                (
                    "rating",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=4, null=True
                    ),
                ),
                ("num_reviews", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "profile",
                "verbose_name_plural": "profiles",
            },
        ),
    ]
