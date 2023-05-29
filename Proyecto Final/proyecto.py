from cgitb import text
from select import select
from sqlite3 import Cursor
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image 
import pymysql


global guardar, var_buscar, id_seleccionado, dni_1
guardar = "Nuevo"
var_buscar = 0
#------------------------Ventana-de-Inicio----------------------------


def ventana_Login():
		global ventana1 
		ventana1 = Tk()
		w = 750
		h = 500
		ws = ventana1.winfo_screenwidth()
		hs = ventana1.winfo_screenheight()
		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)
		ventana1.geometry('%dx%d+%d+%d' % (w, h, x, y))
		#-----------------------------------------------------------------
		ventana1.title("Iniciar Sesion")
		ventana1.configure
		#---------------------------------------------------------
		#-----------------------------------------------------------------
		def login_admin():
			if(usuario1.get() == ""):
				entry_usuario1.focus()
				messagebox.showinfo("Faltan datos", "Ingrese Usuario")
				return
			elif(contrasena1.get()==""):
				messagebox.showinfo("Faltan datos", "Ingrese Contraseña")
				entry_constrasena1.focus()
				return
			
			basedatos = pymysql.connect(host= "localhost", user="root", passwd="", db="admi")
			fcursor = basedatos.cursor()

			fcursor.execute("SELECT Usuario FROM admi WHERE Usuario='" + usuario1.get() + "' and Contrasena='" + contrasena1.get() + "'")

			if fcursor.fetchall():
				deRegistro_a_escuela()
			else:
				messagebox.showinfo("Error", "Usuario y Contraseña Incorrecta")

			basedatos.close()
		
		#-------------------imagen------------------------------------------------------
		imagen = Image.open("imagenes/Home1.png")
		imagen_fondo = ImageTk.PhotoImage(imagen)
		imagen_redimencionada = imagen.resize((800,500))
		imagen_fondo = ImageTk.PhotoImage(imagen_redimencionada)
		
		# Establece la imagen de fondo en un label
		fondo = Label(ventana1, image=imagen_fondo)
		fondo.pack()
		
		
		
	
		#------------------------------------------------------------
		lista_megas=["Español","Ingles"]
		cmbx_megas= ttk.Combobox(ventana1, values= lista_megas)
		cmbx_megas.set("Idiomas")
		cmbx_megas.pack()
		cmbx_megas.place(x=590, y=20)
		
		#----------------------------------------------------------------
		Label(ventana1, text="Usuario     ", bg="#2A6BBF", font= "calibri", fg="white" ).place(x=470, y=200)
		Label(ventana1, text="Contraseña", bg="#2A6BBF", font= "calibri", fg="white").place(x=470, y=250)

		usuario1 = StringVar()
		contrasena1 = StringVar()

		entry_usuario1 = Entry(ventana1, textvariable=usuario1)
		entry_usuario1.pack()
		entry_usuario1.place(x=560,y=200)

		entry_constrasena1 = Entry(ventana1, textvariable=contrasena1, show="*")
		entry_constrasena1.pack()
		entry_constrasena1.place(x=560,y=250)

		Button(ventana1, text="Registrarse", width="15", bg="#2A6BBF",fg="white",command=ventana_registrar_admin).place(x=450, y=350)
		Button(ventana1, text="Entrar", width="15",  bg="#2A6BBF",fg="white",command= login_admin).place(x=585, y=350)


		mainloop()
		

#--------------------------------------------------VENTANA REGISTRO-------------------------------------------------------

