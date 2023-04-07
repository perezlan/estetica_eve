
from tkinter import *
from clases import CrearCitas,StyleWidgets,VerCitas,Inventario
import datetime
#import clases.VerCitas as VerCitas, clases.CrearCitas as CrearCitas


class Menu(Tk):
    def __init__(self):
        super().__init__()
        self.ventana_inventario()
        self.fondo()
        self.widgets()
        self.iconos_im()


    def ventana_inventario(self):
        self.ANCHO=800
        self.ALTO=455
        POSX=400
        POSY=100

        self.anchoAlto=str(self.ANCHO)+"x"+str(self.ALTO)
        self.posicionX="+"+str(POSX)
        self.posicionY="+"+str(POSY)
        
        self.title("MENU")
        self.geometry(self.anchoAlto+self.posicionX+self.posicionY)
        self.resizable(False, False)
        self.frame=Frame(self)
        self.frame.pack()
        self.frame.config(width=self.ANCHO, height=self.ALTO)
        
        self.frame.config(bg="black")

    def fondo(self):
        self.imagen=PhotoImage(file="imagenes_fondo\\menu.png")
        self.fondoo=Label(self.frame,
                    image=self.imagen)
        self.fondoo.place(x=0,y=0)

    def widgets(self):
        self.btn_verCitas=Button(self.frame,
                            text="CITAS CLIENTES",
                            bg="pink",
                            font=("Courier", 14, "italic"),
                            fg="#843DC3",
                            relief="groove", 
                            borderwidth=5,
                            command=self.menu_vercitas)
        self.btn_verCitas.place(x=100,y=100,width=200,height=40)
        
        self.btn_hacerCitas=Button(self.frame,
                            text="NUEVA CITAS",
                            bg="pink",
                            font=("Courier", 14, "italic"),
                            fg="#843DC3",
                            relief="groove", 
                            borderwidth=5,
                            command=self.menu_crearcitas)
        self.btn_hacerCitas.place(x=100,y=210,width=200,height=40)
        
        self.btn_inventario=Button(self.frame,
                            text="INVENTARIO",
                            bg="pink",
                            font=("Courier", 14, "italic"),
                            fg="#843DC3",
                            relief="groove", 
                            borderwidth=5,
                            command=self.menu_inventario)
        self.btn_inventario.place(x=100,y=325,width=200,height=40)
        
        self.btn_salir=Button(self.frame,
                            text="SALIR",
                            bg="pink",
                            font=("Courier", 14, "italic"),
                            fg="#843DC3",
                            relief="groove", 
                            borderwidth=5,
                            command=self.menu_destroy)
        self.btn_salir.place(x=200,y=390,width=100,height=40)
        
        fecha=datetime.datetime.now().strftime("%Y-%m-%d")
        Label(self,
                text=fecha,
                **StyleWidgets.label_fecha1).place(x=20,y=390,width=150,height=40)

    def iconos_im(self):
        self.im_calendario=PhotoImage(file="imagenes\\calendario.png")
        self.et_calendario=Label(self.frame,
                                image=self.im_calendario,
                                bg="#FEDED9")
        self.et_calendario.place(x=30,y=90,width=64,height=64)
        
        
        self.im_agregar=PhotoImage(file="imagenes\\boton-agregar.png")
        self.et_agregar=Label(self.frame,
                                image=self.im_agregar,
                                bg="#FEDED9")
        self.et_agregar.place(x=25,y=198)


        self.im_inv=PhotoImage(file="imagenes\\inventario.png")
        self.et_inv=Label(self.frame,
                                image=self.im_inv,
                                bg="#FEDED9")
        self.et_inv.place(x=25,y=310)

    def menu_ocultar(self):
        self.withdraw()

    def menu_vercitas(self):
        self.destroy()
        VerCitas.iniciar_VerCitas()

    def menu_crearcitas(self):
        self.destroy()
        CrearCitas.iniciar_CrearCitas()

    def menu_inventario(self):
        self.destroy()
        Inventario.iniciar_inventario()

    def menu_mostrar(self):
        self.deiconify()

    def menu_destroy(self):
        self.destroy()



def main_menu():
    menu=Menu()
    menu.mainloop()


if __name__ == "__main__":
    main_menu()