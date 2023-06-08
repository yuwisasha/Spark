from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

from PIL import Image

from .managers import UserManager


class Interest(models.Model):
    """
    Model for storing multiple profile interests
    """
    name = models.CharField(
        verbose_name=_('Interest'),
        max_length=50,
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Interest')
        verbose_name_plural = _('Interests')


class User(AbstractBaseUser, PermissionsMixin):
    """
    Model for user login credentials
    """
    email = models.EmailField(
        verbose_name=_('Email address'),
        max_length=50,
        unique=True,
    )
    is_active = models.BooleanField(
        verbose_name=_('Is active'),
        default=True,
    )
    is_admin = models.BooleanField(
        verbose_name=_('Is admin'),
        default=False,
    )
    created_at = models.DateTimeField(
        verbose_name=_('Created at'),
        auto_now_add=True,
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm: str, obj=None) -> bool:
        return True

    def has_module_perms(self, app_label: str) -> bool:
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        ordering = ['created_at', ]
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class Profile(models.Model):
    """
    Model to display user public credentials
    """
    class Gender(models.IntegerChoices):
        MALE = 0, _('Male')
        FEMALE = 1, _('Female')

        __empty__ = _('(Unknown)')

    class SexualIdentity(models.TextChoices):
        HETERO = 'H', _('Hetero')
        GAY = 'G', _('Gay')
        LESBIAN = 'L', _('Lesbian')
        BISEXUAL = 'B', _('Bisexual')
        ASEXUAL = 'A', _('Asexual')
        DEMISEXUAL = 'D', _('Demisexual')
        PANSEXUAL = 'P', _('Pansexual')
        QUEER = 'Q', _('Queer')
        UNDECIDED = 'U', _('Undecided')

    class LookingFor(models.IntegerChoices):
        MALE = 0, _('Men')
        FEMALE = 1, _('Women')
        BOTH = 2, _('Both')

    __empty__ = _('(Unknown)')
    user = models.OneToOneField(
        User,
        verbose_name=_('Profile'),
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=50,
    )
    date_of_birth = models.DateField(
        verbose_name=_('Date of birth'),
    )
    gender = models.IntegerField(
        verbose_name=_('Gender'),
        choices=Gender.choices,
    )
    looking_for = models.IntegerField(
        verbose_name=_('Looking for'),
        choices=LookingFor.choices,
    )
    sexual_identity = models.CharField(
        verbose_name=_('Sexual identity'),
        max_length=1,
        choices=SexualIdentity.choices,
    )
    bio = models.CharField(
        verbose_name=_('About'),
        max_length=200,
        blank=True,
    )
    interest = models.ManyToManyField(
        Interest,
        verbose_name=_('Interests'),
        blank=True,
    )


def user_directory_path(instance, filename):
    # photo will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "user_{0}/{1}".format(instance.profile.id, filename)


class ProfileImage(models.Model):
    """
    Model for storing multiple profile photos
    """
    user = models.ForeignKey(
        User,
        verbose_name=_('User'),
        on_delete=models.CASCADE,
    )
    profile = models.ForeignKey(
        Profile,
        verbose_name=_('Profile'),
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        verbose_name=_('Photo'),
        upload_to=user_directory_path,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super(ProfileImage, self).save()
        img = Image.open(self.image.path)
        if img.height > 800 and img.width > 500:
            img.thumbnail((800, 500))
        img.save(self.image.path, optimize=True)

    @mark_safe
    def image_preview(self):
        return '<img src="{tag}" height="175" width="150" />' \
            .format(tag=self.image.url,)

    class Meta:
        verbose_name = _('Photo')
        verbose_name_plural = _('Photos')
