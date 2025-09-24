from django.db import models

class Produto(models.Model):
    CATEGORIAS = [
        ('tecnologia', 'Tecnologia'),
        ('vestuario', 'Vestuário'),
    ]

    nome = models.CharField(max_length=100)
    descrição = models.TextField()
    preço = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)


    class Meta:
        ordering = ['nome']

    def __str__(self):
        return f'{self.nome} ({self.preço})'

    def get_absolute_url(self):
        return reverse('app:detalhe', args=[self.pk])
