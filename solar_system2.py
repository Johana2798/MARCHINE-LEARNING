'''
Script description: Get all data about the solar system.
'''

import os
import requests

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def fetch_data(filter_type=None):
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    if filter_type:
        url += f"?filter[]=bodyType,eq,{filter_type}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get("bodies", [])
    except requests.exceptions.RequestException as e:
        print(f"Error al consultar la API: {e}")
        return []

def display_bodies(bodies):
    for body in bodies:
        print(f"Nombre: {body.get('englishName')}")
        print(f"Tipo: {body.get('bodyType')}")
        print(f"Gravedad: {body.get('gravity')} m/s²")
        print(f"Descubrimiento: {body.get('discoveryDate')}")
        print("-" * 40)

def main_menu():
    while True:
        clear_screen()
        print("::: MENÚ DEL SISTEMA SOLAR :::")
        print("1. Planetas")
        print("2. Lunas")
        print("3. Asteroides")
        print("4. Cometas")
        print("5. Salir")

        choice = input("Selecciona una opción: ")

        if choice == "1":
            bodies = fetch_data("Planet")
            display_bodies(bodies)
        elif choice == "2":
            bodies = fetch_data("Moon")
            display_bodies(bodies)
        elif choice == "3":
            bodies = fetch_data("Asteroid")
            display_bodies(bodies)
        elif choice == "4":
            bodies = fetch_data("Comet")
            display_bodies(bodies)
        elif choice == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

        input("\nPresiona Enter para continuar...")

main_menu()