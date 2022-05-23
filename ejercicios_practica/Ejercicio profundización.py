import json
import requests
import matplotlib.pyplot as plt


def fetch():
    # URL de descarga de datos
    url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20Mendoza%20&limit=50'

    # Descarga de datos
    response = requests.get(url)
    dataset = response.json()
    json_response = dataset["results"]

    # Filtrar datos deseados si el precio está en ARS
    global filtro
    filtro = [{"price": x["price"] , "condition": x["condition"]} for x in json_response if x["currency_id"] == "ARS"]
    #print(json.dumps(filtro, indent=4))

def transform(filtro, min, max):
  
    # Arma la partición de listas 
    list_min = []
    list_min_max = []
    list_max = []

    # Precios por parámetro
    for datos in filtro :
        if datos["price"] <= min:
            list_min.append(datos["price"])
        elif datos["price"] >= min and datos["price"] <= max:
            list_min_max.append(datos["price"])
        else :
            list_max.append(datos["price"]) 

    llist_min = len(list_min)
    llist_min_max = len(list_min_max)
    llist_max = len(list_max)
    return[llist_min, llist_min_max, llist_max]

def report(data):   
    plt.title('Costo de alquiler en Mendoza')
    costo = ['Debajo del min', 'Medio', 'Arriba del max']
    colores = ["#EE6055","#60D394","#AAF683"]
    desfase = (0.1, 0.1, 0.1)
    plt.pie(data, labels=costo, autopct="%0.1f %%", colors=colores, explode=desfase)
    plt.axis("equal")
    plt.show()


if __name__ == "__main__":
    min = 5500
    max = 15000

    dataset = fetch()
    data = transform(filtro, min, max)
    data = report(data)
