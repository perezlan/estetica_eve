import os
from sre_parse import State
from pytube import YouTube
from tkinter import *
from tkinter import messagebox
import re

class Main(Tk):
    def __init__(self):
        super().__init__()
        self.ventana_inventario()
        self.widgets()


    def ventana_inventario(self):
        self.ANCHO=750
        self.ALTO=300
        POSX=400
        POSY=100

        self.anchoAlto=str(self.ANCHO)+"x"+str(self.ALTO)
        self.posicionX="+"+str(POSX)
        self.posicionY="+"+str(POSY)
        
        self.title("CONVERTIDOR")
        self.geometry(self.anchoAlto+self.posicionX+self.posicionY)
        self.resizable(False, False)
        self.frame=Frame(self)
        self.frame.pack()
        self.frame.config(width=self.ANCHO, height=self.ALTO)
        
    def widgets(self):
        Label(self.frame,
                text="INGRESAR URL DEL VIDEO EN YOUTUBE").place(x=100,y=70)
        
        self.dato_video =StringVar()
        self.dato_video.set("---")
        self.en_aviso=Entry(self.frame,
                            state=DISABLED,
                textvariable=self.dato_video)
        self.en_aviso.place(x=100,y=130,width=300)
        
        self.url=StringVar()
        self.en_url=Entry(self.frame,
                            textvariable=self.url,
                            width=100)
        self.en_url.place(x=100,y=100,height=30)
        
        btn_descargar_video=Button(self.frame,
                                text="Descargar Video",
                                command=self.descargarVideo).place(x=190,y=170)
    
        btn_descargar_audio=Button(self.frame,
                                text="Descargar Audio",
                                command=self.descargarAudio).place(x=300,y=170)
    
        btn_ver=Button(self.frame,
                                text="ver",
                                command=self.ver).place(x=100,y=170,width=80)
    
        btn_nuevo=Button(self.frame,
                                text="Nuevo",
                                command=self.nuevo).place(x=420,y=170)
        self.btn_listo=Button(self,
                        text="cambiar",
                        state=DISABLED)
        self.btn_listo.place(x=400,y=130)
        
    def descargarVideo(self):
        def descargar():
            #TOMAMOS LA DIRECCION DONDE ESTA EL VIDEO QUE SE DESCARGÓ Y CAMBIAMOS EL NOMBRE POR LO QUE HAY EN LA ENTRADA 
            nuevo_mp4="Youtube_Converter\\Videos\\"+self.dato_video.get()
            #REEMPLAZAMOS EL NOMBRE USANDO LA DIRECCION DONDE SE HABIA DESCARGADO EL VIDEO POR LA NUEVA QUE ES "nuevo_mp4"
            os.replace(self.mp4+".mp4",nuevo_mp4+".mp4")
            messagebox.showinfo("😎","VIDEO DESCARGADO")
            self.btn_listo.config(state=DISABLED,command="")
            self.en_aviso.configure(state=DISABLED)
        try:
            url=self.url.get()#OBTENEMOS EL URL QUE PEGAMOS
            self.yt=YouTube(url)
            self.dato_video.set(self.yt.title)
            video=self.yt.streams.get_highest_resolution()#OBTENEMOS LA RESOLUCION MAS ALTA DEL VIDEO
            video.download(output_path="Youtube_Converter\\Videos")#SE DESCARGA EL VIDEO Y SE CREA LA CARPETA VIDEOS DENTRO DE YOUTUBE_CONVERTER
            self.mp4="Youtube_Converter\\Videos\\"+self.dato_video.get()
            respuesta=messagebox.askyesno("mensaje","Quiere cambiar el nombre? ")
            if respuesta:
                self.en_aviso.configure(state=NORMAL)
                self.btn_listo.config(state=ACTIVE, command=descargar)
            else:
                messagebox.showinfo("😎","VIDEO DESCARGADO")
        except:
            messagebox.showwarning("!!!","ERROR AL DESCARGAR EL AUDIO!!!")
    
    def descargarAudio(self):
        def descargar():
            #TOMAMOS LA DIRECCION DONDE ESTA EL AUDIO QUE ES MP4 QUE SE DESCARGÓ Y CAMBIAMOS EL NOMBRE POR LO QUE HAY EN LA ENTRADA 
            self.nuevo_mp4="Youtube_Converter\\Audios\\"+self.dato_video.get()
            
            #REEMPLAZAMOS EL AUDIO QUE ESTA EN LA DIRECCION "self.mp4" 
            #POR LA NUEVA DIRECCION QUE ES "nuevo_mp4" PERO CAMBIAMOS LA EXTENSION .MP4 POR LA .MP3 
            #Y ASI CONVERTIRLO EN PURO AUDIO Y NO UN VIDEO DONDE SOLO ESTE EL AUDIO SIN VIDEO
            os.replace(self.mp4+".mp4",self.nuevo_mp4+".mp3")
            messagebox.showinfo("😎","AUDIO DESCARGADO")
            self.btn_listo.config(state=DISABLED,command="")
            self.en_aviso.configure(state=DISABLED)
            

        try:
            url=self.url.get()
            self.yt=YouTube(url)
            self.dato_video.set(self.yt.title)
            audio=self.yt.streams.get_audio_only()
            audio.download(output_path="Youtube_Converter\\Audios")#SE DESCARGA EL AUDIO DEL VIDEO Y SE CREA LA CARPETA AUDIOS DENTRO DE YOUTUBE_CONVERTER
            self.nameVideo = self.dato_video.get()
            characters = "'!?.¿¡"

            for x in range(len(characters)):
                self.nameVideo = self.nameVideo.replace(characters[x],"")
            print(self.nameVideo)

            self.mp4="Youtube_Converter\\Audios\\"+self.nameVideo#DIRECCION DONDE ESTA EL AUDIO DEL VIDEO
            
            respuesta=messagebox.askyesno("mensaje","Quiere cambiar el nombre? ")
            if respuesta:
                self.en_aviso.configure(state=NORMAL)
                self.btn_listo.config(state=ACTIVE, command=descargar)
            else:
                os.replace(self.mp4+".mp4",self.mp4+".mp3")
                messagebox.showinfo("😎","AUDIO DESCARGADO")
            
        except:
            messagebox.showwarning("!!!","ERROR AL DESCARGAR EL VIDEO!!!")


    def ver(self):
        #Assign link to"url"variable
        try:
            url=self.url.get()
            self.yt=YouTube(url)
            self.dato_video.set(self.yt.title)
        except:
            messagebox.showwarning("!!!","NO A INGRESADO UN URL")

    def nuevo(self):
        self.dato_video.set("---")
        self.url.set("")

def inicio():
    main=Main()
    main.mainloop()

if __name__ == "__main__":
    inicio()