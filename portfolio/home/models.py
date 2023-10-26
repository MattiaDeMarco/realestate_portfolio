from django.db import models

# Create your models here.

class Property(models.Model):

    title = models.CharField(max_length=99, verbose_name='Titolo')
    city = models.CharField(max_length=99, verbose_name='Città')
    description = models.TextField(verbose_name='Descrizione')
    thumbnail = models.ImageField(verbose_name='Immagine di copertina')
    virtual_tour = models.CharField(max_length=99,
                                    verbose_name='Link Virtual Tour',
                                    help_text='Inserire il link Matterport')

    class Meta:
        verbose_name = ("Immobile")
        verbose_name_plural = ("Immobili")

    def __str__(self):
        return self.title


class Photo(models.Model):

    city = models.ForeignKey(Property, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(blank=False, null=False)
    description = models.TextField(default='Galleria Immagini')

    class Meta:
        verbose_name = ("Foto")
        verbose_name_plural = ("Foto")

    def __str__(self):
        return str(self.description) + ' di ' + str(self.city)
