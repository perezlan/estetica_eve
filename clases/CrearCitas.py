from tkinter import *
from clases import StyleWidgets as StyleWidgets, bd as bd, menu as menu
from datetime import date
from datetime import datetime
from tkinter import messagebox



class crearCitas(Tk):
    def __init__(self):
        super().__init__()
        self.ventanaCitas()
        self.fondo()
        self.widgets()
    
    def ventanaCitas(self):
        self.ancho=500
        self.alto=750
        self.x_ventana =self.winfo_screenwidth() // 2 - self.ancho // 2
        self.y_ventana = self.winfo_screenheight() // 2 - (self.alto // 2)-50
        self.title("AGENDAR CITAS")
        self.geometry(str(self.ancho)+"x"+str(self.alto)+"+"+str(self.x_ventana)+"+"+str(self.y_ventana))
        self.resizable(False,False)


    def widgets(self):
        btn_salir=Button(self,
                        text="salir",
                        bg="red",
                        command=self.cerrar_CrearCitas,
                        **StyleWidgets.boton)
        btn_salir.place(x=300, y=660,width=100,height=40)
        
        btn_guardar=Button(self,
                            text="Guardar",
                            **StyleWidgets.boton,
                            bg="green",
                            command=self.guardad_datos)
        btn_guardar.place(x=80, y=660,width=100,height=40)



        Label(self,
            text="Nombre: ",
            **StyleWidgets.label,).place(x=10, y=50)

        self.en_nombre=Entry(self,
                            **StyleWidgets.entrada)
        self.en_nombre.place(x=150, y=50,height=30)


        self.ejemplo_fecha=StringVar()
        self.ejemplo_fecha.set(date.today())

        
        Label(self,
            text="YYYY-MM-DD",
            **StyleWidgets.label).place(x=150, y=120)

        self.ejemplo=Label(self,
            text="Fecha: ",
            **StyleWidgets.label).place(x=10, y=150)
        

        self.en_fecha=Entry(self,
                            **StyleWidgets.entrada,
                            textvariable=self.ejemplo_fecha,)
        self.en_fecha.place(x=150, y=150,height=30)


        self.en_tele=IntVar()
        self.en_tele.set(0)
        Label(self,
            text="Telefono: ",
            **StyleWidgets.label).place(x=10, y=250)

        self.en_tel=Entry(self,
                        **StyleWidgets.entrada,
                        textvariable=self.en_tele)
        self.en_tel.place(x=150, y=250,height=30)


        noww=datetime.now()
        self.now = StyleWidgets.current_date_format(noww) 
        Label(self,
            text=self.now,
            **StyleWidgets.label_fecha).place(x=10, y=350)

    def fondo(self):
        self.imagen=PhotoImage(file="imagenes_fondo\\crear_cita.png")
        self.fondoo=Label(self,
                    image=self.imagen)
        self.fondoo.place(x=0,y=0)

    def cerrar_CrearCitas(self):
        self.destroy()
        menu.main_menu()

    def guardad_datos(self):
        tel=self.en_tel.get()
        if len(tel)<=10:
            fecha=self.en_fecha.get()
            if (self.en_nombre.get()!="" and fecha!=""):
                datos=(self.en_nombre.get(),fecha,tel,"---")
                self.insertar=bd.insertar(datos)
                if self.insertar:
                    messagebox.showinfo("😊😊","CITA GUARDADA")
                    self.destroy()
                    menu.main_menu()
                else:
                    messagebox.showerror("😭😭","ERROR AL GUARDAR DATOS")
            else:
                messagebox.showerror("😭😭","ERROR AL GUARDAR DATOS")
        else:
            messagebox.showinfo("MENSAJE","TELEFONO MUY LARGO")

def iniciar_CrearCitas():
    WcrearCitas=crearCitas()
    WcrearCitas.mainloop()

if __name__=="__main__":
    iniciar_CrearCitas()