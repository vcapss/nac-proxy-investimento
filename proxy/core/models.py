import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.username


class Pacote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    desc = models.CharField(max_length=500, null=False)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    estoque = models.IntegerField()

    def __str__(self):
        return self.desc

    """def save(self, *args, **kwargs):

        self.save(*args, **kwargs)"""


class Adquirente(models.Model):
    user = models.ForeignKey(User)
    pacote = models.OneToOneField(Pacote)
    qtd = models.IntegerField(null=False)
    total = models.DecimalField(max_digits=12, decimal_places=2, editable=False)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if self.qtd > self.pacote.estoque:
            raise Exception("{} não pode efetuar a compra do pacote, por exceder o estoque".format(self.user.username))

        self.pacote.estoque = self.pacote.estoque - self.qtd
        self.pacote.save()

        self.total = self.pacote.valor * self.qtd

        super().save(*args, **kwargs)
