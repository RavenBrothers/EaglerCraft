import tkinter
from tkinter import *
import webview


root = tkinter.Tk()
root.title('EaglerCraft Launcher')
root.geometry( "600x600" )
chosen_client = 'Choose EaglerCraft Client'

options = [
    "Choose EaglerCraft Client",
    "EaglerCraft 1.3",
    "EaglerCraft 1.5.2",
    "EaglerCraft 1.5.2 (Tame Client)",
    "EaglerCraft 1.5.2 (Resent Client)",
    "EaglerCraft 1.5.2 (Precision Client)",
    "EaglerCraft 1.8.8",
    'EaglerCraft 1.8.8 (Fuchsiax Client)',
    'EaglerCraft 1.14'
]


clients = {
    'EaglerCraft 1.3': 'https://mopnop.github.io/eaglercraft-singleplayer/',
    'EaglerCraft 1.5.2': 'https://html5gfiles.github.io/minecraft-15/',
    'EaglerCraft 1.5.2 (Tame Client)': 'https://mc.tame.gg',
    'EaglerCraft 1.5.2 (Resent Client)': 'https://resent.vercel.app',
    'EaglerCraft 1.5.2 (Precision Client)': 'https://html5gfiles.github.io/precision-client',
    'EaglerCraft 1.8.8': 'https://eaglercraft.q13x.com',
    'EaglerCraft 1.8.8 (Fuchsiax Client)': 'https://elidoesexploits.github.io/eaglercraft/FuschiaX/',
    'EaglerCraft 1.14': 'https://eaglerdevs.github.io/EaglerCraft/'
    
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

            

    

button = Button( root , text = "Launch EaglerCraft Client", command=launch).pack()
  




root.mainloop()
