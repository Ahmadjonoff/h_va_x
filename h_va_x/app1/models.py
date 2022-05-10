from django.db import models

class togri(models.Model):
    t_soz = models.CharField(max_length = 20)

    def __str__(self):
        return self.t_soz


class notogri(models.Model):
    n_soz = models.CharField(max_length=20)
    togrisi = models.ForeignKey(togri, on_delete = models.CASCADE)

    def __str__(self):
        return self.n_soz