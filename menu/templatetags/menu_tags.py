
from django import template
from menu.models import Menu

register = template.Library()


@register.inclusion_tag("menu/menu.html", takes_context=True)
def render_menu(context, slug, template_name="menu/menu.html"):
    try:
        menu = Menu.objects.get(slug=slug)
    except Menu.DoesNotExist:
        menu = None
    root_items = menu.menu_items.filter(parent_item__isnull=True) if menu else []
    return {
        "menu": menu,
        "root_items": root_items,
        "request": context["request"],
        "template_name": template_name
    }

render_menu.function = lambda context, slug, template_name="menu/menu.html": render_menu(context, slug, template_name)
render_menu.template_name = lambda context, slug, template_name="menu/menu.html": template_name

