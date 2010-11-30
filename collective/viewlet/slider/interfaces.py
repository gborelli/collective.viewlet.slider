from zope import schema
from zope.interface import Interface

from plone.theme.interfaces import IDefaultPloneLayer


class ISliderLayer(IDefaultPloneLayer):
    """ Marker interface that defines a Zope 3 browser layer. """


class ISliderSettings(Interface):

    collection_path = schema.TextLine(
            title=u"Collection path",
            description=u"path to the collection used for slides",
            required=True,
            default=u'/Plone/banners')
