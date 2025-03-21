from django.db import models

class Storia(models.Model):
    titolo = models.CharField(max_length=200)
    contenuto = models.TextField()
    data_creazione = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titolo
