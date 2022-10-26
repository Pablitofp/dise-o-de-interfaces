import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from load_window import LoadWindow

win = LoadWindow() #Llamas a la clase LoadWindow para ejecutarla
win.show_all()

Gtk.main()