from django.db import models
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.snippets.models import register_snippet
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey

# Menú como snippet para reutilizarlo en plantillas
@register_snippet
class Menu(ClusterableModel):
    title = models.CharField(
        max_length=255,
        help_text="Nombre interno del menú"
    )
    slug = models.SlugField(
        unique=True,
        help_text="Identificador para cargar el menú"
    )

    panels = [
        FieldPanel('title'),
        FieldPanel('slug'),
        InlinePanel('menu_items', label="Items del menú"),
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Menú"
        verbose_name_plural = "Menús"


# Ítems del menú
class MenuItem(Orderable):
    menu = ParentalKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='menu_items'
    )

    # 🔹 NUEVO CAMPO: permite definir un ítem como hijo de otro (para submenús)
    parent_item = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='children',
        help_text="Si este ítem es un submenú, selecciona su ítem padre."
    )
    title = models.CharField(
        max_length=255,
        help_text="Texto del enlace"
    )
    link_url = models.URLField(
        blank=True,
        null=True,
        help_text="Enlace externo"
    )
    link_page = models.ForeignKey(
        Page,
        blank=True,
        null=True,
        related_name='+',
        on_delete=models.CASCADE,
        help_text="Enlace a una página interna (sobrepone link_url)"
    )
    open_in_new_tab = models.BooleanField(default=False)

    panels = [
        # 🔹 NUEVO PANEL: para seleccionar el ítem padre en el admin
        FieldPanel('parent_item'),
        FieldPanel('title'),
        FieldPanel('link_url'),
        FieldPanel('link_page'),
        FieldPanel('open_in_new_tab'),
    ]

    def __str__(self):
        return self.title

    def get_url(self):
        if self.link_page:
            return self.link_page.url
        return self.link_url or '#'
