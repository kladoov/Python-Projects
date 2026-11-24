import tkinter as tk 
from tkinter import filedialog
import tkinter as tk
from tkinter import messagebox
import os
import shutil

def seleccionar_ruta():
    ruta = filedialog.askdirectory()  # askdirectory saca la carpeta seleccionada
    if ruta:
        entrada.delete(0, tk.END) 
        entrada.insert(0, ruta)

def organizar_directorio():
    ruta = entrada.get() # obtengo la ruta seleccionada
    if ruta:
        folder_images = os.path.join(ruta, "Imagenes")
        folder_exe = os.path.join(ruta, "Ejecutables")
        folder_docs = os.path.join(ruta, "Documentos")
        folder_video = os.path.join(ruta, "Videos")

        if not os.path.exists(folder_images):
            os.makedirs(folder_images)
        if not os.path.exists(folder_exe):
            os.makedirs(folder_exe)
        if not os.path.exists(folder_docs):
            os.makedirs(folder_docs)
        if not os.path.exists(folder_video):
            os.makedirs(folder_video)

        # mueve los archivos a las carpetas correspondientes
        mover_imagenes(ruta, folder_images)
        mover_exe(ruta, folder_exe)
        mover_docs(ruta, folder_docs)
        mover_video(ruta, folder_video)

        messagebox.showinfo("Mensaje", f"Directorio {ruta} organizado.")

def mover_imagenes(ruta, imagenes_carpeta):
    # buscar los archivos 
    for archivo in os.listdir(ruta):
        if archivo.lower().endswith(".jpg") | archivo.lower().endswith(".jpeg") | archivo.lower().endswith(".png") | archivo.lower().endswith(".webp"):
            archivo_origen = os.path.join(ruta, archivo)
            archivo_destino = os.path.join(imagenes_carpeta, archivo)
            shutil.move(archivo_origen, archivo_destino)
        
def mover_exe(ruta, exe_carpeta):
    for archivo in os.listdir(ruta):
        if archivo.lower().endswith(".exe") | archivo.lower().endswith(".zip") | archivo.lower().endswith(".rar"):
            archivo_origen = os.path.join(ruta, archivo)
            archivo_destino = os.path.join(exe_carpeta, archivo)
            shutil.move(archivo_origen, archivo_destino)

def mover_docs(ruta, docs_carpeta):
    for archivo in os.listdir(ruta):
        if archivo.lower().endswith(".pdf") | archivo.lower().endswith(".docx") | archivo.lower().endswith(".xlsx"):
            archivo_origen = os.path.join(ruta, archivo)
            archivo_destino = os.path.join(docs_carpeta, archivo)
            shutil.move(archivo_origen, archivo_destino)

def mover_video(ruta, video_carpeta):
    for archivo in os.listdir(ruta):
        if archivo.lower().endswith((".mp4", ".avi", ".mov", ".mkv")):
            archivo_origen = os.path.join(ruta, archivo)
            archivo_destino = os.path.join(video_carpeta, archivo)
            shutil.move(archivo_origen, archivo_destino)

# crear la ventana principal
ventana = tk.Tk()
ventana.title("Organizador de rutas")
ventana.geometry("400x300")

# etiqueta
etiqueta = tk.Label(ventana, text="Selecciona una carpeta:")
etiqueta.pack(side=tk.TOP, pady=10)

# panel para alinear el textedit y el button de seleccionar
frame = tk.Frame(ventana)
frame.pack(side=tk.TOP, pady=10)

entrada = tk.Entry(frame, width=40)
entrada.pack(side=tk.LEFT, padx=10)

boton = tk.Button(frame, text="Seleccionar", command=seleccionar_ruta, width=50)
boton.pack(side=tk.RIGHT, padx=10)

# boton organizar direcctorios
botonOrganizar = tk.Button(ventana, text="Organizar", command=organizar_directorio)
botonOrganizar.pack(side=tk.TOP, padx=50)

# ejecuta la ventana
ventana.mainloop()
