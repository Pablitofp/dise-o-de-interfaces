import gi
from pop_up_window import PopUpWindow
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Cell(Gtk.EventBox):
    name = None
    
    #Creas las celdas donde van a ir las imágenes
    def __init__(self, name, image, description): 
        super().__init__ ()
        self.name = name
        self.image = image
        self.description = description
        box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 4)
        box.pack_start(Gtk.Label(label = name), False, False, 0)
        box.pack_start(image, True, True, 0)
        self.add(box)
        self.connect("button-release-event", self.on_click)
        
    #Conviertes las imágenes y llamas al metodo que, al clicar en una foto, la abre en una ventana emergente
    def on_click(self, widget, event): 
        image = Gtk.Image()
        image.set_from_pixbuf(self.image.get_pixbuf())
        label = Gtk.Label(label = self.description)
        pop = PopUpWindow(image, self.name, label)
        pop.show_all()
        
    