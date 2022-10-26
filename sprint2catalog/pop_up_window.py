import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib

class PopUpWindow(Gtk.Window):
    
    #Crea una ventana emergente que muestra una imagen, su título y descripción en la que has clicado
    def __init__(self, image, name, label2):
        box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 20)
        super().__init__(title = "")
        self.set_border_width(60)
        self.set_resizable(False)
        self.label = Gtk.Label(label = name)
        
        
        box.pack_start(image, False, False, 0)
        box.pack_start(self.label, False, False, 0)
        box.pack_start(label2, False, False, 0)
        self.add(box)
