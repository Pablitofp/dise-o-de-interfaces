import gi
import requests, threading, shutil
from pop_up_window import PopUpWindow
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib
from window import MainWindow

class LoadWindow(Gtk.Window):
    label = Gtk.Label("Cargando elementos...")
    spinner = Gtk.Spinner()
    box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 20)
    
    #Creación pantalla de carga con un spinner y un label
    def __init__(self): 
        super().__init__(title = "")
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(60)
        self.set_resizable(False)
        self.spinner.props.active = True        
        self.box.pack_start(self.label, False, False, 0)
        self.box.pack_start(self.spinner, False, False, 0)
        self.add(self.box)

        self.launch_load()
        
        #Ubica inicialmente en el centro de la pantalla
        self.set_position(Gtk.WindowPosition.CENTER)
        
    #Cierre de la pantalla de carga y abriendo la MainWindow, una vez cargado los elementos del json
    def start_main_window(self, loaded_items_list):  
        win = MainWindow(loaded_items_list)
        win.show_all()
        self.disconnect_by_func(Gtk.main_quit)
        self.close()
        
    def launch_load(self):
        thread = threading.Thread(target = self.load_json, args=())
        thread.start()
        
    #Extrae del catalog.json el nombre, descripción y url de la imagen, y crea una imagen temporal con la que crea una gtk.image
    def load_json(self):  
        response = requests.get('https://raw.githubusercontent.com/Pablitofp/dise-o-de-interfaces/main/API/catalog.json')
        json_list = response.json()
        
        #Lista donde se almacenan los datos de las imágenes (utilizando el json creado)
        result = []  
        
        for json_item in json_list:
            name = json_item.get("name")
            description = json_item.get("description")
            image_url = json_item.get("image_url")
            r = requests.get(image_url, stream = True)
            with open("temp.png", 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            image = Gtk.Image.new_from_file("temp.png")
            result.append({"name" : name, "description" : description, "gtk_image" : image})
        
        GLib.idle_add(self.start_main_window, result)
    
            