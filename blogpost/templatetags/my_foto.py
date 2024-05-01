from django import template

register = template.Library()


@register.filter()
def media_filter(path):
    if path:
        return f"/media/{path}"
    return f"ФОТО НЕ НА��ДЕНО"
