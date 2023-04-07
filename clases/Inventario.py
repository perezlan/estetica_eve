from tkinter import *
from tkinter.ttk import Treeview
from clases import bd,StyleWidgets,menu
from tkinter import messagebox
from datetime import date
from datetime import datetime

class inventario(Tk):
    def __init__(self):
        super().__init__()
        self.ventanaCitas()
        self.fondo()
        self.widgets()
        self.tablaInventario()

    
    def ventanaCitas(self):
        self.ancho=1200
        self.alto=700
        self.x_ventana =self.winfo_screenwidth() // 2 - self.ancho // 2
        self.y_ventana = self.winfo_screenheight() // 2 - (self.alto // 2)-50
        self.title("Inventario Productos")
        self.geometry("1200x700+"+str(self.x_ventana)+"+"+str(self.y_ventana))
        self.resizable(False,False)
        self.config(bg="#FEDED9")

    def fondo(self):
        self.imagen=PhotoImage(file="imagenes_fondo\\inventario1.png")
        self.fondoo=Label(self,
                    image=self.imagen)
        self.fondoo.place(x=0,y=0)

    def widgets(self):
        noww=datetime.now()
        self.now = StyleWidgets.current_date_format(noww) 

        Label(self,
            text=self.now,
            **StyleWidgets.label_fecha).place(x=10, y=650)
        
        btn_salir=Button(self,
                            **StyleWidgets.boton,
                            text="Salir",
                            anchor=CENTER,
                            bg="brown",
                            command=self.cerrar_inventario)
        btn_salir.place(x=750,y=320,width=100,height=40)
        
        btn_ventas=Button(self,
                            **StyleWidgets.boton,
                            text="VENTAS",
                            anchor=CENTER,
                            command=self.ventana_ventas)
        btn_ventas.place(x=750,y=220,width=100,height=40)
        
        btn_productos=Button(self,
                            **StyleWidgets.boton,
                            text="AGREGRAR PRODUCTO",
                            anchor=CENTER,
                            command=self.ventana_producto)
        btn_productos.place(x=750,y=120,width=200,height=40)
        
        btn_efectuar=Button(self,
                            **StyleWidgets.boton,
                            text="CAPTURAR",
                            bg="yellow",
                            anchor=CENTER,
                            command=self.efectuar)
        btn_efectuar.place(x=750,y=650,width=200,height=40)
        
        btn_guardar=Button(self,
                            **StyleWidgets.boton,
                            text="ACTUALIZAR PRODUCTO",
                            bg="green",
                            anchor=CENTER,
                            command=self.actualizar_datos)
        btn_guardar.place(x=550,y=470,width=300,height=40)
        
        btn_eliminar=Button(self,
                            **StyleWidgets.boton,
                            text="ELIMINAR PRODUCTO",
                            bg="red",
                            anchor=CENTER,
                            command=self.eliminar_datos)
        btn_eliminar.place(x=850,y=470,width=300,height=40)

    
        self.invID=IntVar()
        Label(self,
                text="ID: ",
                **StyleWidgets.label_verCitas).place(x=00, y=455)

        self.ID=Entry(self,
                        **StyleWidgets.entrada_verCitas,
                        textvariable=self.invID,
                        state=DISABLED)
        self.ID.place(x=150, y=455,height=30)


        self.invNombre=StringVar()
        Label(self,
                text="Nombre: ",
                **StyleWidgets.label_verCitas,).place(x=00, y=500)

        self.en_nombre=Entry(self,
                        **StyleWidgets.entrada_verCitas,
                        textvariable=self.invNombre)
        self.en_nombre.place(x=150, y=500,height=30)


        self.invProovedor=StringVar()
        Label(self,
                text="Proovedor ",
                **StyleWidgets.label_verCitas).place(x=500, y=550)


        self.en_proovedor=Entry(self,
                            **StyleWidgets.entrada_verCitas,
                            textvariable=self.invProovedor)
        self.en_proovedor.place(x=650, y=550,height=30)
        
        self.invColor=StringVar()
        Label(self,
                text="Color: ",
                **StyleWidgets.label_verCitas).place(x=0, y=550)


        self.en_color=Entry(self,
                            **StyleWidgets.entrada_verCitas,
                            textvariable=self.invColor)
        self.en_color.place(x=150, y=550,height=30)



        self.invCantidad=IntVar()
        Label(self,
                text="Cantidad: ",
                **StyleWidgets.label_verCitas).place(x=0, y=600)

        self.en_cantidad=Entry(self,
                        **StyleWidgets.entrada_verCitas,
                        textvariable=self.invCantidad)
        self.en_cantidad.place(x=150, y=600,height=30)


        Label(self,
                text="Vendido: ",
                **StyleWidgets.label_inv).place(x=500, y=600)
        self.invVendido=IntVar()
        self.invVendido.set(0)
        self.en_vendido=Entry(self,
                                **StyleWidgets.entrada_inv,
                                textvariable=self.invVendido)
        self.en_vendido.place(x=650, y=600,height=30)

    def tablaInventario(self):
        self.tabla=Treeview(self,height=self.alto,columns=("#0", "#1", "#2","#3","#4"),show="headings")
        self.tabla.place(x=0,y=50,width=700,height=400)
        self.tabla.heading("#1",text="ID",anchor=CENTER)
        self.tabla.heading("#2",text="Nombre",anchor=CENTER)
        self.tabla.heading("#3",text="Proovedor",anchor=CENTER)
        self.tabla.heading("#4",text="Color",anchor=CENTER)
        self.tabla.heading("#5",text="Cantidad",anchor=CENTER)
        
        self.tabla.column("#1",width=50,anchor="c")
        self.tabla.column("#2",anchor="c")
        self.tabla.column("#3",anchor="c")
        self.tabla.column("#4",width=90,anchor="c")
        self.tabla.column("#5",width=90,anchor="c")
    
        self.tabla.bind("<Button>",self.seleccionar_datos)
        self.reeiscribir_datos()

    def reeiscribir_datos(self):
        #CON ESTE PEDASO DE CODIGO BORRAMOS LA TABLA PORQUE SI NO SE AMONTONA LOS NUEVOS DATOS
        registro=self.tabla.get_children()
        for elementos in registro:
            self.tabla.delete(elementos)
        
        datos=bd.mostrar_inventario()
        for row in datos:
            self.tabla.insert("",0,text=row[0],values=(row[0],row[1],row[2],row[3],row[4],row[5]))

    def seleccionar_datos(self,event):
        try:
            item=self.tabla.identify('item',event.x,event.y)
            self.invID.set(self.tabla.item(item,"text"))
            self.invNombre.set(self.tabla.item(item,"values")[1])
            self.invProovedor.set(self.tabla.item(item,"values")[2])
            self.invColor.set(self.tabla.item(item,"values")[3])
            self.invCantidad.set(self.tabla.item(item,"values")[4])
            self.vendido=self.tabla.item(item,"values")[5]
        except:
            messagebox.showinfo("!!","SELECCIONE UN DATO")

    def cerrar_inventario(self):
        self.destroy()
        menu.main_menu()

    def efectuar(self):
        conexion,cursor=bd.conectar_sqlite()
        fecha=str(date.today())
        nombre=self.invNombre.get()
        proovedor=self.invProovedor.get()
        vendido=str(self.invVendido.get())
        if nombre!="" and proovedor!="":
            datos=fecha,nombre,proovedor
            sql="INSERT INTO ventas (Fecha,Nombre,Proovedor,Vendido) values (?,?,?,"+vendido+")"
            cursor.execute(sql,datos)
            conexion.commit()
            conexion.close()
            messagebox.showinfo("MENSAJE","VENTAS CAPTURADAS")
            
            conexion,cursor=bd.conectar_sqlite()
            self.invCantidad.set(self.invCantidad.get()-self.invVendido.get())
            sql2="UPDATE inventario set Cantidad="+str(self.invCantidad.get())+" where ID="+str(self.invID.get())+""
            cursor.execute(sql2)
            conexion.commit()
            conexion.close()
            self.invVendido.set(0)
            self.reeiscribir_datos()
        else:
            messagebox.showinfo("MENSAJE","NO SELECCIONÓ NADA")

    def actualizar_datos(self):
        conexion,cursor=bd.conectar_sqlite()
        self.invNombre.get()
        proovedor=self.invProovedor.get()
        color=self.invColor.get()
        cantidad=self.invCantidad.get()
        ID=str(self.invID.get())
        try:
            if self.invNombre.get()!="" and proovedor!="":
                sql=f"UPDATE inventario set nombre='{self.invNombre.get()}',proovedor='{proovedor}',color='{color}',cantidad='{cantidad}' where ID={ID}"
                cursor.execute(sql)
                conexion.commit()
                conexion.close()
                messagebox.showinfo("😊😊","DATOS ACTUALIZADOS")
                self.reeiscribir_datos()
            else:
                messagebox.showinfo("MENSAJE","NO SELECCIONÓ NADA")
        except Exception as e:
            messagebox.showwarning("!!!",e)

    def eliminar_datos(self):
        conexion,cursor=bd.conectar_sqlite()
        self.invNombre.get()
        proovedor=self.invProovedor.get()
        color=self.invColor.get()
        cantidad=self.invCantidad.get()
        ID=str(self.invID.get())
        try:
            if self.invNombre.get()!="" and proovedor!="":
                respuesta=messagebox.askyesno("MENSAJE","¿SEGURO QUE DESEA BORRAR ESTE PRODUCTO?")
                if respuesta:
                    sql=f"DELETE FROM inventario where ID={ID}"
                    cursor.execute(sql)
                    conexion.commit()
                    conexion.close()
                    messagebox.showinfo("😊😊","DATOS ELIMINADOS")
                    self.reeiscribir_datos()
                else:
                    messagebox.showinfo("MENSAJE","NO SE HA BORRADO NADA")
            else:
                messagebox.showinfo("MENSAJE","NO SELECCIONÓ NADA")
        except Exception as e:
            messagebox.showwarning("!!!",e)
