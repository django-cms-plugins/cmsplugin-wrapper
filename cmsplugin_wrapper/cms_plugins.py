from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_wrapper.models import WrapperPlugin

class CMSWrapperPlugin(CMSPluginBase):
    model = WrapperPlugin
    name = _("WrapperPlugin")
    render_plugin=False
    admin_preview = False

plugin_pool.register_plugin(CMSWrapperPlugin)
