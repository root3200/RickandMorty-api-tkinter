from tkinter import*
import tkinter as tk
from PIL import ImageTk, Image
import requests
from io import BytesIO


base_url = "https://rickandmortyapi.com/api/"
character_url = base_url + "character/"

def get_character(char_id):
    response = requests.get(character_url + str(char_id))
    if response.status_code == 200:
        char = response.json()
        return char
    else:
        return None

def show_character(char_id):
    char = get_character(char_id)
    if char:
        window = tk.Tk()
        window.configure(bg="green")
        window.title(char['name'])
        
        # Cargar la imagen del personaje
        response = requests.get(char['image'])
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        img = img.resize((300, 300), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img)
        
        # Crear la etiqueta de imagen y agregarla a la ventana
        img_label = tk.Label(window, image=img_tk)
        img_label.pack()
        
        # Crear la etiqueta de texto y agregarla a la ventana
        text_label = tk.Label(window, text=char['name'])
        text_label.pack()
        
        window.mainloop()
    else:
        print("Personaje no encontrado")
        
def show_character(char_id):
    char = get_character(char_id)
    if char:
        window = tk.Tk()
        window.title(char['name'])
        
        # Cargar la imagen del personaje
        response = requests.get(char['image'])
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        img = img.resize((300, 300), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img)
        
        # Crear la etiqueta de imagen y agregarla a la ventana
        img_label = tk.Label(window, image=img_tk)
        img_label.pack()
        
        # Crear la etiqueta de texto y agregarla a la ventana
        text_label = tk.Label(window, text=char['name'])
        text_label.pack()
        
        # Crear la etiqueta de texto con la información del personaje y agregarla a la ventana
        data_char = {
            f"ID": char['id'],
            f"Nombre": char['name'],
            f"Estado": char['status'],
            f"Especie": char['species'],
            f"Sexo": char['gender'],
            f"Origen": char['origin']['name'],
            f"Ubicacion": char['location']['name'],
            f"Episodios donde aparece": len(char['episode']),
            f"Creado": char['created'],
            f"Especie": char['species']
        }
        char_info = "\n".join([f"{key}: {value}" for key, value in data_char.items()])
        char_info_label = tk.Label(window, text=char_info, font='bold, 12')
        char_info_label.pack()
        
        window.mainloop()
    else:
        print(colored("[!] Personaje no encontrado", "red"))


import pyfiglet
from termcolor import colored

title = colored(pyfiglet.figlet_format("Rick and Morty", font="doom"),"light_green")
print(title, colored("\t\t\t\t\t==== root3200 ====", "light_yellow"))
print(colored("Rick and morty API - Tkinter", "light_magenta"), colored("\n[!] - Existen 826 personajes \n[!] - Episodios 51 \n[!] - Ubicaciones 126", "blue"))
show_character(int(input("Ingresa un numero y obten informacion del personaje => ")))
