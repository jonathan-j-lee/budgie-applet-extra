#!/usr/bin/env python3

"""
caffeine -- A Budgie applet to toggle screen dimming temporarily.
"""

import gi.repository
gi.require_version('Budgie', '1.0')
gi.require_version('Wnck', '3.0')
from gi.repository import Budgie, GObject, Gtk, Gio


class CaffeinePlugin(GObject.GObject, Budgie.Plugin):
    """ A wrapper for the Caffeine plugin. """
    __gtype_name__ = 'Caffeine'

    def __init__(self):
        super().__init__()

    def do_get_panel_widget(self, uuid):
        """ Initialize and return a new caffeine applet. """
        return CaffeineApplet(uuid)


class CaffeineApplet(Budgie.Applet):
    """ An applet with one toggle button to manipulate power settings. """
    POWER_SCHEMA_NAME = 'org.gnome.settings-daemon.plugins.power'
    DESKTOP_SCHEMA_NAME = 'org.gnome.desktop.session'

    def __init__(self, uuid):
        super().__init__()
        self.uuid = uuid

        self.button = Gtk.ToggleButton.new()
        self.button.set_relief(Gtk.ReliefStyle.NONE)
        self.button.set_active(False)
        self.add(self.button)

        self.image = Gtk.Image.new_from_icon_name('gnome-power-manager-symbolic',
                                                  Gtk.IconSize.BUTTON)
        self.button.add(self.image)
        self.button.set_tooltip_text('Disable screen dimming')
        self.show_all()

        self.power_settings = Gio.Settings(self.POWER_SCHEMA_NAME)
        self.desktop_settings = Gio.Settings(self.DESKTOP_SCHEMA_NAME)
        self.defaults = dict()  # Saved settings

        self.button.connect_after('clicked', self.on_click)

    def disable_dim(self):
        """ Save default settings, and disable screen dim. """
        self.defaults = {
            'idle-dim': self.power_settings.get_boolean('idle-dim'),
            'sleep-inactive-ac-type':
                self.power_settings.get_string('sleep-inactive-ac-type'),
            'sleep-inactive-battery-type':
                self.power_settings.get_string('sleep-inactive-battery-type'),
            'idle-delay': self.desktop_settings.get_uint('idle-delay')
        }

        self.power_settings.set_boolean('idle-dim', False)
        self.power_settings.set_string('sleep-inactive-ac-type', 'nothing')
        self.power_settings.set_string('sleep-inactive-battery-type', 'nothing')
        self.desktop_settings.set_uint('idle-delay', 0)  # Never dim
        self.button.set_tooltip_text('Enable screen dimming')

    def enable_dim(self):
        """ Restore default settings enabling screen dim. """
        self.power_settings.set_boolean('idle-dim', self.defaults.get('idle-dim', True))
        self.power_settings.set_string('sleep-inactive-ac-type',
                                       self.defaults.get('sleep-inactive-ac-type', 'suspend'))
        self.power_settings.set_string('sleep-inactive-battery-type',
                                       self.defaults.get('sleep-inactive-battery-type', 'suspend'))
        self.desktop_settings.set_uint('idle-delay',
                                       self.defaults.get('idle-delay', 60))
        self.button.set_tooltip_text('Disable screen dimming')

    def on_click(self, button):
        """ Delegate action based on current button state. """
        if button.get_active():
            self.disable_dim()
        else:
            self.enable_dim()
