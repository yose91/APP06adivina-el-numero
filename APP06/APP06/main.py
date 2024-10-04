import flet as ft
import random

#Función principal
def main(page: ft.page):
    #Variables globales
    global numero_secreto,entrada_numero,texto_resultado,boton_adivinar
    
    page.title = "Adivinar el número"
    
    #Generar un número aleatorio
    numero_secreto = random.randint(1,100)
    
    #Crear los elementos de la interfaz
    titulo=ft.Text("Adivina el número secreto entre 1 y 100",size=20,color="white")
    entrada_numero=ft.TextField(label="Tu Adivinanza",width=150)
    boton_adivinar=ft.ElevatedButton("Adivinar")
    texto_resultado=ft.Text("",color="white")
    
    contenedor_principal=ft.Container(
        content=ft.Column(
            controls=[
                titulo,
                entrada_numero,
                boton_adivinar,
                texto_resultado,
                ft.image(
                    src="https://i.ibb.co/Gxgryg9/laser.gif",
                    fit=ft.ImageFit.COVER,
                    width=350,
                    height=200,
                )
            ],alignment="CENTER",
            horizontal_aligment="CENTER",
            spacing=28
        ),
        bgcolor="red",
        whidth=page.window.width,
        height=page.window.height,
        padding=20
        
            
    )
    page.add(contenedor_principal)

    

ft.app(main)
