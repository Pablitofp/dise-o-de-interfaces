import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from cell import Cell

class MainWindow(Gtk.Window):
    flowbox = Gtk.FlowBox()
    
    def __init__(self, data_source):
        super().__init__ (title = "Fotos")
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(5)
        self.set_default_size(400, 400)
        
        header = Gtk.HeaderBar(title = "Harry Potter")
        header.set_subtitle("Mix")
        header.props.show_close_button = True
        
        self.set_titlebar(header)
        
        #Creamos un scroll para navegar por la ventana
        scrolled = Gtk.ScrolledWindow() 
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(self.flowbox)
        self.add(scrolled)
        
        #Añades la información de cada elemento de la lista json en celdas
        for item in data_source: 
            cell = Cell(item.get("name"), item.get("gtk_image"), item.get("description"))
            self.flowbox.add(cell)