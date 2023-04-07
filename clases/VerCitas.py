from tkinter import *
from tkinter.ttk import Treeview
from clases import bd,StyleWidgets,menu
from tkinter import messagebox

class verCitas(Tk):
    def __init__(self):
        super().__init__()
        self.ventanaCitas()
        self.fondo()
        self.widgets()
        self.tablaCitas()

    
    def ventanaCitas(self):
        self.ancho=1200
        self.alto=700
        self.x_ventana =self.winfo_screenwidth() // 2 - self.ancho // 2
        self.y_ventana = self.winfo_screenheight() // 2 - (self.alto // 2)-50
        self.title("Citas Hechas")
        self.geometry("1200x700+"+str(self.x_ventana)+"+"+str(self.y_ventana))
        self.resizable(False,False)
        self.config(bg="#FEDED9")

    def fondo(self):
        self.imagen=PhotoImage(file="imagenes_fondo\\prueba1.png")
        self.fondoo=Label(self,
                    image=self.imagen)
        self.fondoo.place(x=0,y=0)

    def widgets(self):
        btn_salir=Button(self,
                text="salir",
                **StyleWidgets.boton_verCitas,
                bg="brown",
                command=self.cerrarVerCitas)
        btn_salir.place(x=600, y=600,width=100,height=40)
        
        btn_Si_Asistencia=Button(self,
                text="Asistió",
                **StyleWidgets.boton_verCitas,
                command=self.asistio)
        btn_Si_Asistencia.place(x=150, y=650,width=100,height=40)
        
        btn_No_Asistencia=Button(self,
                text="No Asistió",
                **StyleWidgets.boton_verCitas,
                command=self.Noasistio)
        btn_No_Asistencia.place(x=300, y=650,width=100,height=40)
        
        btn_guardar=Button(self,
                text="Guardar",
                bg="green",
                **StyleWidgets.boton_verCitas,
                command=self.guardar)
        btn_guardar.place(x=5, y=650,width=100,height=40)
        
        btn_limpiar=Button(self,
                text="Limpiar",
                **StyleWidgets.boton_verCitas,
                command=self.limpiar)
        btn_limpiar.place(x=450, y=650,width=100,height=40)
        
        btn_borrar=Button(self,
                text="borrar",
                bg="red",
                **StyleWidgets.boton_verCitas,
                command=self.borrar)
        btn_borrar.place(x=600, y=650,width=100,height=40)
        
        self.citaID=IntVar()
        Label(self,
                text="ID: ",
                **StyleWidgets.label_verCitas).place(x=00, y=455)

        self.ID=Entry(self,
                        **StyleWidgets.entrada_verCitas,
                        textvariable=self.citaID,
                        state=DISABLED)
        self.ID.place(x=150, y=455,height=30)


        self.citaNombre=StringVar()
        Label(self,
                text="Nombre: ",
                **StyleWidgets.label_verCitas,).place(x=00, y=500)

        self.en_nombre=Entry(self,
                        **StyleWidgets.entrada_verCitas,
                        textvariable=self.citaNombre)
        self.en_nombre.place(x=150, y=500,height=30)


        self.citaFecha=StringVar()
        Label(self,
                text="Fecha: ",
                **StyleWidgets.label_verCitas).place(x=0, y=550)


        Label(self,
                text="YYYY-MM-DD",
                **StyleWidgets.label_verCitas).place(x=480, y=550,height=30)
        self.en_fecha=Entry(self,
                            **StyleWidgets.entrada_verCitas,
                            textvariable=self.citaFecha)
        self.en_fecha.place(x=150, y=550,height=30)



        self.citaTel=IntVar()
        Label(self,
                text="Telefono: ",
                **StyleWidgets.label_verCitas).place(x=0, y=600)

        self.en_tel=Entry(self,
                        **StyleWidgets.entrada_verCitas,
                        textvariable=self.citaTel)
        self.en_tel.place(x=150, y=600,height=30)


    def cerrarVerCitas(self):
            self.destroy()
            menu.main_menu()

    def tablaCitas(self):
        self.tabla=Treeview(self,height=self.alto,columns=("#0", "#1", "#2","#3","#4"),show="headings")
        self.tabla.place(x=0,y=50,width=700,height=400)
        self.tabla.heading("#1",text="ID",anchor=CENTER)
        self.tabla.heading("#2",text="Nombre",anchor=CENTER)
        self.tabla.heading("#3",text="Fecha",anchor=CENTER)
        self.tabla.heading("#4",text="Telefono",anchor=CENTER)
        self.tabla.heading("#5",text="Asistencia",anchor=CENTER)
        
        self.tabla.column("#1",width=50,anchor="c")
        self.tabla.column("#2",anchor="c")
        self.tabla.column("#3",width=100,anchor="c")
        self.tabla.column("#4",width=90,anchor="c")
        self.tabla.column("#5",width=90,anchor="c")
        
        #CON ESTE PEDASO DE CODIGO BORRAMOS LA TABLA PORQUE SI NO SE AMONTONA LOS NUEVOS DATOS
        registro=self.tabla.get_children()
        for elementos in registro:
            self.tabla.delete(elementos)

        #CON ESTE PEDASO DE CODIGO MOSTRAMOS LOS DATOS DE LAS CITAS DE LA BD
        datos=bd.mostrar_citas()
        for row in datos:
            self.tabla.insert("",0,text=row[0],values=(row[0],row[1],row[2],row[3],row[4]))

        #CON ESTA LINEA DE CODIGO SELECCIONAMOS LOS DATOS DE LAS CITAS 
        self.tabla.bind("<Button>",self.seleccionar_datos)

        #FUNCION PARA TOMAR LOS DATOS DE LA BASE DE DATOS Y MOSTRARLOS PA EDITAR O ELIMINAR
    def seleccionar_datos(self,event):
        try:
            item=self.tabla.identify('item',event.x,event.y)
            self.citaID.set(self.tabla.item(item,"text"))
            self.citaNombre.set(self.tabla.item(item,"values")[1])
            self.citaFecha.set(self.tabla.item(item,"values")[2])
            self.citaTel.set(self.tabla.item(item,"values")[3])
        except:
            messagebox.showwarning("!!!!","SELECCIONE UNA CITA")

    def limpiar(self):
        self.citaID.set(0)
        self.citaNombre.set("")
        self.citaFecha.set("")
        self.citaTel.set(0)

    def guardar(self):

        conexion,cursor=bd.conectar_sqlite()
        sql=f"UPDATE datos SET nombre='{self.citaNombre.get()}',fecha='{self.citaFecha.get()}',telefono='{self.citaTel.get()}' WHERE ID={self.citaID.get()}"
        cursor.execute(sql)
        conexion.commit()#commit es para actualizar los datos
        conexion.close()
        self.tablaCitas()
        self.limpiar()
        

    def asistio(self):
        conexion,cursor=bd.conectar_sqlite()
        sql=f"UPDATE datos SET Asistencia='😎👍' WHERE ID={self.citaID.get()}"
        cursor.execute(sql)
        conexion.commit()#commit es para actualizar los datos
        conexion.close()
        self.tablaCitas()
        self.limpiar()
    
    def Noasistio(self):
        conexion,cursor=bd.conectar_sqlite()
        sql=f"UPDATE datos SET Asistencia='😔👎' WHERE ID={self.citaID.get()}"
        cursor.execute(sql)
        conexion.commit()#commit es para actualizar los datos
        conexion.close()
        self.tablaCitas()
        self.limpiar()
    
    def borrar(self):
        respuesta=messagebox.askyesno("Mensaje","¿Esta seguro que quiere borrar esta cita?")
        if respuesta:
            conexion,cursor=bd.conectar_sqlite()
            sql=f"DELETE FROM datos WHERE ID={self.citaID.get()}"
            cursor.execute(sql)
            conexion.commit()#commit es para actualizar los datos
            conexion.close()
            self.tablaCitas()
            self.limpiar()
        


def iniciar_VerCitas():
    WverCitas=verCitas()
    WverCitas.mainloop()

if __name__=="__main__":
    iniciar_VerCitas()