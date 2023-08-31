import tkinter as tk
import os

my_w = tk.Tk()
my_w.geometry("200x240")  # Size of the window 
my_w.title("openVPyN")  # Adding a title
my_w.config(background='green')
my_w.configure(background='green')

my_w.columnconfigure(0, weight=1)
my_w.columnconfigure(1, weight=3)

my_str = tk.StringVar()
l1 = tk.Label(my_w,  textvariable=my_str, borderwidth=1, relief="groove", background='white')
l1.grid(row=0,column=0,sticky=tk.W, padx=8, pady=2)


def press_button(my_language):
    my_str.set("aktiv: "+my_language)
    my_w.title(my_language + " openVPyN aktiv")
    os.system('"c:\\Program Files\\OpenVPN\\bin\\openvpn-gui.exe" --command disconnect_all')
    os.system('"c:\\Program Files\\OpenVPN\\bin\\openvpn-gui.exe" --connect '+my_language)

my_str.set("aktives VPN: - ")
list_languages = os.listdir("C:\\Users\\dhia.bensalem\\OpenVPN\\config\\") # returns list
var = 1

for language in list_languages:
    btn = tk.Button(my_w, text=language, anchor="w", command=lambda lan=language:press_button(lan), background='yellow', height=2, width=20, font='Helvetica')
    btn.grid(row=var,column=0,sticky=tk.W, padx=8, pady=2)
    var += 1
 
my_w.mainloop()  # keep up the good work =)
