from requests import request


def calculadora():

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print("Seleccione la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    operacion = input("Ingrese el número de la operación (1/2/3/4): ")
    if operacion == '1':
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")
    elif operacion == '2':
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}")
    elif operacion == '3':
        resultado = num1 * num2
        print(f"El resultado de la multiplicación es: {resultado}")
    elif operacion == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"El resultado de la división es: {resultado}")  
    else:
        print("Operación no válida")




using (request)
def obtener_genero(nombre):
  
    url = f"https://api.agify.io/?name={nombre}"
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        if 'age' in datos:
            return datos['age']
        else:
            return "No se pudo determinar el género."
    else:
        return "Error al realizar la solicitud."

def main():
    nombre = input("Ingrese un nombre: ")
    genero = obtener_genero(nombre)
    print(f"El género del nombre {nombre} es: {genero}")
    calculadora()

