"""
Just for specify some setting
"""

from django.apps import AppConfig


class CartConfig(AppConfig):
    """
    Specify some settings
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "cart"
