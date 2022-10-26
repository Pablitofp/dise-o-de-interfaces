import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from cell import Cell
from acerca_de import AcercaDe

class MainWindow(Gtk.Window):
    flowbox = Gtk.FlowBox()
    
    def __init__(self, data_source):
        super().__init__ (title = "Fotos")
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(20)
        
        #Define el tamaño de la ventana
        self.set_default_size(1250, 300)
        
        header = Gtk.HeaderBar(title = "Harry Potter")
        header.set_subtitle("Mix")
        header.props.show_close_button = True
        
        self.set_titlebar(header)
        
        #Creamos un scroll para navegar por la ventana
        scrolled = Gtk.ScrolledWindow() 
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(self.flowbox)
        #self.add(scrolled)
        
        #Añades la información de cada elemento de la lista json en celdas
        for item in data_source: 
            cell = Cell(item.get("name"), item.get("gtk_image"), item.get("description"))
            self.flowbox.add(cell)
        
        #Ubica inicialmente en el centro de la pantalla    
        self.set_position(Gtk.WindowPosition.CENTER)
        
        
        
        #Creación de la barra superior de Menú y submenú
        menu = Gtk.MenuBar()
        
        filemenu = Gtk.Menu()
        filem = Gtk.MenuItem("Ayuda")
        filem.set_submenu(filemenu)
        
        acerca_de = Gtk.MenuItem("Acerca de")
        acerca_de.connect("button-release-event", self.on_click)
        filemenu.append(acerca_de)
        
        menu.append(filem)
        
        vbox = Gtk.VBox(False, 2)
        vbox.pack_start(menu, False, False, 0)
        vbox.pack_start(scrolled, True, True, 0)
        self.add(vbox)
    
    #Llamando a la clase AcercaDe para que se abra su ventana emergente cuando se haga click sobre "Acerca de"
    def on_click(self, widget, event):
        acerca = AcercaDe() 
        acerca.show_all()