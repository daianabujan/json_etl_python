# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json


def serializar():
    print("Funcion que genera un archivo JSON")
    # JSON Serialize
    # Armar un JSON que represente los datos personales
    # de su persona (puede invitar los datos sino quiere exponer
    # información confidencial)

    # Debe armar un JSON que tenga como datos
    # nombre, apellido, DNI
    # Dentro debe tener una lista donde coloque cantidad de elementos de vestir
    # ejemplo -->
    #  { "prenda": "zapatilla", "cantidad": 4 }
    #  { "prenda": "remeras", "cantidad": 12 }
    # Que su lista de prendas dentro del JSON tenga al menos 2 prendas

    # json_data = {...}

    # Una vez que finalice el JSON realice un "dump" para almacenarlo en
    # un archivo que usted defina

    # Observe el archivo y verifique que se almaceno lo deseado

    json_data = {
                "Nombre" : "Daiana",
                "Apellido" : "Bujan",
                "DNI" : "36159789",
                "Ropa" : [
                        {
                        "Prenda" : "Buzo",
                        "Cantidad" : 3
                        },
                        {
                        "Prenda" : "Zapatos",
                        "Cantidad" : 6
                        },
                        {
                        "Prenda" : "Campera",
                        "Cantidad" : 4
                        }
                        ]
                }

    with open ('json_ropa.json', 'w') as jsonfile:
        ropa = [json_data]
        json.dump(ropa, jsonfile, indent=4)

    print(ropa)

def deserializar():
    print("Funcion que lee un archivo JSON")
    # JSON Deserialize
    # Basado en la función  anterior debe abrir y leer el contenido
    # del archivo y guardarlo en un objeto JSON utilizando el método
    # load()

    # Luego debe convertir ese JSON data en json_string utilizando
    # el método "dumps" y finalmente imprimir en pantalla el resultado
    # Recuerde utilizar indent=4 para poder observar mejor el resultado
    # en pantalla y comparelo contra el JSON que generó en la función anterior

    with open ('json_ropa.json', 'r') as jsonfile:
        ropa = json.load(jsonfile)
    print(json.dumps(ropa, indent=4))


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    serializar()
    deserializar()

    print("terminamos")