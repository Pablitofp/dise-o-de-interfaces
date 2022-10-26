import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib

class AcercaDe(Gtk.Window):
    
    #Escribir dentro de la ventana emergente de "Acerca de"
    def __init__(self):
        box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 20)
        super().__init__(title = "")
        self.set_default_size(200, 200)
        label = Gtk.Label(label = "Me llamo Pablo")
        self.add(box)
        box.pack_start(label, True, True, 0)
        self.set_position(Gtk.WindowPosition.CENTER)
