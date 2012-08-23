=================
cmsplugin-wrapper
=================

A plugin to wrap other plugins in django-cms

Installation
------------

For the current stable version:

::

    pip install cmsplugin-wrapper


For the development version:

::

    pip install -e git+git://github.com/fivethreeo/cmsplugin-wrapper.git#egg=cmsplugin-wrapper


Config:

::

        INSTALLED_APPS = [
            ...
            'cmsplugin_wrapper',
            ...
        ],
        
        CMS_PLUGIN_PROCESSORS = (
            ...
            'cmsplugin_wrapper.plugin_processors.wrap_plugin',
            ...
        )
        
        
        CONTEXT_PROCESSORS = (
            ...
            'cmsplugin_wrapper.context_processors.cmsplugin_wrapper',
            ...
        )