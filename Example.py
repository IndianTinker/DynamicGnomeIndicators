from gi.repository import Gtk, GLib
from gi.repository import AppIndicator3 as appindicator
import os

count=0

def cb_exit(w, data):
   Gtk.main_quit()


ind_app = appindicator.Indicator.new_with_path (
  "count-indicator",
   "temp-icon",
   appindicator.IndicatorCategory.APPLICATION_STATUS,
    os.path.dirname(os.path.realpath(__file__)))
ind_app.set_status (appindicator.IndicatorStatus.ACTIVE)

def getcount():
    global count
    count=count+1
    return str(count)


def dummy(*args):
    #print(getcount())
    menu_items.set_label(getcount())

menu = Gtk.Menu()
menu_items = Gtk.MenuItem()
menu_items.set_label(getcount())
menu.append(menu_items)
menu_items.connect("activate",dummy)
menu_items.show()
item = Gtk.MenuItem()
item.set_label("Exit")
menu.append(item)
item.connect("activate", cb_exit, '')
item.show()
ind_app.set_menu(menu)


Gtk.main()
