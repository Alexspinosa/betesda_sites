from django.db import models

# Create your models here.
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.TextBlock()
    image = ImageChooserBlock(required=False)
    link = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(default="Ver más")
    background_color = blocks.CharBlock(default="#ffffff")
    button_color = blocks.CharBlock(default="#1D9DE2")

    class Meta:
        template = "blocks/card_block.html"
        icon = "placeholder"
        label = "Card Block"