#"""CREACION DE LA NUEVA VENTANA PARA VENTAS"""***************************************************

    def ventana_ventas(self):   
        ventas=Toplevel(self,
                        width=850,
                        height=400
                        )
        x_ventana =ventas.winfo_screenwidth() // 2 - 800 // 2
        y_ventana = ventas.winfo_screenheight() // 2 - (400 // 2)-50
        ventas.geometry("+"+str(x_ventana)+"+"+str(y_ventana))
        ventas.title("VENTAS")

    #*******************************Funciones*******************************
        def reeiscribir_datos():
        #CON ESTE PEDASO DE CODIGO BORRAMOS LA TABLA PORQUE SI NO SE AMONTONA LOS NUEVOS DATOS
            registros=tabla.get_children()
            for elementos in registros:
                tabla.delete(elementos)
            datos=bd.mostrar_ventas()
            for row in datos:
                tabla.insert("",0,text=row[0],values=(row[0],row[1],row[2],row[3],row[4],row[5]))
            
        
        def seleccionar_cantidad(event):
            try:
                item=tabla.identify('item',event.x,event.y)
                self.cantidad.set(tabla.item(item,"values")[4])
                self.id_ventas=tabla.item(item,"values")[0]
                print(self.id_ventas)
            except:
                messagebox.showinfo("!!","SELECCIONE UN DATO")
        
        def total():
            total_costo=(self.cantidad.get()*self.costo.get())
            self.total.set(total_costo)
        
        def guardar():
            conexion,cursor=bd.conectar_sqlite()
            sql=f"UPDATE ventas SET Total='{self.total.get()}' where ID={self.id_ventas}"
            cursor.execute(sql)
            conexion.commit()
            conexion.close()
            reeiscribir_datos()
        
        def borrar():
            conexion,cursor=bd.conectar_sqlite()
            respuesta=messagebox.askyesno("MENSAJE","DESEA ELIMINAR ESTA VENTA?")
            if respuesta:
                sql=f"DELETE FROM ventas WHERE Id={self.id_ventas}"
                cursor.execute(sql)
                conexion.commit()
                conexion.close()
                reeiscribir_datos()
                messagebox.showinfo("😊😊","VENTA BORRADA")
            else:
                messagebox.showinfo("😊😊","OPERACION CANCELADA")
                
    #*******************************Funciones FIN***************************************************************
    
    #******************************TABLA PARA MOSTRAR VENTAS *******************************************
        tabla=Treeview(ventas,height=self.alto,columns=("#0", "#1", "#2","#3","#4","#5","#6"),show="headings")
        tabla.place(x=0,y=0,width=800,height=300)
        tabla.heading("#1",text="id",anchor=CENTER)
        tabla.heading("#2",text="Fecha",anchor=CENTER)
        tabla.heading("#3",text="Nombre",anchor=CENTER)
        tabla.heading("#4",text="Proovedor",anchor=CENTER)
        tabla.heading("#5",text="#Vendido",anchor=CENTER)
        tabla.heading("#6",text="$TOTAL",anchor=CENTER)
        tabla.column("#1",width=10,anchor="c")
        tabla.column("#2",anchor="c")
        tabla.column("#3",anchor="c")
        tabla.column("#4",anchor="c")
        tabla.column("#5",width=100,anchor="c")
        tabla.column("#6",width=100,anchor="c")
        tabla.bind("<Button>",seleccionar_cantidad)
        reeiscribir_datos()
    #****************************************   ******* ************************    ****
    #******************************WIDGETS VENTAS****************************
        btn_actualizar=Button(ventas,
                                **StyleWidgets.boton,
                                text="GUARDAR",
                                anchor=CENTER,
                                bg="green",
                                command=guardar).place(x=0,y=301)
        btn_eliminar=Button(ventas,
                            **StyleWidgets.boton,
                                text="BORRAR",
                                anchor=CENTER,
                                bg="red",
                                command=borrar).place(x=150,y=301)
        btn_salir=Button(ventas,
                                **StyleWidgets.boton,
                                text="SALIR",
                                anchor=CENTER,
                                bg="brown",
                                command=ventas.destroy).place(x=250,y=301)
        
        btn_ver=Button(ventas,
                            **StyleWidgets.boton,
                            text="VER TOTAL",
                            anchor=CENTER,
                            command=total).place(x=650,y=301)
        self.cantidad=IntVar()
        en_price=Entry(ventas,
                        font=("Courier", 14, "italic"),
                        bg="yellow",
                        width=5,
                        state=DISABLED,
                        textvariable=self.cantidad).place(x=440,y=350)
        
        self.costo=IntVar()
        en_costo=Entry(ventas,
                        font=("Courier", 14, "italic"),
                        bg="yellow",
                        width=10,
                        textvariable=self.costo).place(x=550,y=350)
        
        self.total=IntVar()
        en_total=Entry(ventas,
                        font=("Courier", 14, "italic"),
                        bg="yellow",
                        width=10,
                        state=DISABLED,
                        textvariable=self.total).place(x=740,y=350)
        Label(ventas,
                bg="yellow",
                font=("Courier", 14, "italic"),
                text="#piezas").place(x=350,y=350)
        
        Label(ventas,
                bg="yellow",
                font=("Courier", 14, "italic"),
                text="$/p").place(x=505,y=350)
        Label(ventas,
                bg="green",
                fg="black",
                font=("Courier", 14, "italic"),
                text="$TOTAL").place(x=665,y=350)
        
    #******************************FIN WIDGETS VENTAS****************************


