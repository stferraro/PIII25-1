import requests
from bs4 import BeautifulSoup

url = "https://www.infodolar.com.do/precio-dolar-entidad-banco-bhd.aspx"  # Cambia la URL según el banco

try:
    response = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    })
    response.raise_for_status()
    html_content = response.text
except requests.exceptions.RequestException as e:
    print(f"Error al obtener la página web: {e}")
    exit()

soup = BeautifulSoup(html_content, 'lxml')

try:
    # Busca el span con id="lblVenta" que contiene la tasa de venta del dólar
    tipo_cambio_elemento = soup.find('span', id='lblVenta')
    if tipo_cambio_elemento:
        tipo_cambio = tipo_cambio_elemento.text.strip().replace('$', '').replace(',', '')
        print(f"Tipo de cambio: {tipo_cambio}")
    else:
        print("No se encontró el elemento con el tipo de cambio.")
except Exception as e:
    print(f"Error al encontrar el tipo de cambio: {e}")