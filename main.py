import tkinter as tk
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
import numpy as np
import networkx as nx
from dpto import *
from validacioness import *
from insertar import arbol
from representacion import *
import graphviz as gv
import webbrowser
from mapa import *
from tkinter import ttk
from tkintermapview import TkinterMapView

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.arbol_avl = arbol
        self.title("Residencial Arboreal")
        self.x = self.winfo_screenwidth() // 2 - 1540 // 2
        self.y = self.winfo_screenheight() // 2 - 800 // 2
        self.posicionamiento = f"1540x800+{self.x - 10}+{self.y -35}"
        
        self.geometry(self.posicionamiento)
        self.resizable(False, False)
        
        
        self.dptos = COLOMBIA.departamentos
        
        #Se coloca el grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)
        
        #Se cargan las imágenes
        self.img_avl = ctk.CTkImage(Image.open("graphics/arbol.png"), size=(128, 128))
        #Se crean las fuentes
        self.fontTitles = ctk.CTkFont(family="<family name>", size=16)
        self.fontMid = ctk.CTkFont(family="<family name>", size=14)
        self.fontNormal = ctk.CTkFont(family="<family name>", size=12)
        
        #Base nodos
        self.base_nodos = []
        
        #Se crean los frames
        
        #Menú lateral
        self.menu_frame = ctk.CTkFrame(self, corner_radius=0, bg_color="#1B263B", width=200, height=800, fg_color="transparent")
        self.menu_frame.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self.menu_frame.grid_rowconfigure(10, weight=1)
        self.menu_frame.grid_columnconfigure(2, weight=1)
        
        
        #Botones Menú
        self.home_button_icon = ctk.CTkLabel(self.menu_frame, image=self.img_avl, bg_color="#1B263B", fg_color="transparent", corner_radius=0, width=200, height=128, text="")
        self.home_button_icon.grid(row=0, column=0, sticky="nsew", padx=0, pady=20, columnspan=3)
        self.home_button = ctk.CTkButton(self.menu_frame, text="Inserción", fg_color="transparent", bg_color="#1B263B",width=200, height = 74, corner_radius=0, command=lambda: self.select_frame_by_name("home"))
        self.home_button.grid(row=1, column=0, sticky="nsew", padx=0, pady=0, columnspan=3)
        self.eliminar_button = ctk.CTkButton(self.menu_frame, text="Eliminación", fg_color="transparent", bg_color="#1B263B",width=200, height = 74, corner_radius=0, command=lambda: self.select_frame_by_name("frame_2"))
        self.eliminar_button.grid(row=2, column=0, sticky="nsew", padx=0, pady=0, columnspan=3)
        self.busqueda_button = ctk.CTkButton(self.menu_frame, text="Búsqueda", fg_color="transparent", bg_color="#1B263B",width=200, height = 74, corner_radius=0, command=lambda: self.select_frame_by_name("frame_3"))
        self.busqueda_button.grid(row=3, column=0, sticky="nsew", padx=0, pady=0, columnspan=3)
        self.recorrido_button = ctk.CTkButton(self.menu_frame, text="Recorrido", fg_color="transparent", bg_color="#1B263B",width=200, height = 74, corner_radius=0, command=lambda: self.select_frame_by_name("frame_4"))
        self.recorrido_button.grid(row=4, column=0, sticky="nsew", padx=0, pady=0, columnspan=3)
        self.mapa_button = ctk.CTkButton(self.menu_frame, text="Geolocalización", fg_color="transparent", bg_color="#1B263B",width=200, height = 74, corner_radius=0, command=lambda: self.select_frame_by_name("frame_5"))
        self.mapa_button.grid(row=5, column=0, sticky="nsew", padx=0, pady=0, columnspan=3)
        
        #rame Principal Home
        self.home_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent", bg_color="#0D1B2A")
        self.home_frame.grid(row=0, column=1, sticky="nsew")
        self.home_frame.grid_rowconfigure(1, weight=1)
        self.home_frame.grid_columnconfigure(0, weight=1)   
        
        #Sub Frames Home 
        
        #navbar (row 0)
        self.navbar = ctk.CTkFrame(self.home_frame, corner_radius=0, fg_color="transparent", bg_color="#19293B", width=1340, height=73)
        self.navbar.grid(row=0, column=0, sticky="nsew", padx=0, pady=0, columnspan=1)
        self.navbar.grid_rowconfigure(0, weight=1)
        self.navbar.grid_columnconfigure(5, weight=1)
        
        self.label_titulo = ctk.CTkLabel(self.navbar, text="Residential Arboreal/Inserción", font=self.fontMid, bg_color="#19293B", text_color="#E0E1DD", corner_radius=0, height=73 )
        self.label_titulo.grid(row=0, column=0, sticky="nsew", padx=0, pady=0, columnspan=1, ipadx=30)
        self.fontMid.configure(family="Georgia")
        
        
        #home_content (row 1)
        self.home_content = ctk.CTkFrame(self.home_frame, corner_radius=0, fg_color="transparent", bg_color="#0D1B2A", height=727, width=1338)
        self.home_content.grid(row=1, column=0, sticky="nsew")
        self.home_content.columnconfigure(2, weight=1)
        self.home_content.rowconfigure(0, weight=1)
        
        #Tree frame
        self.tree_frame = ctk.CTkFrame(self.home_content, fg_color="transparent", bg_color="#0D1B2A", width=892, height=727, )
        self.tree_frame.grid(row=0, column=0, columnspan=2, rowspan= 1, pady=0, padx=0, sticky="nsew")
        self.tree_frame.grid_rowconfigure(10, weight=1)
        self.tree_frame.grid_columnconfigure(0, weight=1)
        
        #Button frame
        self.button_frame = ctk.CTkFrame(self.home_content, corner_radius=0, fg_color="transparent", bg_color="#0D1B2A", height=727, width=446)
        self.button_frame.grid(row=0, column=2, sticky="nsew")
        self.button_frame.grid_rowconfigure(9, weight=1)
        self.button_frame.grid_columnconfigure(2, weight=1)
        
        #Título Árbol e insertar
        self.label_arbol = ctk.CTkButton(self.tree_frame, text= "Árbol AVL", bg_color="#0D1B2A", fg_color= "#0466C8", corner_radius=10, width= 667, height=39, text_color="#E0E1DD", font=self.fontNormal, hover_color="#0466C8")
        self.label_arbol.grid(row=0, column=0, padx=110 , ipadx= 0, pady=14, columnspan=1, ipady=0, sticky="nsew")
        self.label_titulo_ins = ctk.CTkButton(self.button_frame, text= "Insertar Nodo", bg_color="#0D1B2A", fg_color= "#0466C8", corner_radius=10, width= 410, height=39, text_color="#E0E1DD", font=self.fontNormal, hover_color="#0466C8")
        self.label_titulo_ins.grid(row=0, column=0, padx=15, pady=14, columnspan=3, ipady=0, sticky="nsew", ipadx=0)
        
        #Frame 2
        self.frame2 = ctk.CTkFrame(self, corner_radius=0, fg_color="#0D1B2A", bg_color="#0D1B2A")
        self.frame2.grid_rowconfigure(1, weight=1)
        self.frame2.grid_columnconfigure(0, weight=1)
        
        self.frame_2_button = ctk.CTkButton(self.menu_frame, text="Frame 2", fg_color="transparent", bg_color="transparent", corner_radius=0, command=lambda: self.select_frame_by_name("frame_2"))
        self.frame_2_navbar = ctk.CTkFrame(self.frame2, corner_radius=0, fg_color="transparent", bg_color="#0D1B2A", width=1340, height=73)
        self.frame_2_content = ctk.CTkFrame(self.frame2, corner_radius=0, fg_color="transparent", bg_color="transparent")
        self.frame_2_tree = ctk.CTkFrame(self.frame_2_content, corner_radius=0, fg_color="transparent", bg_color="transparent")
        self.frame_2_input = ctk.CTkFrame(self.frame_2_content, corner_radius=0, fg_color="transparent", bg_color="transparent")
        
        self.frame_2_content.grid_rowconfigure(0, weight=1)
        self.frame_2_content.grid_columnconfigure(1, weight=1)
        self.frame_2_content.grid(row=1, column=0, sticky="nsew")
        self.frame_2_navbar.grid(row=0, column=0, sticky="nsew")
        self.frame_2_tree.grid(row=0, column=0, sticky="nsew")
        self.frame_2_input.grid(row=0, column=1, sticky="nsew")
        
        self.frame_2_navbar.grid_rowconfigure(0, weight=1)
        self.frame_2_navbar.grid_columnconfigure(5, weight=1)
        self.frame_2_tree.grid_rowconfigure(9, weight=1)
        self.frame_2_tree.grid_columnconfigure(0, weight=1)
        self.frame_2_input.grid_rowconfigure(9, weight=1)
        self.frame_2_input.grid_columnconfigure(2, weight=1)
        
        #Frame 3: 
        self.frame3 = ctk.CTkFrame(self, corner_radius=0, fg_color="#0D1B2A", bg_color="#0D1B2A")
        self.frame3.grid_rowconfigure(1, weight=1)
        self.frame3.grid_columnconfigure(0, weight=1)
        self.frame3_nav = ctk.CTkFrame(self.frame3, corner_radius=0, fg_color="transparent", bg_color="#0D1B2A", width=1340, height=73)
        self.frame3_nav.grid(row=0, column=0, sticky="nsew")
        self.frame3_content = ctk.CTkFrame(self.frame3, corner_radius=0, fg_color="transparent", bg_color="transparent")
        self.frame3_content.grid(row=1, column=0, sticky="nsew")
        self.frame3_bsimple = ctk.CTkFrame(self.frame3_content, corner_radius=0, fg_color="transparent", bg_color="transparent", width=442, height=727)
        self.frame3_bsimple.grid(row=0, column=0, sticky="nsew")
        self.frame3_bavanzado = ctk.CTkFrame(self.frame3_content, corner_radius=0, fg_color="transparent", bg_color="transparent")
        self.frame3_bavanzado.grid(row=0, column=1, sticky="nsew")
        
        self.frame3_nav.grid_rowconfigure(0, weight=1)
        self.frame3_nav.grid_columnconfigure(5, weight=1)
        self.frame3_content.grid_rowconfigure(0, weight=1)
        self.frame3_content.grid_columnconfigure(1, weight=1)
        self.frame3_bsimple.grid_rowconfigure(9, weight=1)
        self.frame3_bsimple.grid_columnconfigure(2, weight=1)
        self.frame3_bavanzado.grid_rowconfigure(9, weight=1)
        self.frame3_bavanzado.grid_columnconfigure(5, weight=1)
        
        # Frame 4
        
        self.frame4 = ctk.CTkFrame(self, corner_radius=0, fg_color="#0D1B2A", bg_color="#0D1B2A")
        self.frame4.grid_rowconfigure(1, weight=1)
        self.frame4.grid_columnconfigure(0, weight=1)
        self.frame4_nav = ctk.CTkFrame(self.frame4, corner_radius=0, fg_color="transparent", bg_color="#0D1B2A", width=1340, height=73)
        self.frame4_nav.grid(row=0, column=0, sticky="nsew")
        self.frame4_nav.grid_rowconfigure(0, weight=1)
        self.frame4_nav.grid_columnconfigure(5, weight=1)
        self.frame4_content = ctk.CTkFrame(self.frame4, corner_radius=0, fg_color="transparent", bg_color="transparent")
        self.frame4_content.grid(row=1, column=0, sticky="nsew")
        self.frame4_content.grid_rowconfigure(0, weight=1)
        self.frame4_content.grid_columnconfigure(1, weight=1)
        self.frame4_tree = ctk.CTkFrame(self.frame4_content, corner_radius=0, fg_color="transparent", bg_color="transparent", width=892, height=727)
        self.frame4_tree.grid(row=0, column=0, sticky="nsew")
        self.frame4_tree.grid_rowconfigure(9, weight=1)
        self.frame4_tree.grid_columnconfigure(0, weight=1)
        self.frame4_input = ctk.CTkFrame(self.frame4_content, corner_radius=0, fg_color="transparent", bg_color="transparent", width=446, height=727)
        self.frame4_input.grid(row=0, column=1, sticky="nsew")
        self.frame4_input.grid_rowconfigure(9, weight=1)
        self.frame4_input.grid_columnconfigure(2, weight=1)
        
        #Frame 5
        self.frame5 = ctk.CTkFrame(self, corner_radius=0, fg_color="#0D1B2A", bg_color="#0D1B2A")
        self.frame5.grid_rowconfigure(1, weight=1)
        self.frame5.grid_columnconfigure(0, weight=1)
        self.frame5_nav = ctk.CTkFrame(self.frame5, corner_radius=0, fg_color="transparent", bg_color="#0D1B2A", width=1340, height=73)
        self.frame5_nav.grid(row=0, column=0, sticky="nsew")
        self.frame5_nav.grid_rowconfigure(0, weight=1)
        self.frame5_nav.grid_columnconfigure(5, weight=1)
        self.frame5_content = ctk.CTkFrame(self.frame5, corner_radius=0, fg_color="transparent", bg_color="transparent")
        self.frame5_content.grid(row=1, column=0, sticky="nsew")
        self.frame5_content.grid_rowconfigure(0, weight=1)
        self.frame5_content.grid_columnconfigure(1, weight=1)
        self.frame5_map = ctk.CTkFrame(self.frame5_content, corner_radius=0, fg_color="transparent", bg_color="transparent", width=892, height=727)
        self.frame5_map.grid(row=0, column=0, sticky="nsew")
        self.frame5_map.grid_rowconfigure(9, weight=1)
        self.frame5_map.grid_columnconfigure(0, weight=1)
        self.frame5_input = ctk.CTkFrame(self.frame5_content, corner_radius=0, fg_color="transparent", bg_color="transparent", width=446, height=727)
        self.frame5_input.grid(row=0, column=1, sticky="nsew")
        self.frame5_input.grid_rowconfigure(9, weight=1)
        self.frame5_input.grid_columnconfigure(2, weight=1)
        self.canvas = tk.Canvas(self.tree_frame, width=892, height=727)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        plot_avl_tree(self.arbol_avl.raiz)
        self.image = Image.open("avl_tree.png")
        self.image_tk = ImageTk.PhotoImage(self.image) 
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_tk)
        
        self.canvas2 = tk.Canvas(self.frame_2_tree, width=892, height=727)
        self.canvas2.grid(row=1, column=0, sticky="nsew")
        plot_avl_tree(self.arbol_avl.raiz)
        self.canvas2.create_image(0, 0, anchor=tk.NW, image=self.image_tk)
        
        self.canvas3 = tk.Canvas(self.frame4_tree, width=892, height=727)
        self.canvas3.grid(row=1, column=0, sticky="nsew")
        plot_avl_tree(self.arbol_avl.raiz)
        self.canvas3.create_image(0, 0, anchor=tk.NW, image=self.image_tk)
        
        #Se crean los inputs de inserción
        
        #Labels
        
        #Frame 1
        self.label_anuncio = ctk.CTkLabel(self.button_frame, text="Título Anuncio", font=self.fontNormal, bg_color="#0D1B2A", text_color="#E0E1DD", corner_radius=0)
        self.label_anuncio.grid(row=1, column=0, padx=30,  columnspan= 1, pady=10 , ipady=0)
        self.label_latitud = ctk.CTkLabel(self.button_frame, text="Latitud", font=self.fontNormal, bg_color="#0D1B2A", text_color="#E0E1DD", corner_radius=0)
        self.label_latitud.grid(row=3, column=0, padx=30,  columnspan= 1, pady=10 , ipady=0)
        self.label_longitud = ctk.CTkLabel(self.button_frame, text="Longitud", font=self.fontNormal, bg_color="#0D1B2A", text_color="#E0E1DD", corner_radius=0)
        self.label_longitud.grid(row=4, column=0, padx=30,  columnspan= 1, pady=10 , ipady=0)
        self.label_st = ctk.CTkLabel(self.button_frame, text="Superficie Total", font=self.fontNormal, bg_color="#0D1B2A", text_color="#E0E1DD", corner_radius=0)
        self.label_st.grid(row=5, column=0, padx=30,  columnspan= 1, pady=10 , ipady=0)
        self.label_sc = ctk.CTkLabel(self.button_frame, text="Superficie Construida", font=self.fontNormal, bg_color="#0D1B2A", text_color="#E0E1DD", corner_radius=0)
        self.label_sc.grid(row=6, column=0, padx=30,  columnspan= 1, pady=10 , ipady=0)
        self.label_precio = ctk.CTkLabel(self.button_frame, text="Precio", font=self.fontNormal, bg_color="#0D1B2A", text_color="#E0E1DD", corner_radius=0)
        self.label_precio.grid(row=8, column=0, padx=30,  columnspan= 1, pady=10 , ipady=0)
        self.label_message1 = ctk.CTkLabel(self.tree_frame, text="", font=self.fontNormal, bg_color="#0D1B2A", text_color="#E0E1DD", corner_radius=0)
        self.label_message1.grid(row=10, column=0, padx=0,  columnspan= 1, pady=0 , ipady=0)
        
        self.fontNormal.configure(family="Georgia")
        
        #Frame 2
        self.label_nav2 = ctk.CTkLabel(self.frame_2_navbar, text= "Residential Arboreal/Eliminación", font=self.fontMid, bg_color="#19293B", text_color="#E0E1DD", fg_color= "#19293B", corner_radius=0, height=73)
        self.label_nav2.grid(row=0, column=0, sticky="nsew", padx=0, pady=0, columnspan=1, ipadx=30)
        self.label_nav2r = ctk.CTkLabel(self.frame_2_navbar, text= "", font=self.fontMid, bg_color="#19293B", text_color="#E0E1DD", fg_color= "#19293B", corner_radius=0, height=73)
        self.label_nav2r.grid(row=0, column=1, sticky="nsew", padx=0, pady=0, columnspan=5,  ipadx=30)
        self.label_arbol = ctk.CTkButton(self.frame_2_tree, text= "Árbol AVL", bg_color="#0D1B2A", fg_color= "#0466C8", corner_radius=10, width= 667, height=39, text_color="#E0E1DD", font=self.fontNormal, hover_color="#0466C8")
        self.label_arbol.grid(row=0, column=0, padx=110 , ipadx= 0, pady=14, columnspan=1, ipady=0, sticky="nsew")
        self.label_titulo_ins = ctk.CTkButton(self.frame_2_input, text= "Eliminar Nodo", bg_color="#0D1B2A", fg_color= "#0466C8", corner_radius=10, width= 410, height=39, text_color="#E0E1DD", font=self.fontNormal, hover_color="#0466C8")
        self.label_titulo_ins.grid(row=0, column=0, padx=15, pady=14, columnspan=3, ipady=0, sticky="nsew", ipadx=0)
        self.label_metrica = ctk.CTkLabel(self.frame_2_input, text="Métrica", font=self.fontNormal, bg_color="#0D1B2A", text_color="#E0E1DD", corner_radius=0)
        self.label_metrica.grid(row=1, column=0, padx=30,  columnspan= 1, pady=20 , ipady=0)
        self.fontMid.configure(family="Georgia")
        
        #Frame 3
        self.label_nav3 = ctk.CTkLabel(self.frame3_nav, text= "Residential Arboreal/Búsqueda", font=self.fontMid, bg_color="#19293B", text_color="#E0E1DD", fg_color= "#19293B", corner_radius=0, height=73)
        self.label_nav3.grid(row=0, column=0, sticky="nsew", padx=0, pady=0, columnspan=1, ipadx=30)
        self.label_nav3r = ctk.CTkLabel(self.frame3_nav, text= "", font=self.fontMid, bg_color="#19293B", text_color="#E0E1DD", fg_color= "#19293B", corner_radius=0, height=73)
        self.label_nav3r.grid(row=0, column=1, sticky="nsew", padx=0, pady=0, columnspan=5,  ipadx=30)
        self.label_busqueda = ctk.CTkButton(self.frame3_bsimple, text= "Búsqueda por métrica", bg_color="#0D1B2A", fg_color= "#0466C8", corner_radius=10, width= 410, height=39, text_color="#E0E1DD", font=self.fontNormal, hover_color="#0466C8")
        self.label_busqueda.grid(row=0, column=0, padx=10 , ipadx= 0, pady=14, columnspan=3, ipady=0, sticky="nsew")
        self.label_busqueda_avanzada = ctk.CTkButton(self.frame3_bavanzado, text= "Búsqueda Avanzada", bg_color="#0D1B2A", fg_color= "#0466C8", corner_radius=10, width= 667, height=39, text_color="#E0E1DD", font=self.fontNormal, hover_color="#0466C8")
        self.label_busqueda_avanzada.grid(row=0, column=0, padx=30 , ipadx= 0, pady=14, columnspan=6, ipady=0, sticky="nsew")
        self.label_met = ctk.CTkLabel(self.frame3_bsimple, text="Métrica", font=self.fontNormal, bg_color="#0D1B2A", text_color="#E0E1DD", corner_radius=0)
        self.label_met.grid(row=1, column=0, padx=80,  columnspan= 1, pady=20 , ipady=0)
        self.label_adic = ctk.CTkButton(self.frame3_bsimple, text= "Adicional", bg_color="#0D1B2A", fg_color= "#243A53", corner_radius=10, width= 200, height=39, text_color="#E0E1DD", font=self.fontNormal, hover_color="#243A53")
        self.label_adic.grid(row=2, column=0, padx=80 , ipadx= 0, pady=14, columnspan=3, ipady=0, sticky="nsew")
        self.label_busc = ctk.CTkLabel(self.frame3_bsimple, text="Buscar su", font=self.fontNormal, bg_color="#0D1B2A", text_color="#E0E1DD", corner_radius=0)
        self.label_busc.grid(row=3, column=0, padx=40,  columnspan= 1, pady=20 , ipady=0)
        self.label_par = ctk.CTkLabel(self.frame3_bavanzado, text="Parámetros", font=self.fontNormal, bg_color="#0D1B2A", text_color="#E0E1DD", corner_radius=0)
        self.label_par.grid(row=1, column=1, padx=70,  columnspan= 1, pady=20 , ipady=0 , sticky="nsew")
        self.label_oper = ctk.CTkLabel(self.frame3_bavanzado, text="Operadores", font=self.fontNormal, bg_color="#0D1B2A", text_color="#E0E1DD", corner_radius=0)
        self.label_oper.grid(row=2, column=1, padx=70,  columnspan= 1, pady=20 , ipady=0, sticky="nsew")
        self.label_p1 = ctk.CTkLabel(self.frame3_bavanzado, text="Parámetro 1", font=self.fontNormal, bg_color="#0D1B2A", text_color="#E0E1DD", corner_radius=0)
        self.label_p1.grid(row=3, column=1, padx=40,  columnspan= 1, pady=20 , ipady=0, sticky="nsew")
        self.label_p2 = ctk.CTkLabel(self.frame3_bavanzado, text="Parámetro 2", font=self.fontNormal, bg_color="#0D1B2A", text_color="#E0E1DD", corner_radius=0)
        self.label_p2.grid(row=4, column=1, padx=40,  columnspan= 1, pady=20 , ipady=0, sticky="nsew")
        self.label_p3 = ctk.CTkLabel(self.frame3_bavanzado, text="Parámetro 3", font=self.fontNormal, bg_color="#0D1B2A", text_color="#E0E1DD", corner_radius=0)
        self.label_p3.grid(row=5, column=1, padx=40,  columnspan= 1, pady=20 , ipady=0, sticky="nsew")
        self.label_buscs = ctk.CTkLabel(self.frame3_bavanzado, text="Buscar su", font=self.fontNormal, bg_color="#0D1B2A", text_color="#E0E1DD", corner_radius=0)
        self.label_buscs.grid(row=4, column=3, padx=20,  columnspan= 1, pady=20 , ipady=0, sticky="nsew")
        self.label_adi = ctk.CTkButton(self.frame3_bavanzado, text= "Adicional", bg_color="#0D1B2A", fg_color= "#243A53", corner_radius=10, width= 200, height=39, text_color="#E0E1DD", font=self.fontNormal, hover_color="#243A53")
        self.label_adi.grid(row=3, column=3, padx=20 , ipadx= 0, pady=20, columnspan=2, ipady=0, sticky="nsew")
        
        #Frame 4
        self.label_nav4 = ctk.CTkLabel(self.frame4_nav, text= "Residential Arboreal/Recorrido", font=self.fontMid, bg_color="#19293B", text_color="#E0E1DD", fg_color= "#19293B", corner_radius=0, height=73)
        self.label_nav4.grid(row=0, column=0, sticky="nsew", padx=0, pady=0, columnspan=1, ipadx=30)
        self.label_nav4r = ctk.CTkLabel(self.frame4_nav, text= "", font=self.fontMid, bg_color="#19293B", text_color="#E0E1DD", fg_color= "#19293B", corner_radius=0, height=73)
        self.label_nav4r.grid(row=0, column=1, sticky="nsew", padx=0, pady=0, columnspan=5,  ipadx=30)
        self.label_arbol4 = ctk.CTkButton(self.frame4_tree, text= "Árbol AVL", bg_color="#0D1B2A", fg_color= "#0466C8", corner_radius=10, width= 667, height=39, text_color="#E0E1DD", font=self.fontNormal, hover_color="#0466C8")
        self.label_arbol4.grid(row=0, column=0, padx=110 , ipadx= 0, pady=14, columnspan=1, ipady=0, sticky="nsew")
        self.label_inp4 = ctk.CTkButton(self.frame4_input, text= "Recorrido", bg_color="#0D1B2A", fg_color= "#0466C8", corner_radius=10, width= 410, height=39, text_color="#E0E1DD", font=self.fontNormal, hover_color="#0466C8")
        self.label_inp4.grid(row=0, column=0, padx=15, pady=14, columnspan=3, ipady=0, sticky="nsew", ipadx=0)
        
        #Frame 5
        
        self.label_nav5 = ctk.CTkLabel(self.frame5_nav, text= "Residential Arboreal/Mapa", font=self.fontMid, bg_color="#19293B", text_color="#E0E1DD", fg_color= "#19293B", corner_radius=0, height=73)
        self.label_nav5.grid(row=0, column=0, sticky="nsew", padx=0, pady=0, columnspan=1, ipadx=30)
        self.label_nav5r = ctk.CTkLabel(self.frame5_nav, text= "", font=self.fontMid, bg_color="#19293B", text_color="#E0E1DD", fg_color= "#19293B", corner_radius=0, height=73)
        self.label_nav5r.grid(row=0, column=1, sticky="nsew", padx=0, pady=0, columnspan=5,  ipadx=30)
        self.label_arbol5 = ctk.CTkButton(self.frame5_map, text= "Mapa Colombia", bg_color="#0D1B2A", fg_color= "#0466C8", corner_radius=10, width= 667, height=39, text_color="#E0E1DD", font=self.fontNormal, hover_color="#0466C8")
        self.label_arbol5.grid(row=0, column=0, padx=110 , ipadx= 0, pady=14, columnspan=1, ipady=0, sticky="nsew")
        self.label_inp5 = ctk.CTkButton(self.frame5_input, text= "Generar Mapa", bg_color="#0D1B2A", fg_color= "#0466C8", corner_radius=10, width= 410, height=39, text_color="#E0E1DD", font=self.fontNormal, hover_color="#0466C8")
        self.label_inp5.grid(row=0, column=0, padx=15, pady=14, columnspan=3, ipady=0, sticky="nsew", ipadx=0)
        self.label_t1 = ctk.CTkLabel(self.frame5_input, text="Sus nodos buscados fueron guardados. Para visualizarlos en el mapa", font=self.fontNormal, bg_color="#0D1B2A", text_color="#E0E1DD", corner_radius=0)
        self.label_t1.grid(row=1, column=0, padx=0,  columnspan= 3, pady=20 , ipady=0, sticky="nsew")
        self.label_t2 = ctk.CTkLabel(self.frame5_input, text="presione el botón 'Geolocalizar'", font=self.fontNormal, bg_color="#0D1B2A", text_color="#E0E1DD", corner_radius=0)
        self.label_t2.grid(row=2, column=0, padx=45,  columnspan= 1, pady=20 , ipady=0, sticky="nsew")
        
        self.fontMid.configure(family="Georgia")
        
        #Entries
        
        #Frame 1
        self.text_anuncio = ctk.CTkTextbox(self.button_frame, bg_color="#0D1B2A", corner_radius=10, width= 253, height=28,  fg_color="#19293B")
        self.text_anuncio.grid(row=1, column=1, padx=25, columnspan= 2, pady=10 , ipady=0)
        self.text_latitud = ctk.CTkTextbox(self.button_frame, bg_color="#0D1B2A", corner_radius=10, width= 253, height=28,  fg_color="#19293B")
        self.text_latitud.grid(row=3, column=1, padx=25, columnspan= 2, pady=20 , ipady=0)
        self.text_longitud = ctk.CTkTextbox(self.button_frame, bg_color="#0D1B2A", corner_radius=10, width= 253, height=28,  fg_color="#19293B")
        self.text_longitud.grid(row=4, column=1, padx=25, columnspan= 2, pady=10 , ipady=0)
        self.text_st = ctk.CTkTextbox(self.button_frame, bg_color="#0D1B2A", corner_radius=10, width= 253, height=28,  fg_color="#19293B")
        self.text_st.grid(row=5, column=1, padx=25, columnspan= 2, pady=10 , ipady=0)
        self.text_sc = ctk.CTkTextbox(self.button_frame, bg_color="#0D1B2A", corner_radius=10, width= 253, height=28,  fg_color="#19293B")
        self.text_sc.grid(row=6, column=1, padx=25, columnspan= 2, pady=10 , ipady=0)
        self.text_precio = ctk.CTkTextbox(self.button_frame, bg_color="#0D1B2A", corner_radius=10, width= 253, height=28,  fg_color="#19293B")
        self.text_precio.grid(row=8, column=1, padx=25, columnspan= 2, pady=10 , ipady=0)
        
        #Frame 2
        self.text_metrica = ctk.CTkTextbox(self.frame_2_input, bg_color="#0D1B2A", corner_radius=10, width= 253, height=28,  fg_color="#19293B")
        self.text_metrica.grid(row=1, column=1, padx=25, columnspan= 2, pady=20 , ipady=0, ipadx=10)
        
        #Frame 3
        self.text_met = ctk.CTkTextbox(self.frame3_bsimple, bg_color="#0D1B2A", corner_radius=10, width= 200, height=28,  fg_color="#19293B")
        self.text_met.grid(row=1, column=1, padx=0, columnspan= 2, pady=20 , ipady=0, ipadx=0)
        self.text_ara= ctk.CTkTextbox(self.frame3_bsimple, bg_color="#0D1B2A", corner_radius=10, width= 348, height=245,  fg_color="#19293B")
        self.text_ara.grid(row=5, column=0, padx=0, columnspan= 3, pady=20 , ipady=0, ipadx=0)
        self.text_p1 = ctk.CTkTextbox(self.frame3_bavanzado, bg_color="#0D1B2A", corner_radius=10, width= 200, height=28,  fg_color="#19293B")
        self.text_p1.grid(row=3, column=2, padx=0, columnspan= 1, pady=20 , ipady=0, ipadx=0)
        self.text_p2 = ctk.CTkTextbox(self.frame3_bavanzado, bg_color="#0D1B2A", corner_radius=10, width= 200, height=28,  fg_color="#19293B")
        self.text_p2.grid(row=4, column=2, padx=0, columnspan= 1, pady=20 , ipady=0, ipadx=0)
        self.text_p3 = ctk.CTkTextbox(self.frame3_bavanzado, bg_color="#0D1B2A", corner_radius=10, width= 200, height=28,  fg_color="#19293B")
        self.text_p3.grid(row=5, column=2, padx=0, columnspan= 1, pady=20 , ipady=0, ipadx=0)
        
        #Combo Boxes
        self.combo_dpto = ctk.CTkComboBox(self.button_frame, bg_color="#0D1B2A", corner_radius=10, width= 110, height=28,  fg_color="#19293B", state= "readonly", values = [dpto.nombre for dpto in self.dptos], command= self.change_combo_ciudad)
        self.combo_dpto.set("Departamento")
        self.combo_dpto.grid(row=2, column=0, padx=15, columnspan= 1, pady=25 , ipady=0, ipadx=10)
        self.combo_ciudad = ctk.CTkComboBox(self.button_frame, bg_color="#0D1B2A", corner_radius=10, width=110, height=28, fg_color="#19293B", state="readonly", values= [])
        self.combo_ciudad.set("Ciudad      ")
        self.combo_ciudad.grid(row=2, column=1, padx=15, columnspan=1, pady=25, ipady=0, ipadx=0)
        self.combo_tipo = ctk.CTkComboBox(self.button_frame, bg_color="#0D1B2A", corner_radius=10, width=110, height=28, fg_color="#19293B", state="readonly", values=["Tipo", "Casa", "Apartamento"])
        self.combo_tipo.set("Tipo          ")
        self.combo_tipo.grid(row=2, column=2, padx=15, columnspan=1, pady=25, ipady=0, ipadx=15)
        self.combo_cuartos = ctk.CTkComboBox(self.button_frame, bg_color="#0D1B2A", corner_radius=10, width=110, height=28, fg_color="#19293B", state="readonly", values=["Cuartos", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
        self.combo_cuartos.set("Cuartos    ")
        self.combo_cuartos.grid(row=7, column=0, padx=15, columnspan=1, pady=25, ipady=0, ipadx=10)
        self.combo_banos = ctk.CTkComboBox(self.button_frame, bg_color="#0D1B2A", corner_radius=10, width=110, height=28, fg_color="#19293B", state="readonly", values=["Baños", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
        self.combo_banos.set("Baños        ")
        self.combo_banos.grid(row=7, column=1, padx=15, columnspan=1, pady=25, ipady=0, ipadx=0)
        self.combo_operacion = ctk.CTkComboBox(self.button_frame, bg_color="#0D1B2A", corner_radius=10, width=110, height=28, fg_color="#19293B", state="readonly", values=["Operación", "Compra", "Arriendo"])
        self.combo_operacion.set("Operación    ")
        self.combo_operacion.grid(row=7, column=2, padx=15, columnspan=1, pady=25, ipady=0, ipadx=15)
        
        #Frame 3
        self.combo_ad = ctk.CTkComboBox(self.frame3_bsimple, bg_color="#0D1B2A", corner_radius=10, width= 200, height=28,  fg_color="#19293B", state= "readonly", values = ["Ninguno", "Nivel", "Factor de balanceo", "Padre", "Abuelo", "Tío"] )
        self.combo_ad.set(self.combo_ad._values[0])
        self.combo_ad.grid(row=3, column=1, padx=0, columnspan= 2, pady=20 , ipady=0, ipadx=0)
        self.combo_p1 = ctk.CTkComboBox(self.frame3_bavanzado, bg_color="#0D1B2A", corner_radius=10, width= 100, height=28,  fg_color="#19293B", state= "readonly", values =["Título", "Departamento", "Ciudad", "Tipo de Propiedad", "Latitud", "Longitud", "Superficie Total", "Superficie Construida", "Número Cuartos", "Número Baños", "Tipo Operación", "Precio"] )
        self.combo_p1.set(self.combo_p1._values[0])
        self.combo_p1.grid(row=1, column=2, padx=30, columnspan= 1, pady=20 , ipady=0, ipadx=30)
        self.combo_p2 = ctk.CTkComboBox(self.frame3_bavanzado, bg_color="#0D1B2A", corner_radius=10, width= 100, height=28,  fg_color="#19293B", state= "readonly", values =["Ninguno","Título", "Departamento", "Ciudad", "Tipo de Propiedad", "Latitud", "Longitud", "Superficie Total", "Superficie Construida", "Número Cuartos", "Número Baños", "Tipo Operación", "Precio"] )
        self.combo_p2.set(self.combo_p2._values[0])
        self.combo_p2.grid(row=1, column=3, padx=30, columnspan= 1, pady=20 , ipady=0, ipadx=30)
        self.combo_p3 = ctk.CTkComboBox(self.frame3_bavanzado, bg_color="#0D1B2A", corner_radius=10, width= 100, height=28,  fg_color="#19293B", state= "readonly", values =["Ninguno","Título", "Departamento", "Ciudad", "Tipo de Propiedad", "Latitud", "Longitud", "Superficie Total", "Superficie Construida", "Número Cuartos", "Número Baños", "Tipo Operación", "Precio"] )
        self.combo_p3.set(self.combo_p3._values[0])
        self.combo_p3.grid(row=1, column=4, padx=30, columnspan= 1, pady=20 , ipady=0, ipadx=30)
        self.combo_o1 = ctk.CTkComboBox(self.frame3_bavanzado, bg_color="#0D1B2A", corner_radius=10, width= 100, height=28,  fg_color="#19293B", state= "readonly", values =["=",">", "<", "!="] )
        self.combo_o1.set(self.combo_o1._values[0])
        self.combo_o1.grid(row=2, column=2, padx=30, columnspan= 1, pady=20 , ipady=0, ipadx=30)
        self.combo_o2 = ctk.CTkComboBox(self.frame3_bavanzado, bg_color="#0D1B2A", corner_radius=10, width= 100, height=28,  fg_color="#19293B", state= "readonly", values =["=",">", "<", "!="] )
        self.combo_o2.set(self.combo_o2._values[0])
        self.combo_o2.grid(row=2, column=3, padx=30, columnspan= 1, pady=20 , ipady=0, ipadx=30)
        self.combo_o3 = ctk.CTkComboBox(self.frame3_bavanzado, bg_color="#0D1B2A", corner_radius=10, width= 100, height=28,  fg_color="#19293B", state= "readonly", values =["=",">", "<", "!="] )
        self.combo_o3.set(self.combo_o3._values[0])
        self.combo_o3.grid(row=2, column=4, padx=30, columnspan= 1, pady=20 , ipady=0, ipadx=30)
        self.combo_ad2 = ctk.CTkComboBox(self.frame3_bavanzado, bg_color="#0D1B2A", corner_radius=10, width= 200, height=28,  fg_color="#19293B", state= "readonly", values = ["Ninguno", "Nivel", "Factor de balanceo", "Padre", "Abuelo", "Tío"] )
        self.combo_ad2.set(self.combo_ad._values[0])
        self.combo_ad2.grid(row=4, column=4, padx=0, columnspan= 1, pady=20 , ipady=0, ipadx=0)
        
        
        #Botones
        
        #Frame 1
        self.boton_insertar = ctk.CTkButton(self.button_frame, text="Insertar", bg_color="#0D1B2A", fg_color="#0353A4", corner_radius=10, width= 100, height=32, text_color="#E0E1DD", font=self.fontNormal, hover_color="#0466C8", command= self.insertar)
        self.boton_insertar.grid(row=9, column=0, padx=15, pady=10, columnspan=3, ipady=0, ipadx=0)
        
        #Frame 2
        self.boton_eliminar = ctk.CTkButton(self.frame_2_input, text="Eliminar", bg_color="#0D1B2A", fg_color="#0353A4", corner_radius=10, width= 100, height=32, text_color="#E0E1DD", font=self.fontNormal, hover_color="#0466C8", command= self.eliminar)
        self.boton_eliminar.grid(row=2, column=1, padx=80, pady=20, columnspan=1, ipady=0, sticky="nsew", ipadx=0)
        
        #Frame 3
        self.boton_buscar1 = ctk.CTkButton(self.frame3_bsimple, text="Buscar", bg_color="#0D1B2A", fg_color="#0353A4", corner_radius=10, width= 100, height=32, text_color="#E0E1DD", font=self.fontNormal, hover_color="#0466C8", command= self.buscar_premetrica)
        self.boton_buscar1.grid(row=4, column=0, padx=80, pady=20, columnspan=3, ipady=0, sticky="nsew", ipadx=20)
        self.boton_buscar2 = ctk.CTkButton(self.frame3_bavanzado, text="Buscar", bg_color="#0D1B2A", fg_color="#0353A4", corner_radius=10, width= 100, height=32, text_color="#E0E1DD", font=self.fontNormal, hover_color="#0466C8", command= self.buscar_avanzado)
        self.boton_buscar2.grid(row=5, column=3, padx=20, pady=20, columnspan=2, ipady=0, sticky="nsew", ipadx=20)
        
        #Frame 4
        self.boton_recorrer = ctk.CTkButton(self.frame4_input, text="Recorrer", bg_color="#0D1B2A", fg_color="#0353A4", corner_radius=10, width= 100, height=32, text_color="#E0E1DD", font=self.fontNormal, hover_color="#0466C8" , command= self.recorrer)
        self.boton_recorrer.grid(row=1, column=0, padx=0, pady=20, columnspan=3, ipady=0, ipadx=0)
        
        #Frame 5
        
        self.boton_mapa = ctk.CTkButton(self.frame5_input, text="Geolocalizar", bg_color="#0D1B2A", fg_color="#0353A4", corner_radius=10, width= 100, height=32, text_color="#E0E1DD", font=self.fontNormal, hover_color="#0466C8", command= self.mapear)
        self.boton_mapa.grid(row=3, column=0, padx=0, pady=20, columnspan=3, ipady=0, ipadx=0)
        
        #Text Areas
        #Frame 2
        
        self.text_area = ctk.CTkTextbox(self.frame_2_input, bg_color="#0D1B2A", corner_radius=10, width= 397, height= 417,  fg_color="#19293B")
        self.text_area.grid(row=3, column=0, padx=25, columnspan= 3, pady=20 , ipady=0, ipadx=10, sticky="nsew", rowspan= 6)
        
        #Frame 3
        self.text_area2 = ctk.CTkTextbox(self.frame3_bavanzado, bg_color="#0D1B2A", corner_radius=10, width= 550, height= 168,  fg_color="#19293B")
        self.text_area2.grid(row=6, column=1, padx=80, columnspan= 4, pady=20 , ipady=0, ipadx=40, sticky="nsew", rowspan= 3)
        
        #Frame 4
        self.text_area3 = ctk.CTkTextbox(self.frame4_input, bg_color="#0D1B2A", corner_radius=10, width= 397, height= 473,  fg_color="#19293B")
        self.text_area3.grid(row=2, column=0, padx=25, columnspan= 3, pady=20 , ipady=0, ipadx=10, sticky="nsew", rowspan= 7)
        # Selecionar frame default
        
        #Frame 5
        self.text_area4 = ctk.CTkTextbox(self.frame5_input, bg_color="#0D1B2A", corner_radius=10, width= 397, height= 307,  fg_color="#19293B")
        self.text_area4.grid(row=4, column=0, padx=25, columnspan= 3, pady=20 , ipady=0, ipadx=10, sticky="nsew", rowspan= 4)
        
        self.select_frame_by_name("home")
        
        #Map
        self.map_widget = TkinterMapView(self.frame5_map, width= 800, height= 473)
        self.map_widget.grid(row=1, column=0, padx=0, columnspan= 1, pady=0 , ipady=100, ipadx=0, sticky="nsew", rowspan= 7)
        self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&x={x}&y={y}&z={z}&s=Ga", max_zoom= 25)
        self.map_widget.set_position(4.570868, -74.297332, 10) #Bogotá
        self.map_widget.set_zoom(6)
        
        
        self.x_offset = 0
        self.y_offset = 0
        self.zoom_factor = 1.0


    def select_frame_by_name(self, name):
        # seleccionar frame
        self.home_button.configure(fg_color=("#1B263B") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("#1B263B") if name == "frame_2" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
            
        if name == "frame_2":
            self.frame2.grid(row=0, column=1, sticky="nsew")   
        else:
            self.frame2.grid_forget()
            
        if name == "frame_3":
            self.frame3.grid(row=0, column=1, sticky="nsew")
        else:
            self.frame3.grid_forget()
        if name == "frame_4":
            self.frame4.grid(row=0, column=1, sticky="nsew")
        else:
            self.frame4.grid_forget()
        if name == "frame_5":
            self.frame5.grid(row=0, column=1, sticky="nsew")
        else:
            self.frame5.grid_forget()

    # Change the value of the combo ciudad depending on the departamento selected
    
    def change_combo_ciudad(self, event):
            for dpto in self.dptos:
                if dpto.nombre == self.combo_dpto.get():
                    self.combo_ciudad.configure(values= [ciudad for ciudad in dpto.ciudades])
                    self.combo_ciudad.set(dpto.ciudades[0])
    
    def insertar(self): 
        self.label_message1.configure(text="")
        if es_default([self.text_anuncio.get(0.0 , "end"), self.combo_dpto.get(), self.combo_ciudad.get(), self.combo_tipo.get(), self.text_latitud.get(0.0 , "end"), self.text_longitud.get(0.0 , "end"), self.text_st.get(0.0 , "end"), self.text_sc.get(0.0 , "end"), self.combo_cuartos.get(), self.combo_banos.get(), self.combo_operacion.get(), self.text_precio.get(0.0 , "end")]):
            self.label_message1.configure(text="Por favor, llene todos los campos")
        else:
            if contiene_no_numero([self.text_latitud.get(0.0 , "end"), self.text_longitud.get(0.0 , "end"), self.text_sc.get(0.0 , "end"), self.text_st.get(0.0 , "end"), self.text_precio.get(0.0 , "end")]) == False:
                valor_metrica1 = int(self.text_precio.get(0.0 , "end"))/int(self.text_st.get(0.0 , "end"))
                if self.combo_ciudad.get() == "Bogotá D.C" or self.combo_ciudad.get() == "Medellín" or self.combo_ciudad.get() == "Barranquilla" or self.combo_ciudad.get() == "Cali":
                    valor_metrica2 = float(self.text_sc.get(0.0 , "end"))/ float(self.text_st.get(0.0 , "end"))
                else:
                    valor_metrica2 = (float(self.text_sc.get(0.0 , "end"))/float(self.text_st.get(0.0 , "end"))) * 0.25
                valor_nuevoNodo = [self.text_anuncio.get(0.0 , "end"), self.combo_dpto.get(), self.combo_ciudad.get(), self.combo_tipo.get(), self.text_latitud.get(0.0 , "end"), self.text_longitud.get(0.0 , "end"), self.text_st.get(0.0 , "end"), self.text_sc.get(0.0 , "end"), self.combo_cuartos.get(), self.combo_banos.get(), self.combo_operacion.get(), self.text_precio.get(0.0 , "end"), valor_metrica1, valor_metrica2]
                
                #Se inserta el nodo:
                
                self.arbol_avl.insertar(valor_nuevoNodo)
                self.plot()
                
                #Dibujar nodo insertado en el árbol
                self.label_message1.configure(text="Se ha insertado el nodo correctamente")
            else: 
                self.label_message1.configure(text="Por favor, ingrese valores numéricos en los campos correspondientes")

    def eliminar(self):
        self.text_area.delete(0.0, "end")
        if es_default([self.text_metrica.get(0.0 , "end")]):
            self.text_area.insert(0.0, "Por favor, llene todos los campos")
        else:
            if contiene_no_numero([self.text_metrica.get(0.0 , "end")]) == False:
                #Dibujar nodo eliminado en el árbol
                a_eliminar = self.buscar_metrica(self.text_metrica.get(0.0 , "end"))
                if  (a_eliminar != []):
                    #!Eliminar nodo
                    self.text_area.insert(0.0, "Se ha eliminado el nodo correctamente")
                    texto_a_mostrar = "\n".join([str(nodo.valor[12]) for nodo in a_eliminar])
                    self.text_area.insert("end", texto_a_mostrar)
                    #!Mostrar el árbol actualizado e info del nodo en el text area             
                    for i in a_eliminar:
                        self.arbol_avl.eliminar(i.valor)
                    self.plot()
                        
                    #!Mostrar el árbol actualizado e info del nodo en el text area
                    self.text_metrica.delete(0.0, tk.END)
                    self.plot()
                else:
                    #? Mostrar mensaje de sugerencia, quizás quisiste buscar (sufiere métrica más cercana)
                    self.text_area.insert(0.0, "El nodo no existe")
                
            else: 
                self.text_area.insert(0.0, "Por favor, ingrese valores numéricos en los campos correspondientes")
    
    def buscar_premetrica(self): 
        self.text_ara.delete(0.0, tk.END)
        if contiene_no_numero([self.text_met.get(0.0 , "end")]) == False:
            print(f"AAAAAAAAAAAA: {self.text_met.get(0.0 , 'end')}")
            encontrados = self.buscar_metrica(self.text_met.get(0.0 , "end"))
            if encontrados != []: 
                self.text_ara.insert(0.0, "Se ha encontrado el nodo")
                texto_a_mostrar = "\n".join([str(nodo.valor[12]) for nodo in encontrados])
                self.text_ara.insert("end", texto_a_mostrar)
                
                #Se agrega a la base el nodo encontrado
                for nodo in encontrados:
                    self.base_nodos.append(nodo)
                    
                if self.combo_ad.get() == "Nivel": 
                    for nodo in encontrados:
                        nivel = self.arbol_avl.obtener_nivel(nodo)
                        self.text_ara.insert("end", f"\nNivel: {nivel}")
                elif self.combo_ad.get() == "Factor de balanceo":
                    for nodo in encontrados:
                        factor = self.arbol_avl.obtener_balance(nodo)
                        self.text_ara.insert("end", f"\nFactor de balanceo: {factor}")
                elif self.combo_ad.get() == "Padre":
                    for nodo in encontrados:
                        padre = self.arbol_avl.buscar_padre(nodo.valor)
                        if padre == None:
                            self.text_ara.insert("end", f"\nPadre: No tiene :(")
                        else:
                            self.text_ara.insert("end", f"\nPadre: {padre.valor[12]}")
                            self.base_nodos.append(padre)
                elif self.combo_ad.get() == "Abuelo":
                    for nodo in encontrados:
                        abuelo = self.arbol_avl.buscar_abuelo(nodo.valor)
                        if abuelo   == None:
                            self.text_ara.insert("end", f"\nAbuelo: No tiene :(")
                        else:
                            self.text_ara.insert("end", f"\nAbuelo: {abuelo.valor[12]}")
                            self.base_nodos.append(abuelo)
                        
                elif self.combo_ad.get() == "Tío":
                    for nodo in encontrados:
                        tio = self.arbol_avl.buscar_tio(nodo.valor)
                        if tio == None:
                            self.text_ara.insert("end", f"\nTío: No tiene :)")
                        else:
                            self.text_ara.insert("end", f"\nTío: {tio.valor[12]}")
                            self.base_nodos.append(tio)
            else:
                self.text_ara.insert(0.0, "No se ha encontrado el nodo")
        else:
            self.text_ara.insert(0.0, "Por favor, ingrese valores numéricos en los campos correspondientes")
            
        
    def buscar_metrica(self, metrica) :
        return self.arbol_avl.buscar_por_metrica(metrica)
        
    
            
    def recorrer(self):
        self.plot()
        self.arbol_avl.string = ""
        self.arbol_avl.levelOrderTraversal(self.arbol_avl.raiz)
        
        self.text_area3.delete(0.0, tk.END)
        self.text_area3.insert(0.0, self.arbol_avl.string)
        
    
    def buscar_avanzado(self):
        combos = [self.combo_p1.get(), self.combo_p2.get(), self.combo_p3.get()]
        operadores = [self.combo_o1.get(), self.combo_o2.get(), self.combo_o3.get()]
        valor1 = eliminar_saltos_de_linea(self.text_p1.get(0.0, "end"))
        valor2 = eliminar_saltos_de_linea(self.text_p2.get(0.0, "end"))
        valor3 = eliminar_saltos_de_linea(self.text_p3.get(0.0, "end"))
        
        if valor1 == "":
            valor1 = None
        if valor2 == "":
            valor2 = None
        if valor3 == "":
            valor3 = None
        valores = [valor1, valor2, valor3]
            
        signos = []
        searchOn = []
        for combo in combos:
            if combo == "Título":
                searchOn.append(0)
            elif combo == "Departamento":
                searchOn.append(1)
            elif combo == "Ciudad":
                searchOn.append(2)
            elif combo == "Tipo de Propiedad":
                searchOn.append(3)
            elif combo == "Latitud":
                searchOn.append(4)
            elif combo == "Longitud":
                searchOn.append(5)
            elif combo == "Superficie Total":
                searchOn.append(6)
            elif combo == "Superficie Construida":
                searchOn.append(7)
            elif combo == "Número Cuartos":
                searchOn.append(8)
            elif combo == "Número Baños":
                searchOn.append(9)
            elif combo == "Tipo Operación":
                searchOn.append(10)
            elif combo == "Precio":
                searchOn.append(11)
            else: 
                searchOn.append(None)
        
        for operador in operadores: 
            if operador == "=":
                signos.append("Equal")
            elif operador == ">":
                signos.append("Greater Than")
            elif operador == "<":
                signos.append("Less Than")
            elif operador == "!=":
                signos.append("Not Equal")
            else:
                signos.append(None)
        print(f"Valores: {valores[0]}")
        resultado = self.arbol_avl.busqueda_multiple(valores[0], searchOn[0], signos[0], valores[1], searchOn[1], signos[1], valores[2], searchOn[2], signos[2])
        
        if resultado != []:
            self.text_area2.delete(0.0, tk.END)
            self.text_area2.insert(0.0, "Se ha encontrado el nodo")
            texto_a_mostrar = "\n".join([str(nodo.valor[12]) for nodo in resultado])
            self.text_area2.insert("end", texto_a_mostrar)
            for nodo in resultado:
                self.base_nodos.append(nodo)
        else: 
            self.text_area2.delete(0.0, tk.END)
            self.text_area2.insert(0.0, "No se ha encontrado el nodo")
    
    def mapear(self):
        for nodo in self.base_nodos:
            self.map_widget.set_position(float(nodo.valor[4]), float(nodo.valor[5]), marker= True)
        
    
    def plot(self):
        plot_avl_tree(self.arbol_avl.raiz)
        self.image = Image.open("avl_tree.png")
        self.image_tk = ImageTk.PhotoImage(self.image)

    
        
    
        
if __name__ == "__main__":
    app = App()
    app.resizable(False, False)
    app.mainloop()