from django.conf import settings
from django.template import Template
from cmsplugin_wrapper.models import WrapperPlugin

varname = getattr(settings, 'CMSPLUGIN_WRAPPER_VARNAME', 'CMSPLUGIN_WRAPPER_HOLDER')

def wrap_plugin(instance, placeholder, rendered_content, original_context):
    
    wrap_holder = original_context[varname]
    if isinstance(instance, WrapperPlugin):
        wrap_info = {
            'wrapper_plugin': instance,
            'context': original_context,
            'plugins': [],
            'plugin_counter': 0
        }
        wrap_holder['at_index'] = wrap_holder['at_index'] and wrap_holder['at_index'] + 1 or 0
        wrap_holder['index'].append(wrap_info)
        
    elif wrap_holder['at_index'] and not (instance._render_meta.text_enabled and instance.parent):
        wrap_info = wrap_holder['index'][wrap_holder.at_index]
        wrap_info['plugin_counter'] = wrap_info['plugin_counter'] + 1
        wrap_info['plugins'].append((instance, rendered_content))
         
        if wrap_info['plugin_counter'] == wrap_info['wrapper_plugin'].number or \
            wrap_info['plugin_counter'] == instance._render_meta.instance._render_meta.total:
             
            template = Template(wrap_info['wrapper_plugin'].template)
            context = wrap_info['context']
            context['plugins'] = wrap_info['plugins']
            wrap_holder['index'].pop()
            wrap_holder['at_index'] = wrap_holder['at_index'] == 0 and None or wrap_holder['at_index'] - 1
            
            return template.render(context)
    return u''