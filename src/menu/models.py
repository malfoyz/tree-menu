from django.db import connection, models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Menu(models.Model):
    """Модель меню."""

    name = models.CharField(
        _('Название'),
        max_length=100,
    )

    @classmethod
    def get_ancestors_recursive(cls, menu_name):
        with connection.cursor() as cursor:
            cursor.execute('''
                WITH RECURSIVE t_menu AS (
                    SELECT menu_menuitem.id, title, parent_id, slug
                    FROM menu_menuitem
                    JOIN menu_menu ON menu_menuitem.menu_id = menu_menu.id
                    WHERE menu_menu.name = %s
                    UNION
                    SELECT m.id, m.title, m.parent_id, m.slug
                    FROM menu_menuitem m
                    JOIN t_menu ON m.parent_id = t_menu.id
                )
                SELECT * FROM t_menu
                ORDER BY title
                ;
            ''', [menu_name])

            result = cursor.fetchall()

            if not result:
                return []

            menu_dict = {}

            for row in result:
                item_id, title, parent_id, slug = row
                children = menu_dict.setdefault(item_id, [])
                menu_dict[parent_id] = menu_dict.get(parent_id, [])
                menu_dict[parent_id].append((item_id, title, slug, children))

            # Фильтрация корневых элементов
            root_items = [item for item in menu_dict[None] if item[0] in menu_dict]

            return root_items

    class Meta:
        verbose_name = _('Меню')
        verbose_name_plural = _('Меню')

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """Модель пункта меню."""

    title = models.CharField(
        _('Название'),
        max_length=100,
    )
    slug = models.SlugField(
        _('URL'),
        max_length=100,
        unique=True,
        db_index=True,
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name=_('Меню'),
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='subitems',
        blank=True,
        null=True,
        verbose_name=_('Родитель'),
        limit_choices_to={'menu': models.OuterRef('menu')},
    )

    class Meta:
        verbose_name = _('Пункт меню')
        verbose_name_plural = _('Пункты меню')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('item', kwargs={'item_slug': self.slug})
