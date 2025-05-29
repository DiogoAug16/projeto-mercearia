from django.contrib import admin

from produtos.models import Produto

# Register your models here.
class ProdutoAdmin (admin.ModelAdmin):
    list_display=('produto_nome', 'preco','imposto','slug','estoque','esta_disponivel')
    prepopulated_fields={
        'slug':('produto_nome',)
    }

admin.site.register(Produto, ProdutoAdmin)