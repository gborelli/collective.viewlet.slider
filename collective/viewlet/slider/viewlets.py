from plone.app.layout.viewlets import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.CMFPlone.utils import getToolByName

from plone.registry.interfaces import IRegistry
from zope.component import getUtility

class SliderViewlet(ViewletBase):
    index = ViewPageTemplateFile('slider.pt')

    @property
    def collection_path(self):
        settings = getUtility(IRegistry)
        return settings.records['collective.viewlet.slider.interfaces.ISliderSettings.collection_path'].value

    def images(self):
        catalog = getToolByName(self.context, 'portal_catalog')
        brains = catalog.searchResults({'path':self.collection_path})
        if brains:
            results = brains[0].getObject().queryCatalog()
            for item in results:
                yield dict(title = item.Title,
                           url = item.getURL())
