import pygtk
import requests

pygtk.require('2.0')
import gtk
import gtk.glade

class LoginWindow:

    def __init__(self):
        self.glade = gtk.Builder()
        self.glade.add_from_file("formlogin.glade")
        self.glade.connect_signals(self)
        self.main_dialog = self.glade.get_object("main_dialog")
        self.main_dialog.set_default(self.glade.get_object("btn_login"))
        self.main_dialog.connect("destroy", gtk.main_quit)
        self.main_dialog.show_all()

    def btn_login_pressed(self, evt):
        txtusername = self.glade.get_object('txtusername').get_text()
        txtpassword = self.glade.get_object('txtpassword').get_text()
        print (txtusername, txtpassword)

        login_succeeded = False
        url = 'http://127.0.0.1:5000/login/{}/{}'.format(txtusername, txtpassword)
        r = requests.get(url)
        d = r.json()
        print ('hdgfhgjh', d)
        login_succeeded = d['succceded']
        parent = self.main_dialog
        if login_succeeded:
            md = gtk.MessageDialog(parent, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_INFO, gtk.BUTTONS_CLOSE, "Login succeed")
            response = md.run()
            if response == gtk.RESPONSE_CLOSE:
                md.destroy()
        else:
            md = gtk.MessageDialog(parent, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, gtk.BUTTONS_CLOSE, "Login failed")
            response = md.run()
            if response == gtk.RESPONSE_CLOSE:
                md.destroy()
if __name__ == "__main__":
    try:
        a = LoginWindow()
        gtk.main()
    except KeyboardInterrupt:
        pass