def ventana_registrar_admin():
		ventana1.destroy()
		global ventana2
		ventana2 = Tk()
		ventana2.configure(background="#FFF2F4")
		w = 750
		h = 500
		ws = ventana2.winfo_screenwidth()
		hs = ventana2.winfo_screenheight()
		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)
		ventana2.geometry('%dx%d+%d+%d' % (w, h, x, y))
		#-----------------------------------------------------------------
		ventana2.title("Registrarse")

		#---------------------------------------------------------------------
		def limpiar_caja_admin():
			usuario.set("")
			mail.set("")
			contrasena1.set("")
			contrasena2.set("")

		def registrar_admin():
			if(usuario.get() == ""):
				entry_usuario.focus()
				messagebox.showinfo("Faltan datos", "Ingrese Usuario")
				return
			elif (mail.get()==""):
				messagebox.showinfo("Faltan datos", "Ingrese Mail")
				entry_mail.focus()
				return
			elif(contrasena1.get()==""):
				messagebox.showinfo("Faltan datos", "Ingrese Contraseña")
				entry_constrasena.focus()
				return
			elif (contrasena2.get()==""):
				messagebox.showinfo("Faltan datos", "Repita Contraseña")
				entry_constrasena2.focus()
				return
			elif (contrasena1.get() != contrasena2.get()):
				messagebox.showinfo("Error","La contraseña no Coinciden")
				return

			basedatos = pymysql.connect(host= "localhost", user="root", passwd="", db="admi")
			fcursor = basedatos.cursor()

			fcursor.execute("SELECT Usuario FROM admi WHERE Usuario='" + usuario.get() + "'")

			if fcursor.fetchall():
				messagebox.showinfo("Aviso", "Usuario ya Registrado")
			else:
				sql="INSERT INTO admi (Usuario, Mail, Contrasena) VALUES ('{0}','{1}','{2}')".format(usuario.get(), mail.get(), contrasena1.get())
				fcursor.execute(sql)
				basedatos.commit()
				messagebox.showinfo("Registo", "Se registro el Usuario con exito")

				limpiar_caja_admin()
			basedatos.close()
			
		#-----------------------icon-----------------------------------------------
		ventana2.resizable(0,0)
		ventana2.iconbitmap("icons/FOLDER02.ico")
		
		#-------------------imagen------------------------------------------------------
		imagen = Image.open("imagenes/imgregistro.png")
		imagen_fondo = ImageTk.PhotoImage(imagen)
		imagen_redimencionada = imagen.resize((800,500))
		imagen_fondo = ImageTk.PhotoImage(imagen_redimencionada)
		
		# Establece la imagen de fondo en un label
		fondo = Label(ventana2, image=imagen_fondo)
		fondo.pack()
		
		
		
		#-----------------------------------------------------------------
		

		Label(ventana2, text="Usuario          ", font= "calibri",bg="#2A6BBF", fg="white" ).place(x=70, y=150)
		Label(ventana2, text="Mail               ",  font= "calibri",bg="#2A6BBF", fg="white" ).place(x=70, y=195)
		Label(ventana2, text="Contraseña    ",  font= "calibri",bg="#2A6BBF", fg="white" ).place(x=70, y=235)
		Label(ventana2, text="R. Contraseña", font= "calibri",bg="#2A6BBF",  fg="white" ).place(x=70, y=275)

		usuario = StringVar()
		mail = StringVar()
		contrasena1 = StringVar()
		contrasena2 = StringVar()

		entry_usuario = Entry(ventana2, textvariable=usuario)
		entry_usuario.pack()
		entry_usuario.place(x=175,y=155)

		entry_mail = Entry(ventana2, textvariable=mail)
		entry_mail.pack()
		entry_mail.place(x=175,y=200)

		entry_constrasena = Entry(ventana2, textvariable=contrasena1, show="*")
		entry_constrasena.pack()
		entry_constrasena.place(x=175,y=240)

		entry_constrasena2 = Entry(ventana2, textvariable=contrasena2, show="*")
		entry_constrasena2.pack()
		entry_constrasena2.place(x=175,y=280)

		Button(ventana2, text="Guardar", width="10", command=registrar_admin ,bg="#90EE90",fg="white").place(x=60,y=370)
		Button(ventana2, text="Salir", width="10", command= deVentanaRegistrarAdmin_a_VentanaInicio,bg="#FF2C00",fg="white").place(x=155,y=370)
		Button(ventana2, text="Cancelar", width="10", command=limpiar_caja_admin,bg="#0053FF", fg="white").place(x=255, y=370)
		#-----------------------------------------------------------------

		mainloop()
#-------------------------------------------------------VENTANA MENU PRINCIPAL-------------------------------------
def ventana_menu():
		global ventana4 
		ventana4 = Tk()
		#---------------------Centrar-Ventana-----------------------------
		w = 655
		h = 300
		ws = ventana4.winfo_screenwidth()
		hs = ventana4.winfo_screenheight()
		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)
		ventana4.geometry('%dx%d+%d+%d' % (w, h, x, y))
		#----------------------ICON-------------------------------------------
		ventana4.title("Menu Principal")
		ventana4.configure(bg="#000675")
		ventana4.resizable(0,0)
		ventana4.iconbitmap("icons/EXPLORER.ico")
		
		
	#---------------------------------------------------------

		mainloop()


def salir_de_login():
	ventana1.destroy()
	ventana_Login()

def deVentanaRegistrarAdmin_a_VentanaInicio():
	ventana2.destroy()
	ventana_Login()

def deInicio_Login ():
	ventana1.destroy()
	ventana_Login()

def salir_de_login():
	ventana1.destroy()
	ventana_Login()

def deRegistro_a_escuela():
	ventana1.destroy()
	ventana_menu()

def salir_de_estudiantes():
	ventana4.destroy()
	ventana_Login()

def salir_de_escuela():
	ventana5.destroy()
	ventana_menu()

ventana_Login ()

