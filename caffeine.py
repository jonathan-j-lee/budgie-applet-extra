#!/usr/bin/env python3

"""
caffeine -- A Budgie applet to toggle screen dimming temporarily.
"""

import gi.repository
gi.require_version('Budgie', '1.0')
gi.require_version('Wnck', '3.0')
from gi.repository import Budgie, GObject, Wnck, Gtk


class CaffeinePlugin(GObject.GObject, Budgie.Plugin):
    __gtype_name__ = 'Caffeine'

    def __init__(self):
        super().__init__()

    def do_get_panel_widget(self, uuid):
        return CaffeineApplet(uuid)


class CaffeineApplet(Budgie.Applet):
    def __init__(self, uuid):
        super().__init__()
