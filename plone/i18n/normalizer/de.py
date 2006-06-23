# -*- coding: UTF-8 -*-

from plone.i18n.normalizer.interfaces import IURLNormalizer
from zope.interface import implements
from plone.i18n.normalizer.base import mapUnicode

# German character mapping
mapping = {
    196 : 'AE', 198 : 'AE', 214 : 'OE', 220 : 'UE', 223 : 'ss', 224 : 'a',
    228 : 'ae', 230 : 'ae', 246 : 'oe', 252 : 'ue'
}

class URLNormalizer(object):
    """
    This normalizer can normalize any unicode string and returns a URL-safe
    version that only contains of ASCII characters allowed in a URL.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IURLNormalizer, URLNormalizer)
      True
    """
    implements(IURLNormalizer)

    def normalize(self, text, locale=None):
        """
        Returns a normalized text. text has to be a unicode string.
        """
        return mapUnicode(text, mapping=mapping)

urlnormalizer = URLNormalizer()
