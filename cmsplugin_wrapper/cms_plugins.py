from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_wrapper.models import WrapperPlugin

class CMSWrapperPlugin(CMSPluginBase):
    model = WrapperPlugin
    name = _("WrapperPlugin")
    admin_preview = False
    template = 'cms/dummy.html'
    
    def render(self, context, instance, placeholder):
        return context
            
plugin_pool.register_plugin(CMSWrapperPlugin)
