import webview
import tkinter
from tkinter import *

#Eaglercraft Application Client by BtPlayzX [Member of EaglrDevs]
root = tkinter.Tk()
Label(root, text='Eaglercraft Launcher in beta! BtPlayzX is working on it.. :>').pack()

def start_client():
    webview.client.start()

root = tkinter.Tk()
root.title('Eaglercraft Launcher')
root.geometry( "600x600" )
chosen_client = 'Choose Eaglercraft Client'

options = [
    "Choose Eaglercraft Client",
    "Eaglercraft 1.3",
    "Eaglercraft 1.5.2",
    "Eaglercraft 1.5.2 (Resent Client)",
    "Eaglercraft 1.5.2 (Precision Client)",
    "Eaglercraft 1.8.8",
    'Eaglercraft 1.8.8 (Fuchsiax Client)',
    'Eaglercraft 1.14'
]


clients = {
    'Eaglercraft 1.3': 'https://mopnop.github.io/eaglercraft-singleplayer/',
    'Eaglercraft 1.5.2': 'https://html5gfiles.github.io/minecraft-15/',
    'Eaglercraft 1.5.2 (Resent Client)': 'https://resent.vercel.app',
    'Eaglercraft 1.5.2 (Precision Client)': 'https://html5gfiles.github.io/precision-client',
    'Eaglercraft 1.8.8': 'https://eaglercraft.q13x.com',
    'Eaglercraft 1.8.8 (Fuchsiax Client)': 'https://elidoesexploits.github.io/eaglercraft/FuschiaX/',
    'Eaglercraft 1.14': 'https://eaglerdevs.github.io/EaglerCraft/'
    
}
  
# datatype of menu text
clicked = StringVar()
  
# initial menu text
clicked.set("Choose EaglerCraft Client")
  
# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.pack()

def launch():
    chosen_client = clicked.get()
    root.destroy()
    url = clients[chosen_client]
    webview.create_window(chosen_client, url)
    webview.start()

            

    

button = Button( root , text = "Launch Eaglercraft Client", command=launch).pack()
  




root.mainloop()
