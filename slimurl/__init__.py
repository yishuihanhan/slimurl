# encoding: utf-8
from .url import URL

__all__ = ['URL']

author_info = (
    ("Dmitry Orlov", "me@mosquito.su"),
)

author_email = ", ".join(map(lambda x: x[1], author_info))

version_info = (0, 7, 8)

__version__ = ".".join(map(str, version_info))
__author__ = ", ".join(map(lambda x: "%s <%s>" % x, author_info))
