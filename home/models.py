
from django.db import models
from wagtail import blocks
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel
from card.models import CardBlock
from wagtail.fields import StreamField

# Bloque Slide para Slider
class SlideBlock(blocks.StructBlock):
    imagen = ImageChooserBlock(required=True)
    titulo = blocks.CharBlock(required=False)
    subtitulo = blocks.TextBlock(required=False)
    boton_texto = blocks.CharBlock(required=False)
    boton_url = blocks.URLBlock(required=False)

    class Meta:
        icon = "image"
        label = "Slide"

# Bloque Slider
class SliderBlock(blocks.StructBlock):
    slides = blocks.ListBlock(SlideBlock())

    class Meta:
        template = "blocks/slider.html"
        icon = "image"
        label = "Slider"

# Bloque de contenido estándar
class RichTextBlock(blocks.StreamBlock):
    heading = blocks.CharBlock(form_classname="full title")
    paragraph = blocks.RichTextBlock()
    image = ImageChooserBlock()

# Bloque Hero
class HeroBlock(blocks.StructBlock):
    titulo = blocks.CharBlock(required=True, help_text="Título principal")
    subtitulo = blocks.TextBlock(required=False, help_text="Texto debajo del título")
    boton_texto = blocks.CharBlock(required=False, help_text="Texto del botón")
    boton_url = blocks.URLBlock(required=False, help_text="Enlace del botón")

    class Meta:
        template = "blocks/hero.html"
        icon = "placeholder"
        label = "Sección Hero"

# Bloque Tarjeta para HomePage
class TarjetaBlock(blocks.StructBlock):
    titulo = blocks.CharBlock()
    descripcion = blocks.TextBlock()
    image = ImageChooserBlock(required=False)
    link = blocks.URLBlock(required=False)

    class Meta:
        icon = "list-ul"
        label = "Tarjeta"

# Bloque Evento para HomePage
class EventoBlock(blocks.StructBlock):
    titulo = blocks.CharBlock()
    descripcion = blocks.TextBlock()
    fecha = blocks.DateBlock()
    image = ImageChooserBlock(required=False)
    link = blocks.URLBlock(required=False)

    class Meta:
        icon = "date"
        label = "Evento"

# Página de inicio con bloques extendidos
class HomePage(Page):
    body = StreamField(
        [
            ("hero", HeroBlock()),
            ("slider", SliderBlock()),
            ("card", blocks.ListBlock(CardBlock())),
            ("eventos", blocks.ListBlock(EventoBlock())),
        ],
        blank=True,
        use_json_field=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

# Página estándar
class StandardPage(Page):
    body = StreamField(RichTextBlock(), blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

# Página de eventos independiente
class EventPage(Page):
    date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)
    body = StreamField(RichTextBlock(), blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('location'),
        FieldPanel('body'),
    ]
# Agregar imagen destacada
class FeaturedImage(models.Model):
       page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='featured_images')
       image = models.ImageField(upload_to='featured_images/')
       alt_text = models.CharField(max_length=255, blank=True)

class Meta:
       verbose_name = "Imagen destacada"
       verbose_name_plural = "Imágenes destacadas"
