import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from cell import Cell

class MainWindow(Gtk.Window):
    flowbox = Gtk.FlowBox()
    
    def __init__(self):
        super().__init__ (title = "Fotos")
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(5)
        self.set_default_size(400, 400)
        
        header = Gtk.HeaderBar(title = "Harry Potter")
        header.set_subtitle("Mix")
        header.props.show_close_button = True
        self.set_titlebar(header)
        
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(self.flowbox)
        self.add(scrolled)
        
        cell_one = Cell("Harry Potter y la piedra filosofal", Gtk.Image.new_from_file("C:/msys64/home/Pablitoo/dise-o-de-interfaces/sprint1gtk/catalog/data/edited/ELEMENTO 1.jpg"))
        cell_two = Cell("Harry Potter y la cámara de los secretos", Gtk.Image.new_from_file("C:/msys64/home/Pablitoo/dise-o-de-interfaces/sprint1gtk/catalog/data/edited/ELEMENTO 2.jpg"))
        cell_three = Cell("Harry Potter y el prisionero de Azkaban", Gtk.Image.new_from_file("C:/msys64/home/Pablitoo/dise-o-de-interfaces/sprint1gtk/catalog/data/edited/ELEMENTO 3.jpg"))
        cell_four = Cell("Harry Potter y el cáliz de fuego", Gtk.Image.new_from_file("C:/msys64/home/Pablitoo/dise-o-de-interfaces/sprint1gtk/catalog/data/edited/ELEMENTO 4.jpg""))
        cell_five = Cell("Harry Potter y la Orden del Fénix", Gtk.Image.new_from_file("C:/msys64/home/Pablitoo/dise-o-de-interfaces/sprint1gtk/catalog/data/edited/ELEMENTO 5.jpg"))
        
        