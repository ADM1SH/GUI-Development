import sys
import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

def print_hello(button):
    print("Hello World! You clicked the button.")

def activate(app):
    window = Gtk.ApplicationWindow(application=app)
    window.set_title("My First Python GUI")
    window.set_default_size(300, 200)

    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    box.set_halign(Gtk.Align.CENTER)
    box.set_valign(Gtk.Align.CENTER)

    window.set_child(box)

    button = Gtk.Button(label="Click Me")
    button.connect("clicked", print_hello)

    box.append(button)

    window.present()

if __name__ == "__main__":
    app = Gtk.Application(application_id="org.example.simplegui")
    app.connect("activate", activate)
    app.run(sys.argv)