#"""CREACION DE LA NUEVA VENTANA PARA AGREGAR PRODUCTOS"""**********************************************************************
    def ventana_producto(self):   
        productos=Toplevel(self,
                        width=500,
                        height=400
                        )
        x_ventana =productos.winfo_screenwidth() // 2 - 500 // 2
        y_ventana = productos.winfo_screenheight() // 2 - (700 // 2)-50
        productos.geometry("+"+str(x_ventana)+"+"+str(y_ventana))
        productos.title("AGREGRAR")
        

#*******************************Funciones***************************************************************
        def limpiar():
            invNombre.set("")
            invProovedor.set("")
            invColor.set("")
            invCantidad.set(0)

        def guardar_product():
            color=invColor.get()
            if (en_nombre.get()!="" and en_proovedor.get()!="" and en_cantidad.get()):
                try:
                    if color=="":
                        color="NINGUNO"
                    conexion,cursor=bd.conectar_sqlite()
                    sql="INSERT into inventario (nombre,Proovedor,Color,Cantidad,Vendido) values (?,?,?,?,?)"
                    datos=en_nombre.get(),en_proovedor.get(),color,en_cantidad.get(),0
                    cursor.execute(sql,datos)
                    conexion.commit()
                    conexion.close()
                    limpiar()
                    self.reeiscribir_datos()
                    messagebox.showinfo("😊😊","PRODUCTO GUARDADO")
                except:
                    messagebox.showwarning("!!","ERROR AL GUARDAR PRODUCTO")
            else:
                messagebox.showwarning("!!","ERROR AL GUARDAR PRODUCTO")
                
