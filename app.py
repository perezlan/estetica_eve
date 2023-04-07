from tkinter import *
from tkinter import messagebox
#importamos el archivo menu que esta en la carpeta clases
import clases.menu as menu



#CLASE PARA EL LOGIN
class login(Frame):
    
    def __init__(self,frame):
        self.ANCHO=800
        self.ALTO=455
        self.POSX=400
        self.POSY=100
        super().__init__(frame,width=self.ANCHO,height=self.ALTO)#constructor de la clase FRAME
            
        
        self.master=frame
        self.pack()
        self.fondo()
        self.widgets()
        
    
    def fondo(self):
        self.imagen=PhotoImage(file="imagenes_fondo\\sesion.png")
        self.Lb=Label(self,image=self.imagen).place(x=0,y=0)
        
        
    #FUNCION DONDE CREAREMOS ETIQUETAS, ENTRADAS, BOTONES, ETC...
    def widgets(self):
        color_et_us="#c0504f"
        color_btn_in="#804331"
        #CREACION DE ETIQUETAS Y POSICION
        self.et_usuario=Label(self,
                        text="USUARIO",
                        font=("Courier",12),
                        bg=color_et_us,width=15).place(x=20,y=205)

        self.et_contraseña=Label(self,
                            text="CONTRASEÑA",
                            font=("Courier",12),
                            bg=color_et_us,width=15).place(x=20,y=275)


        self.et_error=Label(self,
                        text="ERROR: EL USUARIO O CONTRASEÑA HAN SIDO INCORRECTO",
                        fg="red"
                        )


        self.im_candado=PhotoImage(file="imagenes\\candado.png")
        
        self.et_candado=Label(self,
                            image=self.im_candado)
        
        self.et_candado.place(x=480,y=275)
        
        
        self.im_usuario=PhotoImage(file="imagenes\\usuario.png")
        
        self.et_IMusuario=Label(self,
                            image=self.im_usuario)
        
        self.et_IMusuario.place(x=480,y=205)
        


        #CREACION DE ENTRADAS Y POSICION
        self.en_usuario=Entry(self,
                        width=50)
        self.en_usuario.place(x=176,y=205,
                        height=25)
        
        
        self.en_contraseña=Entry(self,
                            width=50,
                            show="*")
        self.en_contraseña.place(x=176,y=275,
                            height=25)
        
        #CREACIO DE BOTONES
        self.btn_ingresar=Button(self,
                            text="Ingresar",
                            font=("Courier",12),
                            bg=color_btn_in,
                            width=15,
                            command=self.entrar).place(x=190,y=325)
        self.btn_salir=Button(self,
                            text="salir",
                            font=("Courier",12),
                            bg=color_btn_in,
                            width=15,
                            command=self.salir).place(x=190,y=360)

    """#CREACIO DE COMANDOS"""
    #FUNCION PARA DESTRUIR LA VENTANA QUE ESTA CON EL LOGIN
    def salir(self):
        ventana.destroy()
        
    #FUNCION PARA QUE FUNCIONE EL LOGIN 
    def entrar(self):
        usuario="mario"
        password="123"
        
        if(self.en_usuario.get().lower()==usuario and self.en_contraseña.get()==password):
            self.et_error.config(text="😊😊😊😊😊")
            self.et_error.place(x=120,y=300)
            #linea para mostrar una ventanita de informacion
            messagebox.showinfo("Mensaje","BIENVENIDO!!!")
            self.en_contraseña.configure(state=DISABLED)
            self.en_usuario.configure(state=DISABLED)
            ventana.destroy()
            menu.main_menu()
            
            
        else:
            self.et_error.config(text="ERROR: EL USUARIO O CONTRASEÑA HAN SIDO INCORRECTO 😭😭")
            self.et_error.place(x=110,y=300)
            #linea para mostrar una ventanita de error
            messagebox.showerror("ERROR","USUARIO O CONTRASEÑA INCORRECTO")



#variables para moldear la ventana
ANCHO=800
ALTO=455

POSX=400
POSY=100

anchoAlto=str(ANCHO)+"x"+str(ALTO)
posicionX="+"+str(POSX)
posicionY="+"+str(POSY)

ventana=Tk()
ventana.title("SESION")
ventana.state(newstate="normal")
ventana.resizable(False,False)
ventana.iconbitmap("imagenes\\inventario.ico")
ventana.geometry(anchoAlto+posicionX+posicionY)

if __name__ == "__main__":
    Login=login(ventana)
    Login.mainloop()


