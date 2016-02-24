from distutils.core import setup
import py2exe

setup(
    description = "Frontend GTK",
    windows=[
        {
            'script':'main.py',
            # "icon_resources": [(1, "images/Icon.ico")],
            "dest_base" : "FrontendGTK",
            "app_base": "FrontendGTK"
        }],
    cmdline_style='pywin32',
    data_files=[
                   'formlogin.glade',
                   # If using GTK+'s built in SVG support, uncomment these
                   #os.path.join(gtk_base_path, '..', 'runtime', 'bin', 'gdk-pixbuf-query-loaders.exe'),
                   #os.path.join(gtk_base_path, '..', 'runtime', 'bin', 'libxml2-2.dll'),
               ],
    options= {
        'py2exe':{
            'dist_dir': "FrontendGTK",
            'packages':'encodings',
                  # Optionally omit gio, gtk.keysyms, and/or rsvg if you're not using them
                  'includes': 'cairo, pango, pangocairo, atk, gobject, gio, gtk.keysyms'

        }
    }
)