#*******************************Funciones FIN***************************************************************
#********************************WIDGETS PRODUCTOS************************************************
        btn_salir=Button(productos,
                        **StyleWidgets.boton,
                            text="Salir",
                            anchor=CENTER,
                            bg="red",
                            command=productos.destroy)
        btn_salir.place(x=350,y=350)
#*****
        btn_guardar=Button(productos,
                        **StyleWidgets.boton,
                            text="Guardar Producto",
                            anchor=CENTER,
                            bg="green",
                            command=guardar_product)
        btn_guardar.place(x=50,y=350)
#*****
        invNombre=StringVar()
        Label(productos,
                text="Nombre: ",
                **StyleWidgets.label_verCitas,).place(x=00, y=50)

        en_nombre=Entry(productos,
                        **StyleWidgets.entrada_verCitas,
                        textvariable=invNombre)
        en_nombre.place(x=150, y=50,height=30)
#*****

        invProovedor=StringVar()
        Label(productos,
                text="Proovedor: ",
                **StyleWidgets.label_verCitas).place(x=0, y=100)


        en_proovedor=Entry(productos,
                            **StyleWidgets.entrada_verCitas,
                            textvariable=invProovedor)
        en_proovedor.place(x=150, y=100,height=30)
#*****
        invColor=StringVar()
        Label(productos,
                text="Color: ",
                **StyleWidgets.label_verCitas).place(x=0, y=150)
        
        
        en_color=Entry(productos,
                            **StyleWidgets.entrada_verCitas,
                            textvariable=invColor)
        en_color.place(x=150, y=150,height=30)
#*****
        
        invCantidad=IntVar()
        Label(productos,
                text="Cantidad: ",
                **StyleWidgets.label_verCitas).place(x=0, y=200)

        en_cantidad=Entry(productos,
                        **StyleWidgets.entrada_verCitas,
                        textvariable=invCantidad)
        en_cantidad.place(x=150, y=200,height=30)
#********************************FIN WIDGETS PRODUCTOS************************************************





def iniciar_inventario():
    Inventario=inventario()
    Inventario.mainloop()

if __name__=="__main__":
    iniciar_inventario()
    '''fecha=str(date.today())
    print(type(fecha))'''