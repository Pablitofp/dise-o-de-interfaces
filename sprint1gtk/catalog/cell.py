from unicodedata import name
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Cell(Gtk.EventBox):
    name = None
    
    def __init__(self):
        super().__init__ ()
        self.name = name
        box = Gtk.box(orientacion = Gtk.Orientation.VERTICAL, spacing = 4)
        box.pack_start(Gtk.Label(label = name), False, False, 0)
        box.pack_start(image, True, True, 0)
        self.add(box)
        self.connect("button-release-event", self.on_click)
        
    def on_click(self, widget, event):
        print("Has clicado en la celda ", self.name)