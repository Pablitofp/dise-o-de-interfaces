from cProfile import label
import gi
import yes_window
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from yes_window import YesWindow
from no_window import NoWindow

class MainWindow(Gtk.Window):
    
    def yes_clicked(self, widget):
        yeswin = YesWindow()
        yeswin.show_all()
        
    def no_clicked(self, widget):
        yowin = NoWindow()
        yowin.show_all()
    
    def __init__(self):
        box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
        box2 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)
        label = Gtk.Label("Ejemplo")
        super().__init__(title = "Main")
        box.pack_start(label, True, True, 0)
        box.pack_start(box2, True, True, 0)
        
        button_yes = Gtk.Button(label = "Si")
        button_no = Gtk.Button(label = "No")
        box2.pack_start(button_yes, True, True, 0)
        box2.pack_start(button_no, True, True, 0)
        self.connect("destroy", Gtk.main_quit)
        
        button_yes.connect("clicked", self.yes_clicked)
        button_no.connect("clicked", self.no_clicked)
        self.add(box)