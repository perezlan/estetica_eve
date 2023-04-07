FONT_BTN=("Courier", 14, "italic")
FONT_BTN_verCitas=("Courier", 11, "italic")
FG_BTN="black"
RELIEF_BTN="groove"
BORDERWIDTH_BTN=1

boton={"font":FONT_BTN,
        "fg":FG_BTN,
        "relief":RELIEF_BTN}

boton_verCitas={"font":FONT_BTN_verCitas,
        "fg":FG_BTN,
        "relief":RELIEF_BTN}



BG_EN="#E3A7CB"
FONT_EN=("Courier", 14, "italic")

entrada={"bg":BG_EN,
        "width":30,
        "font":FONT_EN
        }

BG_EN_verCitas="#E3A7CB"
entrada_verCitas={"bg":BG_EN_verCitas,
        "width":30,
        "font":FONT_EN
        }
entrada_inv={"bg":"yellow",
        "width":30,
        "font":FONT_EN
        }


label={"bg":BG_EN,
        "width":10,
        "font":FONT_EN
        }


label_verCitas={"bg":BG_EN_verCitas,
        "width":10,
        "font":FONT_EN
        }
label_inv={"bg":"yellow",
        "width":10,
        "font":FONT_EN
        }


label_fecha={"bg":BG_EN,
        "width":40,
        "font":FONT_EN
        }
label_fecha1={"bg":"#FEDED9",
        "width":10,
        "font":FONT_EN
        }

#FUNCION PARA OBTENER FECHA EN ESPAÑOL
def current_date_format(date):
        months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
        day = date.day
        month = months[date.month - 1]
        year = date.year
        messsage = "fecha actual: {} de {} del {}".format(day, month, year)

        return messsage