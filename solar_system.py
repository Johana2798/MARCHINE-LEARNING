'''
Script description: Get all data about the solar system.
'''

import os
import requests 

os.system('clear')

def getData():
    print("::: COMETS INFORMATION :::\n")

    url = "https://api.le-systeme-solaire.net/rest/bodies/?filter[]=isComet,eq,true"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        for body in data.get('bodies', []):
            name = body.get('englishName', 'N/A')
            abs_mag = body.get('absoluteMagnitude', 'N/A')
            abs_mag_h = body.get('mag', 'N/A')
            diameter_km = body.get('meanRadius', 'N/A')
            diameter_ft = round(diameter_km * 3280.84, 2) if isinstance(diameter_km, (int, float)) else 'N/A'

            print(f" Nombre: {name}")
            print(f" Magnitud absoluta: {abs_mag}")
            print(f" Magnitud h: {abs_mag_h}")
            print(f" Diámetro estimado (KM): {diameter_km}")
            print(f" Diámetro estimado (FT): {diameter_ft}")
            print("-" * 40)

    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")

getData()